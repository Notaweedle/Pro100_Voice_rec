# THIS IS WHERE ALL COMMAND EXECUTION, LOADING, SAVING, ETC. WILL BE DONE FROM!!! ( i think )
import os
import json

from commands import CommandExecutor

class CommandHandler():
    # command structure for json follows the current custom commands table headers
    # [{name: str, speech: str, enabled: str, category: str, type: str, target: str}]

    # name is simply a short but descriptive user-defined name for the command (required, not blank, WILL BE CHANGED TO BE UNIQUE or may just add ids idk)
    # speech is what the user will have to say for a command to be executed (required, not blank)
    # enabled is if the command will be executed when the speech is detected (required)
    # category is a way for the user to define categories for their custom commands for their own sorting needs (not required, can't be "default"/"Default")
    # type is the chosen type of command, only three implemented are Program (opens a program), Browser (opens a website in default browser) and Script (runs main() off a user's script) (required
    # target is the target file / website (SHOULD be required, but checking is not implemented for this yet since it'd be a bit more complicated)

    def __init__(self, parentWindow):
        # setup variables
        self.CommandExecutor = CommandExecutor()
        self.commands_dict = []
        self.command_speech_phrases = []
        self.data_dir = os.getcwd() + "\\data"
        self.commands_file = self.data_dir + "\\commands.json"

        # load commands from file and then load those into table
        self.load_commands()
        parentWindow.loadCustomCommandsTable(parentWindow.ui.customCommandsTable, self.commands_dict)

    def check_speech(self, speech):
        print(speech)
        # current idea to work on:
        # check_speech(speech) decides if speech matches a command
        # if so, it passes the command name to the other module
        # execute_command(command_info) decides type is Program -> custom_program_command(target) opens target program from specified command
        for phrase in self.command_speech_phrases:
            if phrase in speech:
                for command in self.commands_dict:
                    if command['speech'] == phrase:
                        print("Attempted to execute command: " + str(command))
                        success = self.CommandExecutor.execute_command(command)
                        print(success)

    def load_commands(self):
        if os.path.exists(self.commands_file):
            try:
                with open(self.commands_file, 'r') as f:
                    commands_json = json.load(f)
                    f.close()
                self.parse_commands_data(commands_json)
            except json.JSONDecodeError as e:
                print("Json could not be decoded", e) # have a proper error message window pop up in this case
            except Exception as e:
                print("unknown error!!!!", e) # just catching in case theres other possible errors else i missed
        else:
            # create missing folder (if it doesn't exist)
            if not os.path.exists(self.data_dir):
                os.makedirs(self.data_dir)
            # and create json file with empty array
            with open(self.commands_file, "w") as f:
                f.write("[]")
                f.close()

    def parse_commands_data(self, commands_json):
        # update full dict
        self.commands_dict = commands_json
        # and then speech phrases for an easy index with check_speech
        self.command_speech_phrases = []
        for command in commands_json:
            if command['enabled'] == "True":
                self.command_speech_phrases.append(command['speech'])

    def save_commands(self, table):
        # this is called whenever a row in the custom commands table is created, edited, or deleted as to keep the file in sync
        commands_dict = []

        # just double checking column count in case if i change something down the line
        if table.columnCount() != 6:
            raise ValueError("Table's column count does not match static amount. Expected 6, got " + str(table.columnCount()))

        row_count = table.rowCount()
        for row in range(row_count):
            row_dict = {}
            row_dict["name"] = table.item(row, 0).text()
            row_dict["speech"] = table.item(row, 1).text()
            row_dict["enabled"] = table.item(row, 2).text()
            row_dict["category"] = table.item(row, 3).text()
            row_dict["type"] = table.item(row, 4).text()
            row_dict["target"] = table.item(row, 5).text()
            commands_dict.append(row_dict)

        # theoretically, this should always exist as the load_commands func will always be called first and that creates the file
        if os.path.exists(self.commands_file):
            with open(self.commands_file, "w") as f:
                json.dump(commands_dict, f, indent=2)
                f.close()

        # this keeps the handler phrases in sync with the file
        self.parse_commands_data(commands_dict)
