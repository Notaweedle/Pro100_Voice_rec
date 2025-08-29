from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import Qt

from log_handler import LogHandler

class LogPageHandler():
    def __init__(self, parentWindow):
        self.ui = parentWindow.ui
        self.commandHistoryTable =  parentWindow.ui.executedCommandTable

        self.LogHandler = LogHandler(self, parentWindow)

        self.setupHistoryTable(self.commandHistoryTable)
        parentWindow.ui.addItemHistoryBtn.clicked.connect(self.onAddItemToHistory)
        parentWindow.ui.deleteRowHistoryBtn.clicked.connect(self.onRemoveHistoryRow)

    # UNIVERSAL TABLE CELL CREATOR
    # since they all need to be centered (and maybe more to add)
    def createTableWidgetItem(self, table, data, row, column):
        item = QTableWidgetItem(data)
        item.setTextAlignment(Qt.AlignCenter)
        table.setItem(row, column, item)

    # EXECUTED FOR TESTING PURPOSES ON LAUNCH
    # SETS UP THE TABLE HISTORY WITH MOCK DATA
    def setupHistoryTable(self, table):
        table.setColumnCount(5)
        table.setRowCount(0)
        # add table headers
        table.setHorizontalHeaderLabels(["Time", "Date", "Command Name", "Speech", "Successful", "Error Reason", "Category", "Type", "Target"])
        #test commands
        testHistory = [
            ["3:30 PM", "8/18/2025", "Fake Command", "open burger", "False", "File Not Found", "Custom"],
            ["3:25 PM", "8/18/2025", "Volume Up", "volume up by 5", "True", "", "Utility", "Default"],
            ["3:23 PM", "8/18/2025", "Browser", "open browser", "True", "", "Default"],
            ["9:00 PM", "8/17/2025", "Volume Down", "volume down by 5", "True", "", "Default"]
        ]
        #for i, (time, date, command, speech, type) in enumerate(testHistory):
        #    rowIndex = table.rowCount()
        #    table.setRowCount(rowIndex+1)
        #    # create base widget item for each and put on table
        #    self.createTableWidgetItem(table, time, rowIndex, 0)
        #    self.createTableWidgetItem(table, date, rowIndex, 1)
        #    self.createTableWidgetItem(table, command, rowIndex, 2)
        #    self.createTableWidgetItem(table, speech, rowIndex, 3)
        #    self.createTableWidgetItem(table, type, rowIndex, 4)

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
        self.addItemToCommandHistoryTable(self.commandHistoryTable, time, date, command, speech, type)

    def onRemoveHistoryRow(self):
        table = self.commandHistoryTable
        currentItem = table.currentItem()
        row = table.row(currentItem)
        table.removeRow(row)
