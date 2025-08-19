import ctypes, os, warnings

if os.getenv('DEVICE_TYPE') == 'win32':
    import screen_brightness_control as sbc, os, subprocess
else:
    pass

from dotenv import load_dotenv
load_dotenv(dotenv_path=r'.env')
user_device = os.getenv('DEVICE_TYPE')
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
    except PermissionError:
        raise PermissionError("Denied - execute as root.")

def linux_get_brightness() -> int:
    brightness_path, max_path = get_linux_brightness_paths()
    current_brightness_obj, max_brightness_obj = get_linux_brightness_properties()

    return int(current_brightness_obj / 100 * max_brightness_obj)


def decrease_brightness():
    if user_device == 'win32':
        sbc.set_brightness('-20')
    elif user_device == 'linux':
        current = linux_get_brightness_raw()
        linux_set_brightness(current - int(0.2 * current))
        
def increase_brightness():
     if user_device == 'win32':
        sbc.set_brightness('+20')
     elif user_device == 'linux':
        current = linux_get_brightness_raw()
        linux_set_brightness(current + int(0.2 * current))

def max_brightness():
    if user_device == 'win32':
        sbc.set_brightness('100')
    elif user_device == 'linux':
        _, max_brightness = get_linux_brightness_properties()  # get current max
        linux_set_brightness(max_brightness)

def min_brightness():
    if user_device == 'win32':
        sbc.set_brightness('0.7', force=True)

    elif user_device == 'linux':
        linux_set_brightness(5) # DO NOT SET TO ZERO!


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

    subprocess.run(f"taskkill /PID {pid} /F", shell=True)



def get_linux_active():

    if os.environ.get("WAYLAND_DISPLAY"):
        return "Wayland"
    elif os.environ.get("DISPLAY"):
        from Xlib import display
        import psutil, subprocess


        d = display.Display()
        root = d.screen().root

        NET_ACTIVE_WINDOW = d.intern_atom('_NET_ACTIVE_WINDOW')
        NET_WM_NAME = d.intern_atom('_NET_WM_NAME')

        window_id = root.get_full_property(NET_ACTIVE_WINDOW, display.X.AnyPropertyType).value[0]
        window = d.create_resource_object('window', window_id)


        window_name = window.get_full_property(NET_WM_NAME, 0).value.decode('utf-8')

        pid_atom = d.intern_atom('_NET_WM_PID')
        pid = window.get_full_property(pid_atom, 0).value[0]
        process_name = psutil.Process(pid).name()

        print(f'title: {window_name}, pid: {pid}, process: {process_name}')
# ______________________________________________________________________________________________________________

# Other system functions 


def lock_screen():
    if user_device == 'win32':
        ctypes.windll.user32.LockWorkStation() 
    elif user_device == 'linux':
        pass

def restart():
    os.system('shutdown /r /t 1')

def shutdown():
    os.system('shutdown /s /t 2')




