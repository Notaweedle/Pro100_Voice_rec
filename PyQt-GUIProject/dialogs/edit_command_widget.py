# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets

from dialogs.ui_edit_command import Ui_EditCommandWidget
from dialogs.confirm_dialog import ConfirmDialog

class EditCommandWidget(QtWidgets.QWidget):
    def __init__(self, commandItems, table, CommandHandler, parent=None):
        # defaults for pyside
        super().__init__()
        self.ui = Ui_EditCommandWidget()
        self.ui.setupUi(self)
        # set global for command items (probably unnecessary)
        self.commandItems = commandItems
        self.table = table
        self.CommandHandler = CommandHandler

        # connect gui slots
        self.ui.cancelBtn.clicked.connect(self.onCancel)
        self.ui.deleteBtn.clicked.connect(self.onDelete)
        self.ui.saveBtn.clicked.connect(self.onSave)

        # whatever else i need to do below here
        self.loadValues()

    def loadValues(self):
        # sets basic values
        self.ui.nameEdit.setText(self.commandItems['name'])
        self.ui.speechEdit.setText(self.commandItems['speech'])

        # checks if enabled or not (since a string is stored by default)
        if self.commandItems['enabled'] == "True":
            self.ui.enabledCheck.setChecked(True)
        else:
            self.ui.enabledCheck.setChecked(False)

        # disables certain fields / buttons if its a default command
        if self.commandItems['category'] == "Default":
            self.ui.nameEdit.setEnabled(False)
            self.ui.categoryEdit.setEnabled(False)
            self.ui.typeCombo.setEnabled(False)
            self.ui.deleteBtn.setEnabled(False)
        self.ui.categoryEdit.setText(self.commandItems['category'])

        # AVAILABLE TYPES
        # - Program
        # - Browser
        # - Script
        # insert non-user category such as "Utility" into combo box and set to it
        if self.ui.typeCombo.findText(self.commandItems['type']) == -1 and self.commandItems['category'] == "Default":
                self.ui.typeCombo.insertItem(0, self.commandItems['type'])
        self.ui.typeCombo.setCurrentText(self.commandItems['type'])

        # NEED a better way of detection later
        # (UPDATE: only necessary to add if more types are added that do not require the target field)
        # for now it will stay the same
        cmd_target = self.commandItems['target']
        self.ui.targetEdit.setText(cmd_target)
        if cmd_target != "N/A":
            self.ui.targetEdit.setEnabled(True)
        else:
            self.ui.targetEdit.setEnabled(False)

    def onCancel(self):
        # maybe confirm if unsaved changes first?
        # not sure if that's necessary or just annoying to the user tho
        # maybe only for command creation
        self.destroy()

    def onDelete(self):
        # confirm deletion first before proceeding
        self.confirmDialog = ConfirmDialog("Confirm Command Deletion", "Are you sure you want to delete this command?", "Cancel", "Yes")
        self.confirmDialog.setModal(True)
        self.confirmDialog.show()
        # and call once the dialog is finished
        self.confirmDialog.finished.connect(self.onConfirmDelete)

    def onConfirmDelete(self, result):
        if result == 1:
            row = self.table.currentRow()
            self.table.removeRow(row)
            # update command file since changes were made
            self.CommandHandler.save_commands(self.table)
            # delete window to free up resources
            self.destroy()

    def readNewValues(self):
        # name and speech CANNOT be blank strings
        name = self.ui.nameEdit.text().strip()
        speech = self.ui.speechEdit.text().strip()
        if name:
            self.commandItems['name'] = name
        if speech:
            self.commandItems['speech'] = speech.lower()

        # stored as a string
        if self.ui.enabledCheck.isChecked():
            self.commandItems['enabled'] = "True"
        else:
            self.commandItems['enabled'] = "False"

        # don't update category if the line contains "Default"/"default"
        # prevents user from making a new default command, otherwise it'd be impossible to edit / delete
        category = self.ui.categoryEdit.text().strip()
        if category.lower() != "default":
            self.commandItems['category'] = category

        # target might need to be validated for program / script commands, but otherwise these two are fine
        self.commandItems['type'] = self.ui.typeCombo.currentText()
        self.commandItems['target'] = self.ui.targetEdit.text()

    # this should be finished for good
    # (unless changes are made to the commandItems dict thing itself)
    def onSave(self):
        # set all the row items to the new values
        self.readNewValues()
        row = self.table.currentRow()
        self.table.item(row, 0).setText(self.commandItems['name'])
        self.table.item(row, 1).setText(self.commandItems['speech'])
        self.table.item(row, 2).setText(self.commandItems['enabled'])
        self.table.item(row, 3).setText(self.commandItems['category'])
        self.table.item(row, 4).setText(self.commandItems['type'])
        self.table.item(row, 5).setText(self.commandItems['target'])
        # update command file since changes were made
        self.CommandHandler.save_commands(self.table)
        #finally destroy the window to free resources and let the user proceed with the main application
        self.destroy()

