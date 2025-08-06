import os

import pyaudio
import speech_recognition as sr
import subprocess as sp
r = sr.Recognizer();
r.energy_threshold = 5000
r.pause_threshold = 0.8
inputString = "";

import winreg

key_path = r"Software\Valve\Steam"

try:

    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)

    value_name = "SteamPath"
    value, regtype = winreg.QueryValueEx(registry_key, value_name)
    print(f"{value_name} = {value}")  # Value = Path

    winreg.CloseKey(registry_key)

except FileNotFoundError:
    print("Registry key or value not found, you dumbass.")
except Exception as e:
    print(f"Error: {e}")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name));



with sr.Microphone() as source:
     print("Say something!")
     audio = r.listen(source)
try:

    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    inputString = r.recognize_sphinx(audio)
    steam_exe = os.path.join(value, "steam.exe")
    if "stop" in inputString.lower():
        sp.Popen([steam_exe])

except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
