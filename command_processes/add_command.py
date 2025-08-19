import os, sys

from dotenv import load_dotenv
import write_command, subprocess


def add_command():
    if "--inside-cmd" not in sys.argv:
        os.system(f'start cmd /c python "{__file__}" --inside-cmd')
        sys.exit()


    print("Running add_command interactive mode")


    print("list of types commands:\n1.open file\n2.add shortcut\n\n")
    cmd = input("What type of command? ")

    if cmd == "open file":
        import time

        print("Please select the file to open")
        time.sleep(1)
        from tkinter import Tk, filedialog

        Tk().withdraw()

        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")


        exe_path = filedialog.askopenfilename(
            title="Select an application",
            initialdir = desktop_path
        )


        if exe_path:
            os.system('cls')
            print("Click the CMD Window before typing.\n")
            program_name = input("Whats the programs name? ")
            write_command.write_open_file_command(exe_path, program_name)
            print(f"Saved command as [Open {program_name}]")

            user_choice = input("\n\nWant to add another? (yes or no): ")
            if user_choice == "yes" or user_choice == "y":
                os.system('cls')
                add_command()
            else:
                #another example of the .env in play this currently will just kill the program if .bat not setup properly.
                load_dotenv(dotenv_path=r'.env')
                subprocess.Popen([os.getenv('APP')], shell=True, creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP)
                kill()



        else:
            print("No file selected.")

    elif cmd == 'add shortcut':
        pass
    
    else:
        print("Not valid choice.")
        os.system('cls')
        add_command()
    



def kill():
    with open("pid.txt", "r") as f:
        old_pid = f.read().strip()
    subprocess.run(f"taskkill /PID {old_pid} /F", shell=True)

add_command()