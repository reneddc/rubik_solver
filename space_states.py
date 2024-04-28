class StateSpace():
    def __init__(self):
        self.states = {}

    def add_state(self, state):
        self.states[state.value] = state

    def get_state(self, value):
        if type(value) == tuple:
            return self.states[value[0]]
        return self.states[value]

    def add_edge(self, value1, value2):
        self.states[value1].add_action(value2)

    def add_weighted_edge(self, value1, value2, weight):
        self.states[value1].add_action((value2, weight))

    def reset_visits(self):
        for state in self.states.values():
            state.mark_unvisited()