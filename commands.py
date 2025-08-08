import os, webbrowser, subprocess, winreg


def commands(command):

    command = command.lower()

    if "exit" in command:
        os._exit(0)

    if 'steam' in command:
        ## logic can be applied to open any .exe
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam")
        path, _ = winreg.QueryValueEx(key, "SteamExe")
        winreg.CloseKey(key)
        subprocess.Popen([path])

    if 'call of duty' in command:
        os.startfile(r"put_path_here")

    if 'open browser' in command:
        ##web-browser open to url
        webbrowser.open_new('www.google.com')

    else:
        print("No command found")
