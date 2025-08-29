
import speech_recognition as sr
import re, time, json
import threading
from command_processes import audio as a
from difflib import SequenceMatcher
activation_keywords = ["hey rat",'yo rat', 'rat', 'hello rat']

class Recorder():
    def __init__(self, callbackFunc, startRecordingBtn, stopRecordingBtn, parent=None):
        # used for recording and processing
        self.recording = False
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

        # passive listening stuff
        self.listening_phrase = "hey rat"
        self.stream = None
        self.passive_on = True
        #self.stop_thread = threading.Event()
        self.passive_thread = threading.Thread(target=self.start_passive, daemon=True)

        self.callbackFunc = callbackFunc
        self.startRecordingBtn = parentWindow.ui.startRecordingBtn
        self.stopRecordingBtn = parentWindow.ui.stopRecordingBtn

        self.startRecordingBtn.setEnabled(False)

    def update_settings(self, input_device, input_volume, pause_threshold, model):
        if self.stream is not None:
            self.stream(False)

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

        # start recording
        self.stream = self.r.listen_in_background(self.mic, callback=self.rec_callback)


    #recording functionz
    def startRecording(self):
        self.passive_on = False
        if not self.recording:
            # start recording here
            #self.end_recording = self.stream
            #self.end_recording = self.r.listen_in_background(self.mic, callback=self.rec_callback)
            # adjust boolean values
            self.startRecordingBtn.setEnabled(False) # CHANGE
            self.stopRecordingBtn.setEnabled(True) # CHANGE
            self.recording = True

    def stopRecording(self):
        if self.recording:
            # stop the recording here
            if self.end_recording is not None:
                self.end_recording(False)
                #time.sleep(4)
                #self.stream = self.r.listen_in_background(self.mic, callback=self.rec_callback)
            # adjust boolean values
            self.startRecordingBtn.setEnabled(True) # CHANGE
            self.stopRecordingBtn.setEnabled(False) # CHANGE
            self.recording = False
            self.passive_on = True

    def rec_callback(self, recognizer, audio):
        # first, recognize the text
        if self.model.lower() == "whisper":
            text_recognized = recognizer.recognize_whisper(audio, language="english")
        elif self.model.lower() == "pocketsphinx":
            text_recognized = recognizer.recognize_sphinx(audio)
        elif self.model.lower() == "vosk":
            try:
                text_recognized = recognizer.recognize_vosk(audio)
            except Exception as e:
                print("Exception occured: ", e)

        if text_recognized and text_recognized != "":
            if self.model.lower() == "vosk":
                parsed = self.parse_vosk_text(text_recognized)
            else:
                parsed = self.parse_whisper_text(text_recognized)

            if self.passive_on == True:
                print(parsed)
                if self.listening_phrase in parsed:
                    a.speak("Yes?")
                    self.passive_on = False
            else:
                self.callbackFunc(parsed)
                self.passive_on = True

    # formats audio returned from recognize_whisper to remove punctuation, capitalization, etc.
    def parse_whisper_text(self, text):
        text = text.strip().lower()
        text = re.sub(r"[^A-Za-z0-9 ]", "", text)
        return text

    def changeMic(self):
        #self.mic = sr.Microphone(device_index=1)
        pass
# ________________________________________________________________________________________

    def start_passive(self, stop_event):
        self.stream = self.r.listen_in_background(self.mic, callback=self.rec_callback)
        while self.stream:
            self.end_recording = self.stream


def is_activation_match(text, keywords, threshold=0.8):
    for keyword in keywords:
        ratio = SequenceMatcher(None, text.lower(), keyword).ratio()
        if ratio >= threshold:
            return True
    return False
