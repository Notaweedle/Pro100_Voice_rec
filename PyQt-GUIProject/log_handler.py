class LogHandler():
    def __init__(self, logPage, parentWindow):
        self.parentWindow = parentWindow
        self.logPage = logPage

    # the biggest change is only loading the commands on startup
    # but when the settings are being saved after startup
    # the new directory should be used to save instead
    def load_data_dir(self, save_dir):
        self.data_dir = save_dir
        self.log_file = self.data_dir + "\\log.json"
        # load commands from file to this class, then from this class to table
        #self.load_log()
        #self.logPage.loadCustomCommandsTable(TABLE NAME)

    def change_data_dir(self, new_dir):
        self.data_dir = new_dir
        self.log_file = self.data_dir + "\\log.json"
        #print(self.commands_file)
        # save current table to new dir
        #self.save_log(TABLE NAME)
