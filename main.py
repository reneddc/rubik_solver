from space_states import SpaceStates
from state import State
from searcher import Searcher
from rubik import Rubik

if __name__ == "__main__":
    space = SpaceStates()
    rubik = Rubik()
    initial_state = State(rubik.charge_cube())
    goal_state = State(rubik.get_sorted_cube())
    searcher = Searcher(space)
    
    print("Buscando en costo uniforme")
    print(searcher.uniform_cost(initual_state.value, end_value))