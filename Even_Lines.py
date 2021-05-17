import re


def replace_symbols(lines):
    return re.sub(r'[-.!?,]', "@", lines)


with open("text.txt", "r") as file:
    lines = file.readlines()
    for row_count in range(len(lines)):
        if row_count % 2 == 0:
            replaced = replace_symbols(lines[row_count]).split()
            print(" ".join(replaced[::-1]))