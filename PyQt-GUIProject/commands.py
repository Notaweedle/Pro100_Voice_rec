import sys, os, webbrowser, time, subprocess
from command_processes import audio as a, system_functions as sf

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
                    return self.execute_program_command(command['target'], command['name'])
                case 'Browser':
                    return self.execute_browser_command(command['target'], command['name'])
                case 'Script':
                    return self.execute_script_command(command['target'],command['name'])
        # DON'T FORGET TO ADD COMMAND LOGGING

    def execute_program_command(self, program_path, name):
        if os.path.exists(program_path):
            a.speak(f"Opening {name}")
            os.startfile(program_path)
            return (True, "")
        else:
            return(False, f"Program path does not exist: {program_path}")

    def execute_browser_command(self, url, name):
        if not url.startswith("http://") or not url.startswith("https://"):
            url = "https://" + url
        a.speak(f'Opening {name}')
        webbrowser.open(url)
        return (True, "")

    def execute_script_command(self, script_path, name):
        if not os.path.isfile(script_path):
            return(False, f"Script path doesnt exsist: {script_path}")

        if not sys.executable or not os.path.isfile(sys.executable):
            print("Python interpreter not found")
            return(False, "Python interpreter not found")

        try:
            a.speak(f'Running {name}.py')
            result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
            print(result.stdout)
            return (True, "")
        except subprocess.CalledProcessError as e:
            print("could not run script, heres the error", e.stderr)
            return(False, f"An error occured: {e.stderr}")

    # DEFAULT COMMANDS BELOW HERE

    def execute_default_command(self, command):
        name = command['name'].lower()
        target = command['target']

        if name == 'exit':
            os._exit(0)

        elif name == 'steam':
            if self.device_type == 'win32':
                time.sleep(.2)
                if not os.path.exists(target):
                    return (False, f'Steam path not found: {target} (possibly not installed?)')
                else:
                    a.speak('opening steam')
                    os.startfile(target)

            elif self.device_type == 'linux':
                import shutil
                a.speak('opening steam')
                app_path = shutil.which('steam')
                # report / warning
                if app_path is None:
                    return (False, 'Steam not installed')

        elif name == 'browser':
           return self.execute_browser_command(target)

        elif name == 'volume down':
            a.speak('Turning down volume')
            time.sleep(.2)
            return a.turn_down_volume()

        elif name == 'volume up':
            a.speak('Turning up volume')
            time.sleep(.2)
            return a.turn_up_volume()

        elif name == 'mute volume':
            a.speak("Muted volume")
            return a.mute_speakers()

        elif name == 'max volume':
            a.speak('Maxed out the volume')
            return a.max_volume()

        elif name == 'min volume':
            return a.min_volume()

        elif name == 'unmute volume':
            a.speak('Unmuted volume')
            return a.unmute_speakers()

        elif name == 'mute microphone':
            a.speak('Muted mic')
            return a.mute_mic()

        elif name == 'min brightness':
            a.speak('Minimized Brightness')
            return sf.min_brightness()

        elif name == 'max brightness':
            a.speak('Maximized the Brightness')
            return sf.max_brightness()

        elif name == 'brightness down':
            a.speak('I have decreased the brightness')
            return sf.decrease_brightness()

        elif name == 'brightness up':
            a.speak('I have increased the brightness')
            return sf.increase_brightness()

        elif name == 'close active window':
            a.speak('I have closed the active window')
            return sf.kill_active_window()

        elif name == 'lock computer':
            a.speak('Locking your computer')
            return sf.lock_screen()

        elif name == 'restart computer':
            a.speak('Restarting')
            return sf.restart()

        elif name == 'shutdown computer':
            a.speak('Shutting down')
            return sf.shutdown()

        elif name == 'pause music':
            a.speak('Paused music')
            return a.pause_or_play()

        elif name == 'play music':
            a.speak("Playing music")
            return a.pause_or_play()

        elif name == 'next song':
            a.speak('Skipping to next song')
            return a.next_track()

        elif name == 'rewind song':
            a.speak("Rewinded song")
            return a.rewind_track()

        elif name == 'previous song':
            a.speak("Playing Previous song")
            return a.previous_track()


        # at this point, all implemented default commands should have been found and returned properly
        # if not, there is an implicit error and it should be returned as such
        return (False, "Default command not found!")

