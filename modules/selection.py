from modules import common, direction
import pathlib
import platform


class Selector:
    def __init__(self, display):
        self.selection_list = []
        self.position = 0
        self.display = display
        self.director = direction.Director(self)

    def create_selection(self, position):
        self.selection_list.clear()
        self.position = position
        if len(self.display.items) > 0:
            self.selection_list = [' '] * len(self.display.items)
            self.selection_list[self.position] = '>'

    def can_move_down(self):
        if self.position < len(self.selection_list) - 1:
            return True
        else:
            return False

    def can_move_up(self):
        if self.position > 0:
            return True
        else:
            return False

    def move_down(self):
        if not self.can_move_down():
            return False
        self.selection_list[self.position] = ' '
        self.position += 1
        self.selection_list[self.position] = '>'
        self.display.update()
        return True

    def move_up(self):
        if not self.can_move_up():
            return False
        self.selection_list[self.position] = ' '
        self.position -= 1
        self.selection_list[self.position] = '>'
        self.display.update()
        return True

    def move_in(self):
        if not self.display.items[self.position].is_dir():
            common.run_file(str(self.display.items[self.position]))
        else:
            common.open_directory(self.display, self.display.items[self.position], 0)

    def move_out(self):
        if not self.display.showing_partitions:
            path = pathlib.Path(self.display.title)
            parents = path.parents
            if len(parents) > 0:
                self.position = -1
                parent_path = pathlib.Path(str(parents[0]))
                for parent_item in parent_path.iterdir():
                    self.position += 1
                    if str(parent_item) == self.display.title:
                        break
                common.open_directory(self.display, parent_path, self.position)
            else:
                self.position = -1
                partition_paths = []
                partition_names = []
                if platform.system() == 'Windows':
                    import win32api
                    partitions_string = win32api.GetLogicalDriveStrings()
                    partition_names = partitions_string.split('\000')
                    del partition_names[-1:]
                elif platform.system() == 'Linux':
                    import psutil
                    partition_tuples_list = psutil.disk_partitions(True)
                    for partition_tuple in partition_tuples_list:
                        partition_names.append(partition_tuple[1])
                elif platform.system() == 'Darwin':
                    import os
                    print(os.listdir('/Volumes'))
                for partition_name in partition_names:
                    self.position += 1
                    if partition_name == self.display.title:
                        break
                for partition_name in partition_names:
                    partition_paths.append(pathlib.Path(partition_name))
                common.show_partitions(self.display, partition_paths, self.position, partition_names)
