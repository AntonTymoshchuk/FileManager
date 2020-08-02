from modules import actions
from pynput.keyboard import Key, Listener, GlobalHotKeys


class Director:

    def on_key_press(self, key):
        if key == Key.down:
            self.selector.move_down()
        elif key == Key.up:
            self.selector.move_up()
        elif key == Key.enter:
            self.selector.move_in()
        elif key == Key.esc:
            self.selector.move_out()
        elif key == Key.delete:
            actions.delete_selected_object(self.selector.display)
        elif key == Key.backspace:
            self.key_listener.stop()
            self.hotkey_listener.stop()
            self.selector.display.terminate = True

    def on_ctrl_d_press(self):
        actions.create_new_directory(self.selector.display)

    def on_ctrl_f_press(self):
        actions.create_new_file(self.selector.display)

    def __init__(self, selector):
        self.selector = selector
        self.started = False
        self.key_listener = Listener(self.on_key_press)
        self.hotkey_listener = GlobalHotKeys({
            '<ctrl>+d': self.on_ctrl_d_press,
            '<ctrl>+f': self.on_ctrl_f_press
        })

    def start_directing(self):
        if not self.started:
            self.started = True
            self.key_listener.start()
            self.hotkey_listener.start()
            self.key_listener.join()
