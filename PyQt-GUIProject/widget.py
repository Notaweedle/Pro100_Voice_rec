# external libraries
import sys, os
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QSystemTrayIcon, QMenu
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QAction, QFontDatabase, QFont
import stylesheetsetter

# dialogs
from ui_form import Ui_Widget
from dialogs.edit_command_widget import EditCommandWidget
from dialogs.create_command_widget import CreateCommandWidget
# other
from command_handler import CommandHandler
# page modules
from home_page import HomePageHandler
from log_page import LogPageHandler
from settings_page import SettingsPageHandler

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # home page setup
        self.HomeHandler = HomePageHandler(self)

        #logging page
        self.LogHandler = LogPageHandler(self)

        # handles the loading and saving of all commands
        self.CommandHandler = CommandHandler(self)

        # command history table setup
        self.setupHistoryTable(self.ui.executedCommandTable)
        #self.ui.addItemHistoryBtn.clicked.connect(self.onAddItemToHistory)
        self.ui.deleteRowHistoryBtn.clicked.connect(self.onRemoveHistoryRow)

        # custom command table setup
        #self.setupCustomCommandsTable(self.ui.customCommandsTable) #no longer necessary, data is loaded on start wth command handler
        self.ui.customCommandsTable.itemClicked.connect(self.onSelectCustomCommand)
        self.ui.createCustomRowBtn.clicked.connect(self.onCreateCommand)
        self.ui.editCustomRowBtn.clicked.connect(self.onEditCustomRow)
        # all of this should be moved into its own page handler

        # settings page setup
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


# ======
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
    if click == QSystemTrayIcon.Trigger:
        widget.showNormal()
        widget.activateWindow()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = Widget()

    widget.setWindowIcon(QIcon(r".\PyQt-GUIProject\Assets\RatBalling.png"))
    app.setWindowIcon(QIcon(r".\PyQt-GUIProject\Assets\RatBalling.png"))

    tray = QSystemTrayIcon(QIcon(r".\PyQt-GUIProject\Assets\RatBalling.png"), parent=app)
    app.setStyleSheet(stylesheetsetter.set_theme())

   
    font_id = QFontDatabase.addApplicationFont(r"PyQt-GUIProject\Fonts\SF-Compact-Rounded-Medium.otf")
    family = QFontDatabase.applicationFontFamilies(font_id)
    font = QFont(family, 11, 300,False)
    font.setStyleStrategy(QFont.PreferAntialias)
    font.setHintingPreference(QFont.PreferNoHinting)

    widget.setFont(font)
    app.setFont(font)
    
    for child in widget.findChildren(QWidget):
        child.setFont(font)

    



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
