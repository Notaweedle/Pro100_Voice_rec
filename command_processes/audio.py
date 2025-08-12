from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
import os

# These are for the speakers not the input, so output!!
def get_Speaker_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume

def turn_up_volume():
    if os.getenv('DEVICE_TYPE') == 'win32':
        volume = get_Speaker_volume()
        currentVolume = volume.GetMasterVolumeLevel()

        try:
            volume.SetMasterVolumeLevel((currentVolume + 2), None)
        except:
            volume.SetMasterVolumeLevelScalar(1, None)
    elif os.getenv('DEVICE_TYPE') == 'linux':
        pass


def turn_down_volume():
    if os.getenv('DEVICE_TYPE') == 'win32':
        volume = get_Speaker_volume()
        currentVolume = volume.GetMasterVolumeLevel()

        try:
            volume.SetMasterVolumeLevel((currentVolume - 1.5), None)
        except:
            volume.SetMasterVolumeLevelScalar(0, None)
    elif os.getenv('DEVICE_TYPE') == 'linux':
        pass
    
        

def min_volume():
    if os.getenv('DEVICE_TYPE') == 'win32':
        volume = get_Speaker_volume()
        volume.SetMasterVolumeLevelScalar(0, None)
    elif os.getenv('DEVICE_TYPE') == 'linux':
        pass

def max_volume():
    if os.getenv('DEVICE_TYPE') == 'win32':
        volume = get_Speaker_volume()
        volume.SetMasterVolumeLevelScalar(1, None)
    elif os.getenv('DEVICE_TYPE') == 'linux':
        pass
    

def unmute_speakers():
    if os.getenv('DEVICE_TYPE') == 'win32':
        volume = get_Speaker_volume()
        volume.SetMute(0,None)
    elif os.getenv('DEVICE_TYPE') == 'linux':
        pass
    
# ------------------------------------------------------------------------------------------------

# These are for the microphone!!!
def get_microphone_volume():
    devices = AudioUtilities.GetMicrophone()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume

def mute_mic():
    if os.getenv('DEVICE_TYPE') == 'win32':
        volume = get_microphone_volume()
        volume.SetMute(1, None)
    elif os.getenv('DEVICE_TYPE') == 'linux':
        pass

def unmute_mic():
    if os.getenv('DEVICE_TYPE') == 'win32':
        volume = get_microphone_volume()
        volume.SetMute(0, None)
    elif os.getenv('DEVICE_TYPE') == 'linux':
        pass

# --------------------------------------------------------------------------------------

# Text to speech code

import pyttsx3

engine = pyttsx3.init()  # object creation

"""RATE"""
rate = engine.getProperty("rate")  # getting details of current speaking rate
print(rate)  # printing current voice rate
engine.setProperty("rate", 150)  # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty(
    "volume"
)  # getting to know current volume level (min=0 and max=1)
print(volume)  # printing current volume level
engine.setProperty("volume", 1)  # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty("voices")  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty(
    "voice", voices[1].id
)  # changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say("My current speaking rate is " + str(rate))
engine.runAndWait()
engine.stop()

