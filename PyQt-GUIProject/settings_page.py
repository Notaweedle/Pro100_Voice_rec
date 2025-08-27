# i think i like this idea more where i branch out each tab into its own class
# so that the code is more readable and organized
import math

class SettingsPageHandler():

    # setup settings ui
    def __init__(self, parentWindow):
        self.parentWindow = parentWindow

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

        # OTHER POSSIBILITIES
        # reset to default button for all settings (or specific?)
        # json file path settings
        # have to move calibration into here too

    def onChangeInputDevice(self, inputbox_index):
        input_device = self.parentWindow.ui.inputDeviceBox.currentText()
        print("Output Device Changed: " + input_device)

    def onChangeInputVolSlider(self, new_vol):
        # make sure the other is only being updated once
        # since these could trigger each other in an infinite loop
        spinBox = self.parentWindow.ui.inputVolSpinBox
        old_vol = spinBox.value()
        if new_vol != old_vol:
            spinBox.setValue(new_vol)

        # only one of these needs to call updateInputVolume
        # since both of these will get triggered when one changes
        self.updateInputVolume(new_vol)


    def onChangeInputVolSpinBox(self, new_vol):
        slider = self.parentWindow.ui.inputVolSlider
        old_vol = slider.value()
        if new_vol != old_vol:
            slider.setValue(new_vol)

    def updateInputVolume(self, volume):
        # volume passed and assigned to a variable in the recorder class (probably...)
        print("Input Volume Changed: " + str(volume))

    def onChangeOutputDevice(self, inputbox_index):
        output_device = self.parentWindow.ui.outputDeviceBox.currentText()
        print("Output Device Changed: " + output_device)

    def onChangeOutputVolSlider(self, new_vol):
        spinBox = self.parentWindow.ui.outputVolSpinBox
        old_vol = spinBox.value()
        if new_vol != old_vol:
            spinBox.setValue(new_vol)
        self.updateOutputVolume(new_vol)

    def onChangeOutputVolSpinBox(self, new_vol):
        slider = self.parentWindow.ui.outputVolSlider
        old_vol = slider.value()
        if new_vol != old_vol:
            slider.setValue(new_vol)

    def updateOutputVolume(self, volume):
        # volume passed and assigned to a variable in future TTS module
        print("Output Volume Changed: " + str(volume))

    def onChangeTextToSpeech(self, checked):
        if checked:
            print("Text to Speech turned on!")
        else:
            print("Text to Speech turned off!")

    def onChangePauseThreshSlider(self, new_value):
        spinBox = self.parentWindow.ui.pauseThreshSpinBox
        old_value = round(spinBox.value(), 2)
        new_value = round(new_value / 100, 2)
        if new_value != old_value:
            spinBox.setValue(new_value)

        self.updatePauseThresh(new_value)

    def onChangePauseThreshSpinBox(self, new_value):
        slider = self.parentWindow.ui.pauseThreshSlider
        new_value = round(new_value * 100)
        old_value = slider.value()
        if new_value != old_value:
            slider.setValue(new_value)

    def updatePauseThresh(self, pause_threshold):
        print("Pause Threshold Changed: " + str(pause_threshold))

