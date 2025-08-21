# THIS IS WHERE ALL COMMAND EXECUTION, LOADING, SAVING, ETC. WILL BE DONE FROM!!! ( i think )

class CommandHandler():
    def __init__(self):
        # my idea is to load all saved commands from a json file (if it exist) on initialization
        # save to self.commandKeywords as a list or dict of sorts
        #self.load_commands()

        # this CommandHandler class would be initalized within widget.py in its own __init__
        pass

    def check_speech(self):
        # in here, speech would be passed in from widget.py, whenever the callback from recorder class calls it
        # then it would be checked amongst the currently loaded commandKeywords to see if any whole words match

        # if so, that command will be executed from whatever module it may exist in
        # (this would probably be best with a similar, separate module)

        # maybe only the name and speech variables are stored in here
        # while the full command details are stored in a different module
        # check_speech(speech) decides if speech matches a command
        # if so, it passes the command name to the other module where the rest are stored (illustrated below)
        # execute_command(commandName) decides type -> custom_program_command(target) opens target program from specified command
        pass

    def load_commands(self):
        # in here, the commands would be loaded to self.commandKeywords
        # and then be appended to the custom commands table, so i guess the table would need to be passed into the __init__

        # my idea for the command structure for json follows the current custom commands table headers
        # [{name: str, speech: str, enabled: bool, category: str, type: str, target: str}]

        # name is simply a short but descriptive user-defined name for the command (required, not blank, WILL BE CHANGED TO BE UNIQUE or may just add ids idk)
        # speech is what the user will have to say for a command to be executed (required, not blank)
        # enabled is if the command will be executed when the speech is detected (required)
        # category is a way for the user to define categories for their custom commands for their own sorting needs (not required, can't be "default"/"Default")
        # type is the chosen type of command, only three implemented are Program (opens a program), Browser (opens a website in default browser) and Script (runs main() off a user's script) (required
        # target is the target file / website (SHOULD be required, but checking is not implemented for this yet since it'd be a bit more complicated)
        pass

    def save_commands(self):
        # in here, the commands would be saved to the same file that they were loaded from
        # this would be called whenever a row in the custom commands table is created, edited, or deleted as to keep the file in sync

        # one thing is that commandKeywords has to be updated alongside this
        # just in case if the user updates the "speech" field on a specific command
        # or if they are creating / deleting a new command
        # so that this handler is in sync at all times
        pass
