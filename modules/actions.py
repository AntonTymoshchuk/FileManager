import os
import pathlib
import platform


def create_new_directory(display):
    path = None
    i = 0
    while True:
        if i == 0:
            if platform.system() == 'Windows':
                path = pathlib.Path(display.title + '\\New directory')
            elif platform.system() == 'Linux':
                path = pathlib.Path(display.title + '/New directory')
            elif platform.system() == 'Darwin':
                path = pathlib.Path(display.title + '/New directory')
        else:
            if platform.system() == 'Windows':
                path = pathlib.Path(display.title + '\\New directory ({0})'.format(i))
            elif platform.system() == 'Linux':
                path = pathlib.Path(display.title + '/New directory ({0})'.format(i))
            elif platform.system() == 'Darwin':
                path = pathlib.Path(display.title + '/New directory ({0})'.format(i))
        if not path.exists():
            break
        i += 1
    path.mkdir(parents=True)


def create_new_file(display):
    path = None
    i = 0
    while True:
        if i == 0:
            if platform.system() == 'Windows':
                path = pathlib.Path(display.title + '\\New file.txt')
            elif platform.system() == 'Linux':
                path = pathlib.Path(display.title + '/New file.txt')
            elif platform.system() == 'Darwin':
                path = pathlib.Path(display.title + '/New file.txt')
        else:
            if platform.system() == 'Windows':
                path = pathlib.Path(display.title + '\\New file ({0}).txt'.format(i))
            elif platform.system() == 'Linux':
                path = pathlib.Path(display.title + '/New file ({0}).txt'.format(i))
            elif platform.system() == 'Darwin':
                path = pathlib.Path(display.title + '/New file ({0}).txt'.format(i))
        if not path.exists():
            break
        i += 1
    path.touch()


def delete_selected_object(display):
    if len(display.items) > 0:
        path = pathlib.Path(display.items[display.selector.position])
        if not path.is_dir():
            os.remove(str(path))
        else:
            delete_directory(path)


def delete_directory(path):
    for item in path.iterdir():
        print(item)
        if not item.is_dir():
            os.remove(str(item))
        elif item.is_dir():
            print('delete directory')
            delete_directory(item)
    path.rmdir()
