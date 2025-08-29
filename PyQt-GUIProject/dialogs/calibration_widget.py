# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets

from dialogs.ui_calibration import Ui_CalibrationDialog

class CalibrationWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CalibrationDialog()
        self.ui.setupUi(self)





