from modules import common, selection


class Display:
    def __init__(self):
        self.directory_name = None
        self.items = []
        self.names = None
        self.selector = selection.Selector(self)

    def print(self, directory_name, items, position, names=None):
        common.update_console()
        self.directory_name = directory_name
        self.items = items
        self.names = names
        self.selector.create_selection(position)
        print('\n  {0}\n'.format(self.directory_name))
        i = 0
        if self.names is None:
            while i < len(self.items):
                print('  {0} {1}'.format(self.selector.selection_list[i], self.items[i].name))
                i += 1
        else:
            while i < len(self.names):
                print('  {0} {1}'.format(self.selector.selection_list[i], self.names[i]))
                i += 1
        self.selector.director.start_directing()

    def update(self):
        common.update_console()
        print('\n  {0}\n'.format(self.directory_name))
        i = 0
        if self.names is None:
            while i < len(self.items):
                print('  {0} {1}'.format(self.selector.selection_list[i], self.items[i].name))
                i += 1
        else:
            while i < len(self.names):
                print('  {0} {1}'.format(self.selector.selection_list[i], self.names[i]))
                i += 1
