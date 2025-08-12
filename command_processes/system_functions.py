import screen_brightness_control as sbc, os

# Screen brightness controls

def decrease_brightness():
     sbc.set_brightness('-20')

def increase_brightness():
     sbc.set_brightness('+20')

def max_brightness():
     sbc.set_brightness('100')

def min_brightness():
     sbc.set_brightness('0')

# ______________________________________________________________________________
 

def get_active_window():
    import win32gui, win32process , psutil

    hwnd = win32gui.GetForegroundWindow()  
    title = win32gui.GetWindowText(hwnd)  

    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    process_name = psutil.Process(pid).name()

    print(f"Title: {title}")
    print(f"Process: {process_name}")
    print(f"PID: {pid}")

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
    






   
    