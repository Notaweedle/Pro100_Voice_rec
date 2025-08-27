import ctypes, os, warnings, sys

user_device = sys.platform

if user_device == 'win32':
    import screen_brightness_control as sbc, os, subprocess
else:
    pass

# Screen brightness controls

def get_linux_brightness_paths() -> list[str]:
    brightness_path = "/sys/class/backlight/intel_backlight/brightness"
    max_path = "/sys/class/backlight/intel_backlight/max_brightness"
    return [brightness_path, max_path]

def get_linux_brightness_properties() -> list[int]:
    """
    Get the brightness properties of the Linux system
    :return: [Current Brightness, Max Brightness]
    :exception RuntimeError Execution on a non-linux system.
    """
    brightness_path, max_path = get_linux_brightness_paths()
    if user_device != "linux":
        raise RuntimeError(f"Device is not supported: {user_device}")

    with open(max_path, "r") as f:
        max_brightness = int(f.read().strip())


    with open(brightness_path, "r") as f:
        current_brightness = int(f.read().strip())

    return [int(current_brightness), int(max_brightness)]

def linux_get_brightness_raw() -> int:
    """Return the current brightness in the 0–max_brightness scale."""
    current_brightness, _ = get_linux_brightness_properties()
    return current_brightness

def linux_set_brightness(brightness: int) -> None:
    """Set brightness in the 0–max_brightness scale."""
    brightness_path, max_path = get_linux_brightness_paths()
    _, max_brightness = get_linux_brightness_properties()

    # Clamp to valid range
    brightness = max(0, min(brightness, max_brightness))

    try:
        with open(brightness_path, "w") as f:
            f.write(str(brightness))
            return(True, "") 
    except PermissionError:
        raise PermissionError("Denied - execute as root.")

def linux_get_brightness() -> int:
    brightness_path, max_path = get_linux_brightness_paths()
    current_brightness_obj, max_brightness_obj = get_linux_brightness_properties()

    return int(current_brightness_obj / 100 * max_brightness_obj)


def decrease_brightness():
    if user_device == 'win32':
        try:
            sbc.set_brightness('-20')
            return(True, "") 
        except Exception as e:
            return(False, f"Failed to decrease brightness because: {e}") 
    elif user_device == 'linux':
        try:
            current = linux_get_brightness_raw()
            linux_set_brightness(current - int(0.2 * current))
            return(True, "") 
        except Exception as e:
            return(False, f"Failed to decrease brightness because: {e}") 


        
def increase_brightness():
     if user_device == 'win32':
        try:
            sbc.set_brightness('+20')
            return(True, "") 
        except Exception as e:
            return(False, f"Failed to increase brightness because: {e}") 
        
     elif user_device == 'linux':
        try:
            current = linux_get_brightness_raw()
            linux_set_brightness(current + int(0.2 * current))
            return(True, "") 
        except Exception as e:
            return(False, f"Failed to increase brightness because: {e}") 

def max_brightness():
    if user_device == 'win32':
        try:
            sbc.set_brightness('100')
            return(True, "") 
        except Exception as e:
            return(False, f"Failed to max brightness because: {e}") 
        
    elif user_device == 'linux':
        try:
            _, max_brightness = get_linux_brightness_properties()  # get current max
            linux_set_brightness(max_brightness)
            return(True, "") 
        except Exception as e:
            return(False, f"Failed to max brightness because: {e}") 


def min_brightness():
    print(user_device)
    if user_device == 'win32':
        try:
            sbc.set_brightness('0.7', force=True)
            return(True, "") 
        except Exception as e:
            return(False, f"Failed to min brightness because: {e}") 

    elif user_device == 'linux':
        try:
            linux_set_brightness(5) # DO NOT SET TO ZERO!
            return(True, "") 
        except Exception as e:
            return(False, f"Failed to min brightness because: {e}") 
        


# ______________________________________________________________________________

def get_active_window():
    if user_device != "win32":
        warnings.warn("Attempted usage of a windows only feature on a UNIX platform.")
        return
    import win32gui, win32process , psutil

    hwnd = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(hwnd)

    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    process_name = psutil.Process(pid).name()


    print(f"Title: {title}")
    print(f"Process: {process_name}")
    print(f"PID: {pid}")

    info = [title, process_name, pid]
    return info

def kill_active_window():
    if user_device != "win32":
        warnings.warn("Attempted usage of a windows only feature on a UNIX platform.")
        return
    info = get_active_window()
    title = info[0]
    process = info[1]
    pid = info[2]

    #ADD tts to speak what function is being killed, using the title
    try:
        subprocess.run(f"taskkill /PID {pid} /F", shell=True)
        return(True, "")
    except Exception as e:
            return(False, f"Failed to kill app : {e}") 
# ______________________________________________________________________________________________________________

# Other system functions 


def lock_screen():
    if user_device == 'win32':
        try:
            ctypes.windll.user32.LockWorkStation() 
            return(True, "") 
        except Exception as e:
            return(False, f"Failed to lock screen : {e}") 
        
    elif user_device == 'linux':
        try:
            os.system('xdg-screensaver lock')
            return(True, "") 
        except Exception as e:
            return(False, f"Failed to shutdown: {e}") 

def restart():
    if user_device == 'win32':
        try:
            os.system('shutdown /r /t 4')
            return(True, "") 
        except Exception as e:
            return(False, f"Failed to restart : {e}") 
        
    elif user_device == 'linux':
        try:
            os.system('reboot')
            return(True, "") 
        except Exception as e:
            return(False, f"Failed to shutdown: {e}") 


def shutdown():
    if user_device == 'win32':
        try:
            os.system('shutdown /s /t 4')
            return(True, "") 
        except Exception as e:
            return(False, f"Failed to shutdown: {e}") 
        
    elif user_device == 'linux':
        try:
            os.system('shutdown --no-wall -P')
            return(True, "") 
        except Exception as e:
            return(False, f"Failed to shutdown: {e}") 
