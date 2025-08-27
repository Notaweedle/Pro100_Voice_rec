# external libraries
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QSystemTrayIcon, QMenu
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QAction


# auto generated stuff
from ui_form import Ui_Widget
from calibration_widget import CalibrationWidget
from edit_command_widget import EditCommandWidget
from create_command_widget import CreateCommandWidget

# our modules
from recorder import Recorder
from command_handler import CommandHandler

from home_page import HomePageHandler
from settings_page import SettingsPageHandler

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # home page setup
        self.HomeHandler = HomePageHandler(self)

        # handles the loading and saving of all commands
        self.CommandHandler = CommandHandler(self)

        # command history table setup
        self.setupHistoryTable(self.ui.executedCommandTable)
        self.ui.addItemHistoryBtn.clicked.connect(self.onAddItemToHistory)
        self.ui.deleteRowHistoryBtn.clicked.connect(self.onRemoveHistoryRow)

        # custom command table setup
        #self.setupCustomCommandsTable(self.ui.customCommandsTable) #no longer necessary, data is loaded on start wth command handler
        self.ui.customCommandsTable.itemClicked.connect(self.onSelectCustomCommand)
        self.ui.createCustomRowBtn.clicked.connect(self.onCreateCommand)
        self.ui.editCustomRowBtn.clicked.connect(self.onEditCustomRow)

        # settings page setup
        self.ui.openCalibrationBtn.clicked.connect(self.showCalibration) # needs to be moved into settings handler
        self.SettingsHandler = SettingsPageHandler(self)

    # UNIVERSAL TABLE CELL CREATOR
    # since they all need to be centered (and maybe more to add)
    def createTableWidgetItem(self, table, data, row, column):
        item = QTableWidgetItem(data)
        item.setTextAlignment(Qt.AlignCenter)
        table.setItem(row, column, item)

    # CREATES A ROW IN CUSTOM COMMANDS TABLE GIVEN AN ARRAY OF 6 VALUES
    def createCustomTableRow(self, commandItems):
        table = self.ui.customCommandsTable
        if len(commandItems) == 6:
            table.setRowCount(table.rowCount()+1)
            for i in range(len(commandItems)):
                self.createTableWidgetItem(table, commandItems[i], table.rowCount()-1, i)

    # LOAD DATA IN CUSTOM COMMANDS TABLE
    def loadCustomCommandsTable(self, table, commands):
        table.setColumnCount(6)
        table.setRowCount(len(commands))
        table.setHorizontalHeaderLabels(["Name", "Speech", "Enabled", "Category", "Type", "Target"])
        # creating cells for each key,value pair with row and column tracking
        curRow = 0
        for command in commands:
            curColumn = 0
            for key in command:
                value = command[key]
                self.createTableWidgetItem(table, value, curRow, curColumn)
                curColumn += 1
            curRow += 1

    # ENABLES EDIT BUTTON WHEN A ROW IS SELECTED
    def onSelectCustomCommand(self):
        self.ui.editCustomRowBtn.setEnabled(True)

    # EDIT WINDOW FOR EDITING A CUSTOM COMMAND
    def onEditCustomRow(self):
        table = self.ui.customCommandsTable
        row = table.currentRow()
        # get all items from current row
        commandItems = {}
        commandItems['name'] = table.item(row, 0).text()
        commandItems['speech'] = table.item(row, 1).text()
        commandItems['enabled'] = table.item(row, 2).text()
        commandItems['category'] = table.item(row, 3).text()
        commandItems['type'] = table.item(row, 4).text()
        commandItems['target'] = table.item(row, 5).text()
        # pass params to editcommand window
        self.EditCommandWidget = EditCommandWidget(commandItems, table, self.CommandHandler)
        self.EditCommandWidget.show()

    # CREATE WINDOW FOR CREATING A CUSTOM COMMAND
    def onCreateCommand(self):
        self.CreateCommandWidget = CreateCommandWidget(self)
        self.CreateCommandWidget.show()

    # SAVING A NEWLY CREATED CUSTOM COMMAND
    def onSaveNewCommand(self):
        # update values, take the new values, and create a row
        # then free up resources
        self.CreateCommandWidget.updateValues()
        commandItems = self.CreateCommandWidget.commandItems
        self.createCustomTableRow(commandItems)
        self.CreateCommandWidget.destroy()

        #TODO this is one place where the list of dicts needs to be created
        # and hten saved to file using command_handler
        self.CommandHandler.save_commands(self.ui.customCommandsTable)

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

def closeEvent(event):
        event.ignore()
        widget.hide()
        tray.showMessage(
            "Rat",
            "Application minimized to tray",
            QSystemTrayIcon.Information,
            2000
        )

def on_tray_activated(click):
    # Different types of clicks are possible
    if click == QSystemTrayIcon.Trigger:  # single left click
        widget.showNormal()   # restore if minimized
        widget.activateWindow()  # bring to front

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()

    widget.setWindowIcon(QIcon(r".\PyQt-GUIProject\Assets\RatBalling.png"))
    tray = QSystemTrayIcon(QIcon(r".\PyQt-GUIProject\Assets\RatBalling.png"), parent=app)


    tray_menu = QMenu()
    show_action = QAction("Show")
    quit_action = QAction("Quit")
    tray_menu.addAction(show_action)
    tray_menu.addAction(quit_action)
    tray.setContextMenu(tray_menu)
    tray.setVisible(True)

    tray.activated.connect(on_tray_activated)

    show_action.triggered.connect(widget.show)
    quit_action.triggered.connect(app.quit)


    widget.closeEvent = closeEvent

    widget.show()
    sys.exit(app.exec())
