# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets

from ui_confirm_dialog import Ui_ConfirmDialog

class ConfirmDialog(QtWidgets.QDialog):
    def __init__(self, title, mainText, cancelText="Cancel", confirmText="Confirm", parent=None):
        super().__init__(parent)
        self.ui = Ui_ConfirmDialog()
        self.ui.setupUi(self)

        if cancelText == None:
            self.ui.cancelBtn.setVisible(False)
            cancelText = "Cancel"
        # setup text params
        self.setupText(title, mainText, cancelText, confirmText)
        # connect buttons here!!
        self.ui.cancelBtn.clicked.connect(self.reject)
        self.ui.confirmBtn.clicked.connect(self.accept)

    def setupText(self, title, mainText, cancelText, confirmText):
        self.setWindowTitle(title)
        self.ui.dialogText.setText(mainText)
        self.ui.cancelBtn.setText(cancelText)
        self.ui.confirmBtn.setText(confirmText)
