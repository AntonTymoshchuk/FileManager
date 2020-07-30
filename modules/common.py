import os
import platform


def update_console():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Darwin':
        os.system('clear')


def sort_items_by_name(items):
    items.sort(key=lambda sorted_item: sorted_item.name.lower())


def open_directory(display, path, position):
    items = []
    try:
        directory_iterator = path.iterdir()
        for item in directory_iterator:
            items.append(item)
        sort_items_by_name(items)
        display.print(str(path), items, position)
    except Exception as exception:
        print(exception.args[1])


def show_partitions(display, partitions, position, names):
    names.sort(key=lambda p_name: p_name.lower())
    display.print('Partitions', partitions, position, names)


def run_file(file_path):
    if platform.system() == 'Windows':
        os.system('"{0}"'.format(file_path))
    elif platform.system() == 'Linux':
        os.system('xdg-open "{0}"'.format(file_path))
    elif platform.system() == 'Darwin':
        os.system('open "{0}"'.format(file_path))
