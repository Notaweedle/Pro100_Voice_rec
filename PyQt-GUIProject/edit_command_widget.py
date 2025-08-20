# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets

from ui_edit_command import Ui_EditCommandWidget

class EditCommandWidget(QtWidgets.QWidget):
    def __init__(self, commandItems, table, parent=None):
        # defaults for pyside
        super().__init__()
        self.ui = Ui_EditCommandWidget()
        self.ui.setupUi(self)
        # set global for command items (probably unnecessary)
        self.commandItems = commandItems
        self.table = table

        # connect gui slots
        self.ui.cancelBtn.clicked.connect(self.onCancel)
        self.ui.deleteBtn.clicked.connect(self.onDelete)
        self.ui.saveBtn.clicked.connect(self.onSave)

        # whatever else i need to do below here
        self.loadValues()

    def loadValues(self):
        # set basic values
        self.ui.nameEdit.setText(self.commandItems['name'])
        self.ui.speechEdit.setText(self.commandItems['speech'])

        # check if enabled or not (since string is stored by default)
        if self.commandItems['enabled'] == "True":
            self.ui.enabledCheck.setChecked(True)
        else:
            self.ui.enabledCheck.setChecked(False)

        # figure these two out
        #self.ui.categoryCombo
        #self.ui.typeCombo

        # disable certain fields / buttons if its a default command
        if self.commandItems['category'] == "Default":
            self.ui.nameEdit.setEnabled(False)
            self.ui.categoryCombo.setEnabled(False)
            self.ui.typeCombo.setEnabled(False)
            self.ui.deleteBtn.setEnabled(False)
        else:
            # maybe need an else?
            pass

        # NEED a better way of detection later
        # (when changing type, this should become active)
        # but for now this works
        cmd_target = self.commandItems['target']
        self.ui.targetEdit.setText(cmd_target)
        if cmd_target != "N/A":
            self.ui.targetEdit.setEnabled(True)
        else:
            self.ui.targetEdit.setEnabled(False)

    def onCancel(self):
        # TODO maybe confirm if unsaved changes first?
        self.destroy()

    def onDelete(self):
        #confirm deletion first before proceeding
        doDelete = True #TODO update with new dialog to confirm
        if doDelete:
            row = self.table.currentRow()
            self.table.removeRow(row)
            self.destroy()
        #otherwise do nothing else

    def readNewValues(self):
        #TODO stuff for other fields
        self.commandItems['name'] = self.ui.nameEdit.text()
        self.commandItems['speech'] = self.ui.speechEdit.text()
        if self.ui.enabledCheck.isChecked():
            self.commandItems['enabled'] = "True"
        else:
            self.commandItems['enabled'] = "False"
        self.commandItems['target'] = self.ui.targetEdit.text()

    # this should be finished for good
    # (unless changes are made to the commandItems dict thing itself)
    def onSave(self):
        self.readNewValues()
        row = self.table.currentRow()
        self.table.item(row, 0).setText(self.commandItems['date'])
        self.table.item(row, 1).setText(self.commandItems['name'])
        self.table.item(row, 2).setText(self.commandItems['speech'])
        self.table.item(row, 3).setText(self.commandItems['enabled'])
        self.table.item(row, 4).setText(self.commandItems['category'])
        self.table.item(row, 5).setText(self.commandItems['type'])
        self.table.item(row, 6).setText(self.commandItems['target'])
        #finally destroy the window to free resources and let the user proceed with the main application
        self.destroy()
