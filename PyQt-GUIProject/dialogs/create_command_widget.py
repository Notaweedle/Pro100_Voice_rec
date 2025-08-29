# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets

from dialogs.ui_create_command import Ui_CreateCommandWidget
from dialogs.confirm_dialog import ConfirmDialog

class CreateCommandWidget(QtWidgets.QWidget):
    def __init__(self, returnWindow, parent=None):
        super().__init__(parent)
        self.ui = Ui_CreateCommandWidget()
        self.ui.setupUi(self)

        # hook up buttons
        self.ui.createBtn.clicked.connect(returnWindow.onSaveNewCommand)
        self.ui.cancelBtn.clicked.connect(self.onCancel)

        # update create button state when name, speech, or category box is changed
        self.ui.nameEdit.textChanged.connect(self.updateCreateBtn)
        self.ui.speechEdit.textChanged.connect(self.updateCreateBtn)
        self.ui.categoryEdit.textChanged.connect(self.updateCreateBtn)

    def checkValues(self):
        self.updateValues()
        # all restrictions
        # name cant be empty
        # speech cant be empty
        # category cannot be "default" or "Default"
        name = self.commandItems[0]
        speech = self.commandItems[1]
        category = self.commandItems[3]

        if name and speech and category.lower() != "default":
            return True
        else:
            return False

    def updateCreateBtn(self):
        if self.checkValues():
            self.ui.createBtn.setEnabled(True)
        else:
            self.ui.createBtn.setEnabled(False)

    def updateValues(self):
        name = self.ui.nameEdit.text().strip()
        speech = self.ui.speechEdit.text().strip().lower()
        enabled = ""
        if self.ui.enabledCheck.isChecked():
            enabled = "True"
        else:
            enabled = "False"
        category = self.ui.categoryEdit.text().strip()
        type = self.ui.typeCombo.currentText()
        target = self.ui.targetEdit.text().strip()

        self.commandItems = [name,speech,enabled,category,type,target]


    def onCancel(self):
        self.confirmCancelDialog = ConfirmDialog("Confirm Cancellation", "Are you sure you want to cancel creating this command?", "No", "Yes")
        self.confirmCancelDialog.setModal(True)
        self.confirmCancelDialog.show()

        self.confirmCancelDialog.finished.connect(self.onCancelConfirm)

    def onCancelConfirm(self, result):
        if result == 1:
            self.destroy()
