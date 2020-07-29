import os
import platform


def update_console():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Darwin':
        os.system('clear')


def open_directory(display, path, position):
    items = []
    try:
        directory_iterator = path.iterdir()
        for item in directory_iterator:
            items.append(item)
    except Exception as exception:
        print('\nERROR: {0}'.format(exception.args))
    display.print(str(path), items, position)


def show_partitions(display, drives, position, names):
    display.print('Partitions', drives, position, names)


def run_file(file_path):
    if platform.system() == 'Windows':
        os.system('"{0}"'.format(file_path))
    elif platform.system() == 'Linux':
        os.system('xdg-open "{0}"'.format(file_path))
    elif platform.system() == 'Darwin':
        os.system('open "{0}"'.format(file_path))
