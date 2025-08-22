from recorder import Recorder

class HomePageHandler():
    def __init__(self, parentWindow):
        self.parentWindow = parentWindow
        self.speechHistory = parentWindow.ui.speechHistory
        self.removeSpeechHistoryItemBtn = parentWindow.ui.removeSpeechHistoryItemBtn
        self.clearSpeechHistoryBtn = parentWindow.ui.clearSpeechHistoryBtn

        # create recorder
        parentWindow.Recorder = Recorder(self.recording_callback, parentWindow.ui.startRecordingBtn, parentWindow.ui.stopRecordingBtn)
        # setup recording buttons
        parentWindow.ui.startRecordingBtn.clicked.connect(parentWindow.Recorder.startRecording)
        parentWindow.ui.stopRecordingBtn.clicked.connect(parentWindow.Recorder.stopRecording)
        # setup history list and buttons
        self.speechHistory.itemClicked.connect(self.select_list_item)
        self.removeSpeechHistoryItemBtn.clicked.connect(self.remove_list_item)
        self.clearSpeechHistoryBtn.clicked.connect(self.speechHistory.clear)

        # testing purposes
        parentWindow.ui.executeMockSpeechBtn.clicked.connect(self.onExecuteMockSpeech)

    def onExecuteMockSpeech(self):
        mock_command = self.parentWindow.ui.mockSpeechEdit.text().strip()
        if mock_command:
            self.recording_callback(mock_command)
            #self.parentWindow.CommandHandler.check_speech(mock_command)

    def select_list_item(self, item):
        self.speechHistory.setCurrentItem(item)
        self.removeSpeechHistoryItemBtn.setEnabled(True)

    def remove_list_item(self):
        row = self.speechHistory.currentRow()
        deleted_item = self.speechHistory.takeItem(row)
        del deleted_item
        if self.speechHistory.count() == 0:
            self.removeSpeechHistoryItemBtn.setEnabled(False)

    def recording_callback(self, speech):
        self.speechHistory.addItem(speech)
        self.parentWindow.CommandHandler.check_speech(speech)
