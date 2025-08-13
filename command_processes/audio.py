import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=r'.env')
if os.getenv('DEVICE_TYPE') == 'win32':
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    from comtypes import CLSCTX_ALL
    from ctypes import cast, POINTER
elif os.getenv('DEVICE_TYPE') == 'linux':
    import pyvolume.pyvolume as pyinner


# These are for the speakers not the input, so output!!
def get_Speaker_volume():
    """
    UNSAFE FOR LINUX!
    Get the current speaker volume.
    :return: Volume object.
    """
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume

def turn_up_volume() -> None:
    """
    Turn up the volume.
    WINDOWS BEHAVIOR: Increase volume by two.
    LINUX BEHAVIOR: Increase the volume.
    """
    if os.getenv('DEVICE_TYPE') == 'win32':
        volume = get_Speaker_volume()
        currentVolume = volume.GetMasterVolumeLevel()

        try:
            volume.SetMasterVolumeLevel((currentVolume + 1.8), None)
        except:
            volume.SetMasterVolumeLevelScalar(1, None)
    elif os.getenv('DEVICE_TYPE') == 'linux':
        pyinner.increase()

turn_up_volume()

def turn_down_volume() -> None:
    """
    Turn down the volume.
    WINDOWS BEHAVIOR: Decrease volume by 1.5
    LINUX BEHAVIOR: Decrease the volume.
    """
    if os.getenv('DEVICE_TYPE') == 'win32':
        volume = get_Speaker_volume()
        currentVolume = volume.GetMasterVolumeLevel()

        try:
            volume.SetMasterVolumeLevel((currentVolume - 1.8), None)
        except:
            volume.SetMasterVolumeLevelScalar(0, None)
    elif os.getenv('DEVICE_TYPE') == 'linux':
        pyinner.decrease()
    
        

def min_volume() -> None:
    """
    Turn down the volume.
    BEHAVIOR: Volume decreased to zero.
    """
    if os.getenv('DEVICE_TYPE') == 'win32':
        volume = get_Speaker_volume()
        volume.SetMasterVolumeLevelScalar(0, None)
    elif os.getenv('DEVICE_TYPE') == 'linux':
        pyinner.custom(percent=0)

def max_volume() -> None:
    """
    Turn up the volume.
    BEHAVIOR: Volume increased to max.
    """
    if os.getenv('DEVICE_TYPE') == 'win32':
        volume = get_Speaker_volume()
        volume.SetMasterVolumeLevelScalar(1, None)
    elif os.getenv('DEVICE_TYPE') == 'linux':
        pyinner.custom(percent=150)
    

def unmute_speakers() -> None:
    """
    Unmute the speakers.
    WINDOWS BEHAVIOR: Volume unmuted.
    LINUX BEHAVIOR: Volume set to 50%.
    """
    if os.getenv('DEVICE_TYPE') == 'win32':
        volume = get_Speaker_volume()
        volume.SetMute(0,None)
    elif os.getenv('DEVICE_TYPE') == 'linux':
        pyinner.custom(percent=50)

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
