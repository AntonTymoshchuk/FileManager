from pynput.keyboard import Key, Listener


class Director:

    def on_press(self, key):
        if key == Key.down:
            self.selector.move_down()
        elif key == Key.up:
            self.selector.move_up()
        elif key == Key.enter:
            self.selector.move_in()
        elif key == Key.esc:
            self.selector.move_out()

    def on_release(self, key):
        pass

    def __init__(self, selector):
        self.selector = selector
        self.listener = Listener(self.on_press, self.on_release)
        self.started = False

    def start_directing(self):
        if not self.started:
            self.started = True
            self.listener.start()
            self.listener.join()
