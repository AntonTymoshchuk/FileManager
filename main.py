import sys
from modules import common, displaying
import pathlib

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print('FileManager ERROR: There must be only one argument or no argument at all.')
        sys.exit(-1)
    elif len(sys.argv) == 2:
        path = pathlib.Path(sys.argv[1])
        if not path.exists():
            print('FileManager ERROR: There must be a path to an existing directory.')
            sys.exit(-1)
        else:
            display = displaying.Display()
            common.open_directory(display, path, 0)
    elif len(sys.argv) == 1:
        path = pathlib.Path(str(pathlib.Path.home()))
        display = displaying.Display()
        common.open_directory(display, path, 0)
