class State:
    def __init__(self, name):
        self.name = name

    def terminal_test(self):
        return len(self.successors()) == 0

    def successors(self):
        raise NotImplemented

    def utility(self):
        raise NotImplemented