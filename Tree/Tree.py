class Tree:

    def __init__(self, type, value=None, child=None, lineno=None):
        self.type = type
        self.value = value
        self.child = child
        self.lineno = lineno

    def __repr__(self):
        return f'''{self.type} {self.value} {self.lineno}'''

    def print(self, level: int = 0):
        if self is None:
            return
        print(' ' * level, self)
        if type(self.child) is Tree:
            self.child.print(level + 1)
        elif type(self.child) is list:
            for i in range(len(self.child)):
                self.child[i].print(level + 1)
        elif type(self.child) is dict:
            for key, value in self.child.items():
                print(' ' * (level + 1), key)
                if value:
                    value.print(level + 2)