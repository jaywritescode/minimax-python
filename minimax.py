def minimax_decision(state):
    v = max_value(state)
    for succ in state.successors():
        if succ.utility == v:
            return succ

def max_value(state):
    if state.terminal_test():
        return state.utility

    state.utility = max(min_value(succ) for succ in state.successors())
    return state.utility

def min_value(state):
    if state.terminal_test():
        return state.utility

    state.utility = min(max_value(succ) for succ in state.successors())
    return state.utility