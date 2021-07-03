class Tree(object):
    def __init__(self, data):
        self.data = data
        self.children = list()
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, level=None):
        if level != None and self.getLevel() > level:
            return 
        spaces = ' ' * self.getLevel() * 3
        prefix = spaces + '|--' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)
