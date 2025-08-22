import os, ctypes, time, sys

user_device = sys.platform

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
            return(True, "") 
        except Exception as e:
            volume.SetMasterVolumeLevelScalar(1, None)
            return(False, f"Already was max volume {e}")
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
            return(True, "") 
        except Exception as e:
            volume.SetMasterVolumeLevelScalar(0, None)
            return(False, f"Already at min volume: {e}")
    elif user_device == 'linux':
        pyinner.decrease()
    

def min_volume():
    """
    Turn down the volume.
    BEHAVIOR: Volume decreased to zero.
    """
    if user_device == 'win32':
        try:
            volume = get_Speaker_volume()
            volume.SetMasterVolumeLevelScalar(0, None)
            return(True, "") 
        except Exception as e:
            return(False, f"Error occured: {e}")
    elif user_device == 'linux':
        pyinner.custom(percent=0)

def max_volume():
    """
    Turn up the volume.
    BEHAVIOR: Volume increased to max.
    """
    if user_device == 'win32':
        try:
            volume = get_Speaker_volume()
            volume.SetMasterVolumeLevelScalar(1, None)
            return(True, "") 
        except Exception as e:
            return(False, f"Error occured: {e}")
        
    elif user_device == 'linux':
        pyinner.custom(percent=150)
    

def unmute_speakers():
    """
    Unmute the speakers.
    WINDOWS BEHAVIOR: Volume unmuted.
    LINUX BEHAVIOR: Volume set to 50%.
    """
    if user_device == 'win32':
        try:
            volume = get_Speaker_volume()
            volume.SetMute(0,None)
            return(True, "") 
        except Exception as e:
            return(False, f"Error occured: {e}")
        
    elif user_device == 'linux':
        pyinner.custom(percent=50)

def mute_speakers():
    """
    Unmute the speakers.
    WINDOWS BEHAVIOR: Volume unmuted.
    LINUX BEHAVIOR: Volume set to 50%.
    """
    if user_device == 'win32':
        try:
            volume = get_Speaker_volume()
            volume.SetMute(1,None)
            return(True, "") 
        except Exception as e:
            return(False, f"Error occured: {e}")
    elif user_device == 'linux':
        pyinner.custom(percent=0)



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
        try:
            volume = get_microphone_volume()
            volume.SetMute(1, None)
            return(True, "") 
        except Exception as e:
            return(False, f"Error occured: {e}")
        
    elif user_device == 'linux':
        os.system("amixer set Capture nocap")


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
    try:
        VK_MEDIA_PLAY_PAUSE = 0xB3
        ctypes.windll.user32.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, 0, 0)
        ctypes.windll.user32.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, 2, 0) 
        time.sleep(1)
        return(True, "") 
    except Exception as e:
        return(False, f"Error occured: {e}")

def next_track():
    try:
        VK_MEDIA_NEXT_TRACK = 0xB0
        ctypes.windll.user32.keybd_event(VK_MEDIA_NEXT_TRACK, 0, 0, 0)  
        ctypes.windll.user32.keybd_event(VK_MEDIA_NEXT_TRACK, 0, 2, 0) 
        time.sleep(1)
        return(True, "") 
    except Exception as e:
        return(False, f"Error occured: {e}")


def rewind_track():
    try:
        VK_MEDIA_PREV_TRACK = 0xB1
        ctypes.windll.user32.keybd_event(VK_MEDIA_PREV_TRACK, 0, 0, 0) 
        ctypes.windll.user32.keybd_event(VK_MEDIA_PREV_TRACK, 0, 2, 0)
        time.sleep(1)
        return(True, "")
    except Exception as e:
        return(False, f"Error occured: {e}")
    

def previous_track():
    try:
        VK_MEDIA_PREV_TRACK = 0xB1

        for i in range(2):
            ctypes.windll.user32.keybd_event(VK_MEDIA_PREV_TRACK, 0, 0, 0) 
            ctypes.windll.user32.keybd_event(VK_MEDIA_PREV_TRACK, 0, 2, 0)
            time.sleep(.2)

        time.sleep(1)
        return(True, "")
    except Exception as e:
        return(False, f"Error occured: {e}")
    



    
    
