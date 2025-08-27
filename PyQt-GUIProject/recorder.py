import speech_recognition as sr
import re, json

class Recorder():
    def __init__(self, parentWindow, callbackFunc):
        # used for recording and processing
        self.recording = False
        self.r = sr.Recognizer()
        self.parentWindow = parentWindow

        # defaults, unnecessary now
        #self.input_device = "Default"
        #self.model = "whisper"
        # this one necessary tho for getting available microphones
        self.mic = sr.Microphone()

        self.callbackFunc = callbackFunc
        self.startRecordingBtn = parentWindow.ui.startRecordingBtn
        self.stopRecordingBtn = parentWindow.ui.stopRecordingBtn

        self.startRecordingBtn.setEnabled(False)

    def update_settings(self, input_device, input_volume, pause_threshold, model):
        # input device handling
        self.input_device = input_device
        if input_device['name'].lower() == "default":
            self.mic = sr.Microphone()
        else:
            self.mic = sr.Microphone(device_index=input_device['index'])

        # for now input volume is useless
        self.input_volume = input_volume

        # pause threshold handling
        self.r.pause_threshold = pause_threshold

        # model updating (should always be in here, since it is a pre-set input)
        if model.lower() in ["whisper", "vosk", "pocketsphinx"]:
            self.model = model

        # for the first time that settings are loaded
        # startRecording button will be turned on
        # this check prevents it from updating when the user is recording since the button is also off then
        # altho i should probably make it so settings cant be changed while recording!
        if not self.recording:
            self.startRecordingBtn.setEnabled(True)

    #recording functionz
    def startRecording(self):
        if not self.recording:
            # start recording here
            self.end_recording = self.r.listen_in_background(self.mic, callback=self.test_callback)
            # adjust boolean values
            self.startRecordingBtn.setEnabled(False)
            self.stopRecordingBtn.setEnabled(True)
            self.parentWindow.ui.saveSettingsBtn.setEnabled(False)
            self.parentWindow.ui.resetDefaultSettingsBtn.setEnabled(False)
            self.recording = True

    def stopRecording(self):
        if self.recording:
            # stop the recording here
            if self.end_recording is not None:
                self.end_recording(False)
            # adjust boolean values
            self.startRecordingBtn.setEnabled(True)
            self.stopRecordingBtn.setEnabled(False)
            self.parentWindow.ui.saveSettingsBtn.setEnabled(True)
            self.parentWindow.ui.resetDefaultSettingsBtn.setEnabled(True)
            self.recording = False

    def test_callback(self, recognizer, audio):
        if self.model.lower() == "whisper":
            text_recognized = recognizer.recognize_whisper(audio, language="english") # CHANGE TO BELOW
        elif self.model.lower() == "pocketsphinx":
            text_recognized = recognizer.recognize_sphinx(audio)
        elif self.model.lower() == "vosk":
            try:
                text_recognized = recognizer.recognize_vosk(audio)
            except Exception as e:
                print("Exception occured: ", e)

        if text_recognized and text_recognized != "":
            #self.ui.listWidget.addItem(text_recognized)
            if self.model.lower() == "vosk":
                parsed = self.parse_vosk_text(text_recognized)
                self.callbackFunc(parsed)
            else:
                parsed = self.parse_whisper_text(text_recognized)
                self.callbackFunc(parsed)

    # formats audio returned from recognize_whisper to remove punctuation, capitalization, etc.
    def parse_whisper_text(self, text):
        text = text.strip().lower()
        text = re.sub(r"[^A-Za-z0-9 ]", "", text)
        return text

    def parse_vosk_text(self, text):
        text = json.loads(text)['text']
        return text

