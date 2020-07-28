import os
import platform
import displaying


def update_console():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Darwin':
        os.system('clear')


def open_directory(display, path, position):
    items = []
    for item in path.iterdir():
        items.append(item)
    display.print(str(path), items, position)


def show_drives(display, drives, position, names):
    display.print('Drives', drives, position, names)


def run_file(file_path):
    if platform.system() == 'Windows':
        os.system('"{0}"'.format(file_path))
    elif platform.system() == 'Linux':
        os.system('xdg-open "{0}"'.format(file_path))
    elif platform.system() == 'Darwin':
        os.system('open "{0}"'.format(file_path))
