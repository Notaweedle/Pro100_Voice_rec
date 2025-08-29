from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import Qt
from datetime import datetime

from log_handler import LogHandler

class LogPageHandler():
    def __init__(self, parentWindow):
        self.ui = parentWindow.ui
        self.table =  parentWindow.ui.executedCommandTable

        self.LogHandler = LogHandler(self, parentWindow)

        #setup table with dummy info
        self.setupHistoryTable()
        parentWindow.ui.deleteRowHistoryBtn.clicked.connect(self.onRemoveHistoryRow)

    # UNIVERSAL TABLE CELL CREATOR
    # since they all need to be centered (and maybe more to add)
    def createTableWidgetItem(self, table, data, row, column):
        item = QTableWidgetItem(data)
        item.setTextAlignment(Qt.AlignCenter)
        table.setItem(row, column, item)

    def loadLogTable(self, log_json):
        for row_dict in log_json:
            self.createLogRow(row_dict)

    def createLogRow(self, commandInfo):
        table = self.table
        rowIndex = table.rowCount()
        table.setRowCount(rowIndex+1)
        # all the dif keys within the commandinfo
        self.createTableWidgetItem(table, commandInfo['time'], rowIndex, 0)
        self.createTableWidgetItem(table, commandInfo['date'], rowIndex, 1)
        self.createTableWidgetItem(table, commandInfo['name'], rowIndex, 2)
        self.createTableWidgetItem(table, commandInfo['speech'], rowIndex, 3)
        self.createTableWidgetItem(table, commandInfo['success'], rowIndex, 4)
        self.createTableWidgetItem(table, commandInfo['error_reason'], rowIndex, 5)
        self.createTableWidgetItem(table, commandInfo['category'], rowIndex, 6)
        self.createTableWidgetItem(table, commandInfo['type'], rowIndex, 7)
        self.createTableWidgetItem(table, commandInfo['target'], rowIndex, 8)

    def logCommand(self, commandInfo):
        # get date and time
        now = datetime.now()
        formattedDate = now.strftime("%m/%d/%Y")
        formattedTime = now.strftime("%I:%M:%S %p")
        commandInfo['time'] = formattedTime
        commandInfo['date'] = formattedDate
        self.createLogRow(commandInfo)
        # update log
        self.LogHandler.save_log()

    # EXECUTED FOR TESTING PURPOSES ON LAUNCH
    # SETS UP THE TABLE HISTORY WITH MOCK DATA
    def setupHistoryTable(self):
        table = self.table
        table.setColumnCount(9)
        table.setRowCount(0)
        # add table headers
        table.setHorizontalHeaderLabels(["Time", "Date", "Command Name", "Speech", "Success", "Error Reason", "Category", "Type", "Target"])

    def onRemoveHistoryRow(self):
        table = self.table
        currentItem = table.currentItem()
        row = table.row(currentItem)
        table.removeRow(row)
        # update log
        self.LogHandler.save_log()
