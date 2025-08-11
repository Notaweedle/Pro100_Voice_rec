import os, webbrowser, time, json, chat
from dotenv import load_dotenv
from command_processes import audio as a

def commands(command):

    command = command.lower()

    if "exit" in command:
        os._exit(0)

    elif 'steam' in command:
        a.say("Opening steam")
        time.sleep(.2)
        os.startfile(r"C:\Program Files (x86)\Steam\Steam.exe")


    elif 'open browser' in command:
        time.sleep(.2)
        webbrowser.open_new('www.google.com')

    elif 'turn down volume' in command:
        time.sleep(.2)
        a.turn_down_volume()

    elif 'turn up volume' in command:
        time.sleep(.2)
        a.turn_up_volume()

    elif 'add command' in command:
        import  subprocess
        load_dotenv(dotenv_path=r'.env')

        #we can possibly have an initialization script to create an env with paths to everything.
        python_exe = os.getenv('PYTHON_EXE')
        script_path = os.getenv('SCRIPT_PATH')

        subprocess.Popen([python_exe, script_path])



    else:
        print("No command found")

