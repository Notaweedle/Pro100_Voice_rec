import os, sys


PYTHON_EXE = sys.executable
PYTHONW_EXE = os.path.join(os.path.dirname(sys.executable), "pythonw.exe")
SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "command_processes", "add_command.py")
LISTENER_PATH = os.path.join(os.path.dirname(__file__), "listener.pyw")
DEVICE_TYPE = sys.platform
# identifier string like 'win32' for Windows, 'linux' for Linux, and 'darwin' for macOS. 
# we dont need the bat file when we bundle the application to .exe

env_write = f'PYTHON_EXE={PYTHON_EXE}\nPYTHONW_EXE={PYTHONW_EXE}\nSCRIPT_PATH={SCRIPT_PATH}\nDEVICE_TYPE={DEVICE_TYPE}\n'

with open('.env', 'w') as env:
    env.write(env_write)
