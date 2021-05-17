import os


def Create_file(file_name):
    with open(file_name, "w") as file:
        file.write("")


def Add_to_file(file_name, content):
    with open(file_name, 'a') as edited_file:
        edited_file.write(content+'\n')


def Replace_content_in_file(file_name, old_str, new_str):
    try:
        with open(file_name, 'r+') as file:
            text = " ".join(file.readlines())
            replaced_content = text.replace(old_str, new_str)
            file.seek(0)
            file.write(replaced_content)
    except FileNotFoundError:
        print('An error occurred')


def Delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("An error occurred")


action = {'Create': Create_file,
          'Add': Add_to_file,
          'Replace': Replace_content_in_file,
          'Delete': Delete_file
          }


def Start_engine():
    command_line = input()
    while not command_line == 'End':
        command, *command_data = command_line.split("-")
        action[command](*command_data)
        command_line = input()


Start_engine()
