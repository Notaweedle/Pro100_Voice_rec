import sys, os, webbrowser, time
#from command_processes import audio as a, system_functions as sf

class CommandExecutor():
    def __init__(self):
        # setup necessary stuff
        self.python_exe = sys.executable
        self.pythonw_exe = os.path.join(os.path.dirname(sys.executable), "pythonw.exe")
        self.device_type = sys.platform
        #self.script_path = os.path.join(os.path.dirname(__file__), "command_processes", "add_command.py") # redoing this
        #self.listener_path = os.path.join(os.path.dirname(__file__), "listener.pyw") # old

    def execute_command(self, command):
        if command['category'].lower() == "default":
            return self.execute_default_command(command)
        else:
            match command['type']:
                case 'Program':
                    return self.execute_program_command(command['target'])
                case 'Browser':
                    return self.execute_browser_command(command['target'])
                case 'Script':
                    return self.execute_script_command(command['target'])
        # DON'T FORGET TO ADD COMMAND LOGGING

    def execute_program_command(self, program_path):
        print(program_path)

    def execute_browser_command(self, url):
        if not url.startswith("http://") or not url.startswith("https://"):
            url = "https://" + url
        webbrowser.open(url)
        return (True, "")

    def execute_script_command(self, script_path):
        print(script_path)

    # DEFAULT COMMANDS BELOW HERE

    def execute_default_command(self, command):
        name = command['name'].lower()
        target = command['target']

        if 'exit' in name:
            os._exit(0)

        elif 'steam' in name:
            if self.device_type == 'win32':
                time.sleep(.2)
                if os.path.exists(target):
                    return (False, 'Steam not installed')
                else:
                    os.startfile(target)

            elif self.device_type == 'linux':
                import shutil
                app_path = shutil.which('steam')
                # report / warning
                if app_path is None:
                    return (False, 'Steam not installed')

        elif 'browser' in name:
            time.sleep(.2)
            webbrowser.open_new('google.com')

        # return true if a command reaches this far
        return (True, "")



