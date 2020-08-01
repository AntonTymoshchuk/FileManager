from modules import common
import time
import pathlib
import platform
import threading


class Controller(threading.Thread):
    def __init__(self, display):
        threading.Thread.__init__(self)
        self.display = display
        pass

    def run(self):
        while True:
            try:
                self.check_path_existence()
                self.inspect_path_items()
                time.sleep(0.001)
            except KeyboardInterrupt:
                pass

    def check_path_existence(self):
        if not self.display.partitions and self.display.title is not None:
            path = pathlib.Path(self.display.title)
            if not path.exists():
                for parent in path.parents:
                    if parent.exists():
                        self.display.title = str(parent)
                        break
                self.display.selector.move_out()

    def inspect_path_items(self):
        if not self.display.partitions and self.display.title is not None:
            path = pathlib.Path(self.display.title)
            current_path_items = []
            for current_item in path.iterdir():
                current_path_items.append(current_item)
            common.sort_items_by_name(current_path_items)
            if len(current_path_items) != len(self.display.items):
                position = self.display.selector.position
                if len(current_path_items) < len(self.display.items):
                    name = self.display.items[self.display.selector.position].name
                    i = 0
                    while i < len(current_path_items):
                        if current_path_items[i].name == name:
                            position = i
                            break
                        i += 1
                    if i == len(current_path_items):
                        position = 0
                elif len(current_path_items) > len(self.display.items):
                    if len(self.display.items) > 0:
                        name = self.display.items[self.display.selector.position].name
                        i = 0
                        while i < len(current_path_items):
                            if current_path_items[i].name == name:
                                position = i
                                break
                            i += 1
                common.open_directory(self.display, path, position)
            else:
                for current_path_item, item in zip(current_path_items, self.display.items):
                    if current_path_item.name != item.name:
                        position = self.display.selector.position
                        name = self.display.items[self.display.selector.position].name
                        i = 0
                        while i < len(current_path_items):
                            if current_path_items[i].name == name:
                                position = i
                                break
                            i += 1
                        if i == len(current_path_items):
                            new_item = list(set(current_path_items) - set(self.display.items))[0]
                            i = 0
                            while i < len(current_path_items):
                                if current_path_items[i].name == new_item.name:
                                    position = i
                                    break
                                i += 1
                            pass
                        common.open_directory(self.display, path, position)
                        break
        elif self.display.partitions and self.display.title is not None:
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
            partition_names.sort(key=lambda p_name: p_name.lower())
            for partition_name in partition_names:
                partition_paths.append(pathlib.Path(partition_name))
            if len(partition_names) != len(self.display.names):
                position = self.display.selector.position
                if len(partition_names) < len(self.display.names):
                    name = self.display.names[self.display.selector.position]
                    i = 0
                    while i < len(partition_names):
                        if partition_names[i] == name:
                            position = i
                            break
                        i += 1
                    if i == len(partition_names):
                        position = 0
                elif len(partition_names) > len(self.display.names):
                    if len(self.display.names) > 0:
                        name = self.display.names[self.display.selector.position]
                        i = 0
                        while i < len(partition_names):
                            if partition_names[i] == name:
                                position = i
                                break
                            i += 1
                common.show_partitions(self.display, partition_paths, position, partition_names)
            else:
                for partition_name, display_name in zip(partition_names, self.display.names):
                    if partition_name != display_name:
                        position = self.display.selector.position
                        name = self.display.names[self.display.selector.position]
                        i = 0
                        while i < len(partition_names):
                            if partition_names[i] == name:
                                position = i
                                break
                            i += 1
                        if i == len(partition_names):
                            new_name = list(set(partition_names) - set(self.display.names))[0]
                            i = 0
                            while i < len(partition_names):
                                if partition_names[i] == new_name:
                                    position = i
                                    break
                                i += 1
                            pass
                        common.show_partitions(self.display, partition_paths, position, partition_names)
                        break
