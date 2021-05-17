import os


def extract_files(dir):
    return [el for el in dir if '.' in el]


def get_report_for_files_extension(files):
    report = {}
    for file in files:
        name, extension = os.path.splitext(file)
        if extension not in report:
            report[extension] = []
        report[extension].append(name)
    return report


dir_content = os.listdir()

files = extract_files(dir_content)
report_info = get_report_for_files_extension(files)

report_str = ""
file_path = os.path.normpath(os.path.expanduser("~/Desktop/report.txt"))


with open(file_path, 'w') as report_file:
    for extension, file_names in sorted(report_info.items(), key=lambda x: x[0]):
        report_str += f'{extension}\n'
        for name in file_names:
            report_str += f'- - - {name}{extension}\n'
    report_file.write(report_str)