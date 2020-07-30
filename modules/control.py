import time
import pathlib
import threading


class Controller(threading.Thread):
    def __init__(self, display):
        threading.Thread.__init__(self)
        self.display = display
        pass

    def run(self):
        while True:
            self.check_if_current_directory_exists()
            time.sleep(0.1)
        pass

    def check_if_current_directory_exists(self):
        if not self.display.partitions and self.display.title is not None:
            path = pathlib.Path(self.display.title)
            if not path.exists():
                for parent in path.parents:
                    if parent.exists():
                        self.display.title = str(parent)
                        break
                self.display.selector.move_out()
