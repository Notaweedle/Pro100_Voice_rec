# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
import speech_recognition as sr

class Widget(QWidget):
    recording = False
    end_recording_func = None
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        #testing stuff
        self.ui.addItemButton.clicked.connect(self.addItem)
        self.ui.listWidget.itemClicked.connect(self.selectItemInList)
        self.ui.removeItemButton.clicked.connect(self.removeItem)

        #recording stuff
        self.ui.startRecordingBtn.clicked.connect(self.startRecording)
        self.ui.stopRecordingBtn.clicked.connect(self.stopRecording)

        # adjust for ambient noise
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)


    #testing functionz
    def addItem(self):
        text = self.ui.itemEdit.text()
        if text and text != "":
            self.ui.listWidget.addItem(text)
            self.ui.itemEdit.clear()


    def selectItemInList(self, item):
        self.ui.listWidget.setCurrentItem(item)


    def removeItem(self):
        currentItem = self.ui.listWidget.currentItem()
        #currentItem.setText(currentItem.text() + " e")
        row = self.ui.listWidget.row(currentItem)
        deletedItem = self.ui.listWidget.takeItem(row)
        del deletedItem


    #recording functionz
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
