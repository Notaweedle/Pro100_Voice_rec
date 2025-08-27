# i think i like this idea more where i branch out each tab into its own class
# so that the code is more readable and organized
from PySide6 import QtWidgets
from settings_handler import SettingsHandler
from confirm_dialog import ConfirmDialog
import pyaudio, os

class SettingsPageHandler():

    # setup settings ui
    def __init__(self, parentWindow):
        self.parentWindow = parentWindow
        self.SettingsHandler = SettingsHandler(self)
        # load available inputs and outputs
        self.getInputDevices()
        self.getOutputDevices()
        # then load settings from json
        self.SettingsHandler.load_settings()

        # input device and volume
        self.parentWindow.ui.inputDeviceBox.currentIndexChanged.connect(self.onChangeInputDevice)
        self.parentWindow.ui.inputVolSlider.valueChanged.connect(self.onChangeInputVolSlider)
        self.parentWindow.ui.inputVolSpinBox.valueChanged.connect(self.onChangeInputVolSpinBox)
        # output device and volume
        self.parentWindow.ui.outputDeviceBox.currentIndexChanged.connect(self.onChangeOutputDevice)
        self.parentWindow.ui.outputVolSlider.valueChanged.connect(self.onChangeOutputVolSlider)
        self.parentWindow.ui.outputVolSpinBox.valueChanged.connect(self.onChangeOutputVolSpinBox)
        # text to speech checkbox
        self.parentWindow.ui.ttsCheckBox.toggled.connect(self.onChangeTextToSpeech)
        # pause threshold
        self.parentWindow.ui.pauseThreshSlider.valueChanged.connect(self.onChangePauseThreshSlider)
        self.parentWindow.ui.pauseThreshSpinBox.valueChanged.connect(self.onChangePauseThreshSpinBox)
        # speech model box
        self.parentWindow.ui.speechModelBox.currentIndexChanged.connect(self.onChangeSpeechModel)
        # save dir box
        self.parentWindow.ui.chooseSaveDirBtn.clicked.connect(self.onChooseSaveDir)
        # save settings button
        self.parentWindow.ui.saveSettingsBtn.clicked.connect(self.onSaveSettings)

        # OTHER POSSIBILITIES
        # reset to default button for all settings (or specific?)
        # json file path settings
        # have to move calibration into here too

    def loadSettings(self, settings):
        # setting up all the
        self.input_device = settings['input_device']
        self.input_volume = settings['input_volume']
        self.output_device = settings['output_device']
        self.output_volume = settings['output_volume']
        self.tts_enabled = settings['text_to_speech']
        self.pause_threshold = settings['pause_threshold']
        self.model = settings['speech_model']
        self.save_directory = settings['save_directory']

        # special parsing for input device box
        index = self.parentWindow.ui.inputDeviceBox.findText(self.input_device['name'])
        if index != -1:
            self.parentWindow.ui.inputDeviceBox.setCurrentIndex(index)
        else:
            self.parentWindow.ui.inputDeviceBox.setCurrentText('Default')
            self.input_device = {'name': 'Default', 'index': None}
        # setting both input volume boxes
        self.parentWindow.ui.inputVolSlider.setValue(self.input_volume)
        self.parentWindow.ui.inputVolSpinBox.setValue(self.input_volume)

        # special parsing for output device box
        index = self.parentWindow.ui.outputDeviceBox.findText(self.output_device['name'])
        if index != -1:
            self.parentWindow.ui.outputDeviceBox.setCurrentIndex(index)
        else:
            self.parentWindow.ui.outputDeviceBox.setCurrentText('Default')
            self.output_device = {'name': 'Default', 'index': None}
        # setting both output volume boxes
        self.parentWindow.ui.outputVolSlider.setValue(self.output_volume)
        self.parentWindow.ui.outputVolSpinBox.setValue(self.output_volume)

        # other settings!!!
        self.parentWindow.ui.ttsCheckBox.setChecked(self.tts_enabled)
        self.parentWindow.ui.pauseThreshSlider.setValue(self.pause_threshold * 100)
        self.parentWindow.ui.pauseThreshSpinBox.setValue(self.pause_threshold)
        self.parentWindow.ui.speechModelBox.setCurrentText(self.model)
        self.parentWindow.ui.saveDirEdit.setText(self.save_directory)

        # now all of these need to be passed to their respective modules
        self.setEachSetting(is_startup=True)

    def onSaveSettings(self):
        # get each setting value from self.SettingName
        # and then pass to where each need to go (most do not have a place yet tho)
        settings = {}
        #input settings
        settings['input_device'] = self.input_device
        settings['input_volume'] = self.input_volume
        #output settings
        settings['output_device'] = self.output_device
        settings['output_volume'] = self.output_volume
        #other
        settings['text_to_speech'] = self.tts_enabled
        settings['pause_threshold'] = self.pause_threshold
        settings['speech_model'] = self.model
        settings['save_directory'] = self.save_directory
        # save to file
        self.SettingsHandler.save_settings(settings)
        # set each individually
        self.setEachSetting(is_startup=False)

    def setEachSetting(self, is_startup):
        #input device + volume + pause threshold + model
        # all need to be given to recorder
        self.parentWindow.Recorder.update_settings(self.input_device, self.input_volume, self.pause_threshold, self.model)

        # output device + volume + tts_enabled
        # all need to be given to tts module
        #TODO

        # save_directory
        # needs to be given to command_handler
        if is_startup:
            self.parentWindow.CommandHandler.load_data_dir(self.save_directory)
        else:
            self.parentWindow.CommandHandler.change_data_dir(self.save_directory)

    def getInputDevices(self):
        working_mics = self.parentWindow.Recorder.mic.list_working_microphones()
        inputDeviceBox = self.parentWindow.ui.inputDeviceBox
        for key in working_mics:
            inputDeviceBox.insertItem(inputDeviceBox.count()+1, working_mics[key], key)

    def getOutputDevices(self):
        p = pyaudio.PyAudio()
        info = p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        output_devices = []
        for i in range(0, numdevices):
            device = {}
            device_info = p.get_device_info_by_index(i)
            device['name'] = device_info.get('name')
            device['index'] = i

            if device_info.get('maxOutputChannels') > 0:
                output_devices.append(device)
        p.terminate()

        outputDeviceBox = self.parentWindow.ui.outputDeviceBox
        for device in output_devices:
            outputDeviceBox.insertItem(outputDeviceBox.count()+1, device['name'], device['index'])

    def onChangeInputDevice(self, inputbox_index):
        self.input_device = {}
        self.input_device['name'] = self.parentWindow.ui.inputDeviceBox.currentText()
        self.input_device['index'] = self.parentWindow.ui.inputDeviceBox.currentData()
        print("Input Device Changed: " + self.input_device['name'] + " (" + str(self.input_device['index']) + ")")

    def onChangeInputVolSlider(self, new_vol):
        # make sure the other is only being updated once
        # since these could trigger each other in an infinite loop
        spinBox = self.parentWindow.ui.inputVolSpinBox
        old_vol = spinBox.value()
        if new_vol != old_vol:
            spinBox.setValue(new_vol)

        # only one of these needs to call updateInputVolume
        # since both of these will get triggered when one changes
        self.input_volume = new_vol


    def onChangeInputVolSpinBox(self, new_vol):
        slider = self.parentWindow.ui.inputVolSlider
        old_vol = slider.value()
        if new_vol != old_vol:
            slider.setValue(new_vol)

    def onChangeOutputDevice(self, inputbox_index):
        self.output_device = {}
        self.output_device['name'] = self.parentWindow.ui.outputDeviceBox.currentText()
        self.output_device['index'] = self.parentWindow.ui.outputDeviceBox.currentData()
        print("Output Device Changed: " + self.output_device['name'] + " (" + str(self.output_device['index']) + ")")

    def onChangeOutputVolSlider(self, new_vol):
        spinBox = self.parentWindow.ui.outputVolSpinBox
        old_vol = spinBox.value()
        if new_vol != old_vol:
            spinBox.setValue(new_vol)
        self.output_volume = new_vol

    def onChangeOutputVolSpinBox(self, new_vol):
        slider = self.parentWindow.ui.outputVolSlider
        old_vol = slider.value()
        if new_vol != old_vol:
            slider.setValue(new_vol)

    def onChangeTextToSpeech(self, checked):
        if checked:
            self.tts_enabled = True
            #print("Text to Speech turned on!")
        else:
            self.tts_enabled = False
            #print("Text to Speech turned off!")

    def onChangePauseThreshSlider(self, new_value):
        spinBox = self.parentWindow.ui.pauseThreshSpinBox
        old_value = round(spinBox.value(), 2)
        new_value = round(new_value / 100, 2)
        if new_value != old_value:
            spinBox.setValue(new_value)

        self.pause_threshold = new_value

    def onChangePauseThreshSpinBox(self, new_value):
        slider = self.parentWindow.ui.pauseThreshSlider
        new_value = round(new_value * 100)
        old_value = slider.value()
        if new_value != old_value:
            slider.setValue(new_value)

    def onChangeSpeechModel(self, inputbox_index):
        self.model = self.parentWindow.ui.speechModelBox.currentText()
        if self.model == "Vosk":
            self.ConfirmDialog = ConfirmDialog("Vosk Model Warning", "Please download the model from https://alphacephei.com/vosk/models and unpack in opened folder as \"/model\".", None, "Okay")
            self.ConfirmDialog.setModal(True)
            self.ConfirmDialog.show()
            os.startfile(os.path.abspath("../"))
        #print("Speech Model Changed: " + self.model)

    def onChooseSaveDir(self):
        self.FileDialog = QtWidgets.QFileDialog()
        self.FileDialog.setFileMode(QtWidgets.QFileDialog.FileMode.Directory)
        self.FileDialog.setModal(True)
        self.FileDialog.finished.connect(self.changeSaveDir)
        self.FileDialog.open()

    def changeSaveDir(self):
        selected_files = self.FileDialog.selectedFiles()
        if len(selected_files) > 0:
            self.save_directory = selected_files[0]
            self.parentWindow.ui.saveDirEdit.setText(self.save_directory)
