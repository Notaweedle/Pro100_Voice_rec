# This Python file uses the following encoding: utf-8
#TODO this was just moved frm widget.py nothing is really working or updated
import speech_recognition as sr

class Recorder():
    # variables used for recording and processing
    recording = False
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)

    def __init__(self, parent=None):
        pass

        #recording stuff
        #self.ui.startRecordingBtn.clicked.connect(self.startRecording)
        #self.ui.stopRecordingBtn.clicked.connect(self.stopRecording)

    #recording functionz
    #TODO revamp, move to new module?
    def startRecording(self):
        if not self.recording:
            # start recording here
            self.end_recording = self.r.listen_in_background(self.mic, callback=self.test_callback)
            # adjust boolean values
            self.ui.startRecordingBtn.setEnabled(False)
            self.ui.stopRecordingBtn.setEnabled(True)
            self.recording = True

    def stopRecording(self):
        if self.recording:
            # stop the recording here
            if self.end_recording is not None:
                self.end_recording(False)
            # adjust boolean values
            self.ui.startRecordingBtn.setEnabled(True)
            self.ui.stopRecordingBtn.setEnabled(False)
            self.recording = False

    def test_callback(self, recognizer, audio):
        text_recognized = recognizer.recognize_whisper(audio, language="english")
        #text_recognized = recognizer.recognize_sphinx(audio, language="en-US")
        if text_recognized and text_recognized != "":
            self.ui.listWidget.addItem(text_recognized)

# if __name__ == "__main__":
#     pass
