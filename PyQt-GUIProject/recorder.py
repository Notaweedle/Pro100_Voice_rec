
import speech_recognition as sr
import re, time
from command_processes import audio as a
from difflib import SequenceMatcher
activation_keywords = ["hey rat",'yo rat', 'rat', 'hello rat']

class Recorder():
    def __init__(self, callbackFunc, startRecordingBtn, stopRecordingBtn, parent=None):
        # used for recording and processing
        self.recording = False
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        #self.stream = self.r.listen_in_background(self.mic, callback=self.test_callback)
        self.passive_on = True

        self.callbackFunc = callbackFunc
        self.startRecordingBtn = startRecordingBtn
        self.stopRecordingBtn = stopRecordingBtn

    #recording functionz
    def startRecording(self):
        if not self.recording:
            #self.passive_on = False
            # start recording here
            self.end_recording = self.stream
            # adjust boolean values
            self.startRecordingBtn.setEnabled(False) # CHANGE
            self.stopRecordingBtn.setEnabled(True) # CHANGE
            self.recording = True

    def stopRecording(self):
        if self.recording:
            #self.passive_on = True
            # stop the recording here
            if self.end_recording is not None:
                self.end_recording(False)
                #time.sleep(4)
                #self.stream = self.r.listen_in_background(self.mic, callback=self.test_callback)
            # adjust boolean values
            self.startRecordingBtn.setEnabled(True) # CHANGE
            self.stopRecordingBtn.setEnabled(False) # CHANGE
            self.recording = False

    def test_callback(self, recognizer, audio):
        # first, recognize the text
        if self.model.lower() == "whisper":
            text_recognized = recognizer.recognize_whisper(audio, language="english") # CHANGE TO BELOW
        elif self.model.lower() == "pocketsphinx":
            text_recognized = recognizer.recognize_sphinx(audio)
        elif self.model.lower() == "vosk":
            try:
                text_recognized = recognizer.recognize_vosk(audio)
            except Exception as e:
                print("Exception occured: ", e)
        text_recognized = recognizer.recognize_whisper(audio, language="english")# CHANGE TO BELOW
        #text_recognized = recognizer.recognize_vosk(audio)
        #text_recognized = recognizer.recognize_pocketsphinx(audio)

        # now use the text to execute a command
        if text_recognized and text_recognized != "":
            #self.ui.listWidget.addItem(text_recognized)
            parsed = self.parse_whisper_text(text_recognized)
            
            if self.passive_on == True:
                print(parsed)
                if is_activation_match(parsed, activation_keywords):
                    a.speak("Yes?")
                    self.passive_on = False
            else:
                self.callbackFunc(parsed)
                self.passive_on = True
            if self.model.lower() == "vosk":
                parsed = self.parse_vosk_text(text_recognized)
                #if self.passive_on == True:
                #    print(parsed)
                #    if self.listening_phrase in parsed:
                #        a.speak("Yes?")
                #        self.passive_on = False
                #else:
                #    self.callbackFunc(parsed)
                #    self.passive_on = True
                self.callbackFunc(parsed)
            else:
                #parsed = self.parse_whisper_text(text_recognized)
                #if self.passive_on == True:
                #    print(parsed)
                #    if self.listening_phrase in parsed:
                #        a.speak("Yes?")
                #        self.passive_on = False
                #else:
                #    self.callbackFunc(parsed)
                #    self.passive_on = True
                self.callbackFunc(parsed)


    # formats audio returned from recognize_whisper to remove punctuation, capitalization, etc.
    def parse_whisper_text(self, text):
        text = text.strip().lower()
        text = re.sub(r"[^A-Za-z0-9 ]", "", text)
        return text

    def parse_vosk_text(self, text):
        text = json.loads(text)['text']
        return text

    def start_passive(self):
        self.r.listen_in_background(self.mic, callback=self.test_callback)
        #self.end_recording = self.stream
    def changeMic(self):
        #self.mic = sr.Microphone(device_index=1)
        pass
# ________________________________________________________________________________________

    def startPassive(self):
        self.end_recording = self.stream


def is_activation_match(text, keywords, threshold=0.8):
    for keyword in keywords:
        ratio = SequenceMatcher(None, text.lower(), keyword).ratio()
        if ratio >= threshold:
            return True
    return False
