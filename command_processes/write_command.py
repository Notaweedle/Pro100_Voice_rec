import os

def write_open_file_command(file_path, program_name):

    new_block = (
        f'    elif "open {program_name.lower()}" in command:\n'
        f'        a.say("opening {program_name.lower()}")\n'
        f'        os.startfile(r"{file_path}")\n\n'
    )

    write_new_command(new_block)


def write_new_command(new_block):
    commands_file = os.path.join(os.path.dirname(__file__), "..", "commands.py")
    commands_file = os.path.abspath(commands_file)

    with open(commands_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    insert_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith('else:'):
            insert_index = i
            break

    if insert_index is None:
        raise ValueError("No 'else:' block found in commands.py")


    lines.insert(insert_index, new_block)

    with open(commands_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)