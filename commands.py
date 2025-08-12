import os, webbrowser, time, json
from dotenv import load_dotenv
from command_processes import audio as a, system_functions as sf

def commands(command):

    command = command.lower()

    if "exit" in command:
        os._exit(0)

    elif 'steam' in command:
         
        load_dotenv(dotenv_path=r'.env')
        if os.getenv('DEVICE_TYPE') == 'win32':
            time.sleep(.2)
            os.startfile(r"C:\Program Files (x86)\Steam\Steam.exe")
        elif os.getenv('DEVICE_TYPE') == 'linux':
            import shutil
            app_path = shutil.which('steam')
            if app_path is None:
                print('Steam NOT installed')
            else:
                os.startfile(app_path)

    
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

        python_exe = os.getenv('PYTHON_EXE')
        script_path = os.getenv('SCRIPT_PATH')
        subprocess.Popen([python_exe, script_path])
    
    elif 'mute volume' in command or 'mute audio' in command:
    
        a.mute()
    
    elif 'max volume' in command or 'full volume' in command:
        a.max_volume()

    elif 'min volume' in command or 'minimum volume' in command:
        a.min_volume()
    
    elif 'unmute volume' in command or 'unmute audio' in command:
        a.unmute()

    elif 'mute mic' in command or 'mute microphone' in command:
        a.mute_mic()
    
    elif 'unmute mic' in command or 'mute microphone' in command:
        a.unmute_mic()

    elif 'minimum brightness' in command:
        sf.min_brightness()

    elif 'max brightness' in command or 'maximum brightness' in command:
        sf.max_brightness()

    elif 'decrease brightness' in command:
        sf.decrease_brightness()

    elif 'increase brightness' in command:
        sf.increase_brightness


    else:
        print("No command found")

