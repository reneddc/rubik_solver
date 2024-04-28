class State:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.actions = []
        self.parent = None
    
    def add_action(self, other_value):
        if other_value not in self.actions:
            self.actions.append(other_value)

    def mark_visited(self):
        self.visited = True

    def mark_unvisited(self):
        self.visited = False

    def set_parent(self, parent):
        self.parent = parent

    def __lt__(self, other):
        return self.value <= other.value

    def __str__(self):
        return f"{self.value}, visited:{self.visited} -> {self.actions}"