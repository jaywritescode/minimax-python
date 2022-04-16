from minimax import minimax_decision
from src.state import State


def test_minimax():
    b1 = ExampleState('b1', utility=3)
    b2 = ExampleState('b2', utility=12)
    b3 = ExampleState('b3', utility=8)

    c1 = ExampleState('c1', utility=2)
    c2 = ExampleState('c2', utility=4)
    c3 = ExampleState('c3', utility=6)

    d1 = ExampleState('d1', utility=14)
    d2 = ExampleState('d2', utility=5)
    d3 = ExampleState('d3', utility=2)

    B = ExampleState('B', successors=[b1, b2, b3])
    C = ExampleState('C', successors=[c1, c2, c3])
    D = ExampleState('D', successors=[d1, d2, d3])
    A = ExampleState('A', successors=[B, C, D])

    assert minimax_decision(A) is B


class ExampleState(State):
    def __init__(self, name, *, successors=[], utility=None):
        super().__init__(name)
        self._successors = successors
        self._utility = utility

    def successors(self):
        return self._successors

    @property
    def utility(self):
        return self._utility

    @utility.setter
    def utility(self, value):
        # TODO: should be immutable once set
        self._utility = value
