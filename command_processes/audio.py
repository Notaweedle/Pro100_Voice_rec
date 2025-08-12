from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER

def get_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume

def turn_up_volume():
    volume = get_volume()
    currentVolume = volume.GetMasterVolumeLevel()

    try:
        volume.SetMasterVolumeLevel((currentVolume + 2), None)
    except:
        volume.SetMasterVolumeLevelScalar(1, None)


def turn_down_volume():
    volume = get_volume()
    currentVolume = volume.GetMasterVolumeLevel()

    try:
        volume.SetMasterVolumeLevel((currentVolume - 1.5), None)
    except:
        volume.SetMasterVolumeLevelScalar(0, None)

def mute():
    volume = get_volume()

    volume.SetMasterVolumeLevelScalar(0, None)

def max_volume():
    volume = get_volume()

    volume.SetMasterVolumeLevelScalar(1, None)

def unmute():
    volume = get_volume()
    volume.SetMute(0,None)
