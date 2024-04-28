class Searcher:
    def __init__(self, space):
        self.space = space

    def breadth_first(self, initial_value, end_value):
        return self.search(initial_value, end_value, Queue())

    def depth_first(self, initial_value, end_value):
        return self.search(initial_value, end_value, Stack())
    
    def uniform_cost(self, initial_value, end_value):
        return self.weighted_search(initial_value, end_value, PriorityQueue())

    def weighted_search(self, initial_value, end_value, frontier):
        initial_state = self.space.get_state(initial_value)
        frontier.put((0, initial_state))
        lowest_costs = {initial_state: 0}

        while not frontier.empty():
            current_cost, current_state = frontier.get()
            print(current_state.value, current_cost)
            # current_state.mark_visited()

            if current_state.value == end_value:
                print("Found", current_state.value, current_cost)
                return (self.build_solution_path(current_state), current_cost)

            for action in current_state.actions:
                next_state = self.space.get_state(action[0])
                new_cost = current_cost + action[1]

                if next_state not in lowest_costs or new_cost < lowest_costs[next_state]:
                    next_state.set_parent(current_state)
                    lowest_costs[next_state] = new_cost
                    print("Expanding:", next_state.value, new_cost)
                    frontier.put((new_cost, next_state))
        return []

    def search(self, initial_value, end_value, frontier):
        initial_state = self.space.get_state(initial_value)
        frontier.push(initial_state)

        while frontier:
            current_state = frontier.pop()
            current_state.mark_visited()

            if current_state.value == end_value:
                return self.build_solution_path(current_state)

            for action in current_state.actions:
                next_state = self.space.get_state(action)
                if not next_state.visited and not frontier.has(next_state):
                    next_state.set_parent(current_state)
                    frontier.push(next_state)
        return []

    def build_solution_path(self, state):
        path = []
        while state:
            path.append(state.value)
            state = state.parent
        return list(reversed(path))