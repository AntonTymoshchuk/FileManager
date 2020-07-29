from modules import common, selection


class Display:
    def __init__(self):
        self.title = None
        self.items = []
        self.names = None
        self.showing_partitions = False
        self.selector = selection.Selector(self)

    def print(self, title, items, position, names=None):
        common.update_console()
        self.title = title
        self.items = items
        self.names = names
        self.selector.create_selection(position)
        if names is not None:
            self.showing_partitions = True
        else:
            self.showing_partitions = False
        print('{0}\n'.format(self.title))
        if len(self.items) > 0:
            i = 0
            if self.names is None:
                while i < len(self.items):
                    if self.items[i].is_dir():
                        print('d {0} {1}'.format(self.selector.selection_list[i], self.items[i].name))
                    else:
                        print('F {0} {1}'.format(self.selector.selection_list[i], self.items[i].name))
                    i += 1
            else:
                while i < len(self.names):
                    if self.items[i].is_dir():
                        print('d {0} {1}'.format(self.selector.selection_list[i], self.names[i]))
                    else:
                        print('F {0} {1}'.format(self.selector.selection_list[i], self.names[i]))
                    i += 1
        else:
            print('  Empty')
        self.selector.director.start_directing()

    def update(self):
        common.update_console()
        print('{0}\n'.format(self.title))
        i = 0
        if self.names is None:
            while i < len(self.items):
                if self.items[i].is_dir():
                    print('d {0} {1}'.format(self.selector.selection_list[i], self.items[i].name))
                else:
                    print('F {0} {1}'.format(self.selector.selection_list[i], self.items[i].name))
                i += 1
        else:
            while i < len(self.names):
                if self.items[i].is_dir():
                    print('d {0} {1}'.format(self.selector.selection_list[i], self.names[i]))
                else:
                    print('F {0} {1}'.format(self.selector.selection_list[i], self.names[i]))
                i += 1
