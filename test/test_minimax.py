from minimax import minimax_decision
from src.state import State


def test_minimax():
    b1 = TestState('b1', utility=3)
    b2 = TestState('b2', utility=12)
    b3 = TestState('b3', utility=8)

    c1 = TestState('c1', utility=2)
    c2 = TestState('c2', utility=4)
    c3 = TestState('c3', utility=6)

    d1 = TestState('d1', utility=14)
    d2 = TestState('d2', utility=5)
    d3 = TestState('d3', utility=2)

    B = TestState('B', successors=[b1, b2, b3])
    C = TestState('C', successors=[c1, c2, c3])
    D = TestState('D', successors=[d1, d2, d3])
    A = TestState('A', successors=[A, B, C])

    assert minimax_decision(A) is B


class TestState(State):
    def __init__(self, name, *, successors=[], utility=None):
        self.__super__(name)
        self.successors = successors
        self.utility = utility

    def is_terminal(self):
        return len(self.successors) == 0

    def successors(self):
        return self.successors

    def utility(self):
        return self.utility
