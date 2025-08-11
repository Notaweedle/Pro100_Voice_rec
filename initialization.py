import os
import sys

PYTHON_EXE = sys.executable
PYTHONW_EXE = os.path.join(os.path.dirname(sys.executable), "pythonw.exe")
SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "command_processes", "add_command.py")
LISTENER_PATH = os.path.join(os.path.dirname(__file__), "listener.pyw")

bat = f'@echo off\ncd /d "%~dp0"\nstart "" "{PYTHONW_EXE}" "{LISTENER_PATH}"\nexit'

with open('app.bat', 'w') as f:
    f.write(bat)

APP = os.path.join(os.path.dirname(__file__), "APP.bat")
env_write = f'PYTHON_EXE={PYTHON_EXE}\nPYTHONW_EXE={PYTHONW_EXE}\nSCRIPT_PATH={SCRIPT_PATH}\nAPP={APP}'

with open('.env', 'w') as env:
    env.write(env_write)
