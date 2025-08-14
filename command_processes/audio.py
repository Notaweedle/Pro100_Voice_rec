import os, ctypes, time
from dotenv import load_dotenv
import pyautogui
load_dotenv(dotenv_path=r'.env')

user_device = os.getenv('DEVICE_TYPE')

if user_device == 'win32':
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    from comtypes import CLSCTX_ALL
    from ctypes import cast, POINTER

elif user_device == 'linux':

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

def turn_up_volume():
    """
    Turn up the volume.
    WINDOWS BEHAVIOR: Increase volume by two.
    LINUX BEHAVIOR: Increase the volume.
    """
    if user_device == 'win32':
        volume = get_Speaker_volume()
        currentVolume = volume.GetMasterVolumeLevel()

        try:
            volume.SetMasterVolumeLevel((currentVolume + 1.8), None)
        except:
            volume.SetMasterVolumeLevelScalar(1, None)
    elif user_device == 'linux':
        pyinner.increase()

def turn_down_volume():
    """
    Turn down the volume.
    WINDOWS BEHAVIOR: Decrease volume by 1.5
    LINUX BEHAVIOR: Decrease the volume.
    """
    if user_device == 'win32':
        volume = get_Speaker_volume()
        currentVolume = volume.GetMasterVolumeLevel()

        try:
            volume.SetMasterVolumeLevel((currentVolume - 1.8), None)
        except:
            volume.SetMasterVolumeLevelScalar(0, None)
    elif user_device == 'linux':
        pyinner.decrease()
    

def min_volume():
    """
    Turn down the volume.
    BEHAVIOR: Volume decreased to zero.
    """
    if user_device == 'win32':
        volume = get_Speaker_volume()
        volume.SetMasterVolumeLevelScalar(0, None)
    elif user_device == 'linux':
        os.system("pactl set-sink-volume 0 0")

def max_volume():
    """
    Turn up the volume.
    BEHAVIOR: Volume increased to max.
    """
    if user_device == 'win32':
        volume = get_Speaker_volume()
        volume.SetMasterVolumeLevelScalar(1, None)
    elif user_device == 'linux':
        os.system("pactl set-sink-volume 0 65565")
    

def unmute_speakers():
    """
    Unmute the speakers.
    WINDOWS BEHAVIOR: Volume unmuted.
    LINUX BEHAVIOR: Volume set to 50%.
    """
    if user_device == 'win32':
        volume = get_Speaker_volume()
        volume.SetMute(0,None)
    elif user_device == 'linux':
        vol = 65564/2
        os.system(f"pactl set-sink-volume 0 {vol}")

def mute_speakers():
    """
    Unmute the speakers.
    WINDOWS BEHAVIOR: Volume unmuted.
    LINUX BEHAVIOR: Volume set to 0%.
    """
    if user_device == 'win32':
        volume = get_Speaker_volume()
        volume.SetMute(1,None)
    elif user_device == 'linux':
        os.system(f"pactl set-sink-volume 0 0")

    

# ------------------------------------------------------------------------------------------------

# These are for the microphone!!!
def get_microphone_volume():

    devices = AudioUtilities.GetMicrophone()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume

def mute_mic():
    if user_device == 'win32':
        volume = get_microphone_volume()
        volume.SetMute(1, None)
    elif user_device == 'linux':
        pyautogui.press('micmute')

def unmute_mic():
    if user_device == 'win32':
        volume = get_microphone_volume()
        volume.SetMute(0, None)
    elif user_device == 'linux':
        pyautogui.press('micmute')

# --------------------------------------------------------------------------------------

# Text to speech code
def speak(text):
    import pyttsx3
    engine = pyttsx3.init() 
    engine.setProperty("rate", 120)  
    engine.setProperty("volume", 1) 
    voices = engine.getProperty("voices") 
    engine.setProperty("voice", voices[1].id) 
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ________________________________________________________________________

# media controls

def pause_or_play():
    
    VK_MEDIA_PLAY_PAUSE = 0xB3
    ctypes.windll.user32.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, 0, 0)
    ctypes.windll.user32.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, 2, 0) 
    time.sleep(1)
    print('media paused or played')

def next_track():

    VK_MEDIA_NEXT_TRACK = 0xB0
    ctypes.windll.user32.keybd_event(VK_MEDIA_NEXT_TRACK, 0, 0, 0)  
    ctypes.windll.user32.keybd_event(VK_MEDIA_NEXT_TRACK, 0, 2, 0) 
    time.sleep(1)
    print('skipped to next track')

def rewind_track():
    VK_MEDIA_PREV_TRACK = 0xB1
    ctypes.windll.user32.keybd_event(VK_MEDIA_PREV_TRACK, 0, 0, 0) 
    ctypes.windll.user32.keybd_event(VK_MEDIA_PREV_TRACK, 0, 2, 0)
    time.sleep(1)
    print('rewinded')

def previous_track():
    VK_MEDIA_PREV_TRACK = 0xB1

    for i in range(2):
        ctypes.windll.user32.keybd_event(VK_MEDIA_PREV_TRACK, 0, 0, 0) 
        ctypes.windll.user32.keybd_event(VK_MEDIA_PREV_TRACK, 0, 2, 0)
        time.sleep(.2)

    time.sleep(1)
    print('previous media playing')



    
    
