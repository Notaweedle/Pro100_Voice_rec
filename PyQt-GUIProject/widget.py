# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PySide6.QtCore import Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
from calibration_widget import CalibrationWidget
from edit_command_widget import EditCommandWidget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # setup table on start
        self.setupHistoryTable(self.ui.executedCommandTable)
        # add item to history table button
        self.ui.addItemHistoryBtn.clicked.connect(self.onAddItemToHistory)
        # remove row from history table button
        self.ui.deleteRowHistoryBtn.clicked.connect(self.onRemoveHistoryRow)

        # setup custom command table on start
        self.setupCustomCommandsTable(self.ui.customCommandsTable)
        self.ui.customCommandsTable.itemClicked.connect(self.onSelectCustomCommand)
        # edit item in custom table (TEST)
        self.ui.editCustomRowBtn.clicked.connect(self.onEditCustomRow)

        # setup calibration open
        self.ui.openCalibrationBtn.clicked.connect(self.showCalibration)

        #testing stuff
        self.ui.listWidget.itemClicked.connect(self.selectItemInList)
        self.ui.clearHistoryBtn.clicked.connect(self.clearSpeechHistory)


    def createTableWidgetItem(self, table, data, row, column):
        item = QTableWidgetItem(data)
        item.setTextAlignment(Qt.AlignCenter)
        table.setItem(row, column, item)

    def setupCustomCommandsTable(self, table):
        table.setColumnCount(7)
        table.setRowCount(0)
        # add table headers
        table.setHorizontalHeaderLabels(["Date", "Name", "Speech", "Enabled", "Category", "Type", "Target"])
        #test commands
        testCommands = [
            ["8/18/2025", "Fake Command", "open burger.exe", "False", "Custom", "Program", "C:/Path/To/Burger.exe"],
            ["8/17/2025", "Volume Up", "volume up by 5", "True", "Default", "Utility", "N/A"],
            ["8/17/2025", "Volume Down", "volume down by 5", "True", "Default", "Utility", "N/A"],
            ["8/17/2025", "Browser", "open browser", "True", "Default", "Browser", "google.com"]
        ]
        for i, (date, name, speech, enabled, category, type, target) in enumerate(testCommands):
            rowIndex = table.rowCount()
            table.setRowCount(rowIndex+1)
            # create base widget item for each and put on table
            self.createTableWidgetItem(table, date, rowIndex, 0)
            self.createTableWidgetItem(table, name, rowIndex, 1)
            self.createTableWidgetItem(table, speech, rowIndex, 2)
            self.createTableWidgetItem(table, enabled, rowIndex, 3)
            self.createTableWidgetItem(table, category, rowIndex, 4)
            self.createTableWidgetItem(table, type, rowIndex, 5)
            self.createTableWidgetItem(table, target, rowIndex, 6)

    def onSelectCustomCommand(self):
        self.ui.editCustomRowBtn.setEnabled(True)

    def onEditCustomRow(self):
        table = self.ui.customCommandsTable
        row = table.currentRow()
        # get all items from current row
        commandItems = {}
        commandItems['date'] = table.item(row, 0).text()
        commandItems['name'] = table.item(row, 1).text()
        commandItems['speech'] = table.item(row, 2).text()
        commandItems['enabled'] = table.item(row, 3).text()
        commandItems['category'] = table.item(row, 4).text()
        commandItems['type'] = table.item(row, 5).text()
        commandItems['target'] = table.item(row, 6).text()

        # pass params to editcommand window
        self.EditCommandWidget = EditCommandWidget(commandItems, table)
        self.EditCommandWidget.show()

    # OPENING A NEW WINDOW FOR CALIBRATION
    def showCalibration(self):
        self.calibration = CalibrationWidget()
        self.calibration.show()

    # EXECUTED FOR TESTING PURPOSES ON LAUNCH
    # SETS UP THE TABLE HISTORY WITH MOCK DATA
    def setupHistoryTable(self, table):
        table.setColumnCount(5)
        table.setRowCount(0)
        # add table headers
        table.setHorizontalHeaderLabels(["Time", "Date", "Command", "Speech", "Type"])
        #test commands
        testHistory = [
            ["3:30 PM", "8/18/2025", "Fake Command", "open burger", "Custom"],
            ["3:25 PM", "8/18/2025", "Volume Up", "volume up by 5", "Default"],
            ["3:23 PM", "8/18/2025", "Browser", "open browser", "Default"],
            ["9:00 PM", "8/17/2025", "Volume Down", "volume down by 5", "Default"]
        ]
        for i, (time, date, command, speech, type) in enumerate(testHistory):
            rowIndex = table.rowCount()
            table.setRowCount(rowIndex+1)
            # create base widget item for each and put on table
            self.createTableWidgetItem(table, time, rowIndex, 0)
            self.createTableWidgetItem(table, date, rowIndex, 1)
            self.createTableWidgetItem(table, command, rowIndex, 2)
            self.createTableWidgetItem(table, speech, rowIndex, 3)
            self.createTableWidgetItem(table, type, rowIndex, 4)

    def onAddItemToHistory(self):
        # get all inputs
        time = self.ui.timeEdit.text()
        date = self.ui.dateEdit.text()
        command = self.ui.commandEdit.text()
        speech = self.ui.speechEdit.text()
        type = self.ui.typeEdit.text()
        # clear the inputs
        self.ui.timeEdit.clear()
        self.ui.dateEdit.clear()
        self.ui.commandEdit.clear()
        self.ui.speechEdit.clear()
        self.ui.typeEdit.clear()
        # add to table
        self.addItemToCommandHistoryTable(self.ui.executedCommandTable, time, date, command, speech, type)

    def onRemoveHistoryRow(self):
        table = self.ui.executedCommandTable
        currentItem = table.currentItem()
        row = table.row(currentItem)
        table.removeRow(row)

    def selectItemInList(self, item):
        self.ui.listWidget.setCurrentItem(item)


    def clearSpeechHistory(self):
        #currentItem = self.ui.listWidget.currentItem()
        #row = self.ui.listWidget.row(currentItem)
        #deletedItem = self.ui.listWidget.takeItem(row)
        #del deletedItem
        self.ui.listWidget.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
