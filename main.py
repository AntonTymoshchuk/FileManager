import sys
from modules import common, displaying
import pathlib

if __name__ == '__main__':
    # At first, check if user started our application with two, or more
    # arguments (actually, we must check if count of arguments more than 2,
    # because the first one is the application itself)
    if len(sys.argv) > 2:
        # If count of arguments is more than 2, than we must notify our
        # user, that we don't expect more than 1 argument
        print('There must be only one argument or no argument at all.')

        # Close application
        sys.exit(-1)

    # Check if user started our application with only one argument
    # (actually, we must check if count of arguments equals 2, because
    # the first one is the application itself)
    elif len(sys.argv) == 2:
        # Import second (actually it is first user's argument) to a variable
        path = pathlib.Path(sys.argv[1])

        # Check if folder, represented by variable, is existing
        if not path.exists():
            # No such folder, so we must notify our user, that he made
            # a mistake, or something else gone wrong
            print('There must be a path to an existing directory.')

            # And close application, no sense to continue working, and
            # trying to solve problem with not existing folder ourself
            sys.exit(-1)
        else:
            # Folder exists, so we must start our directory functionality
            # Go to 'modules/displaying.py'...
            display = displaying.Display()
            common.open_directory(display, path, 0)
    elif len(sys.argv) == 1:
        path = pathlib.Path(str(pathlib.Path.home()))
        display = displaying.Display()
        common.open_directory(display, path, 0)
