from queue import PriorityQueue

def manhattan_distance(state, goal):  # Calculates the Manhattan distance heuristic for a state
    distance = 0
    for i in range(len(state)):
        row1, column1 = divmod(state[i], 3)
        row2, column2 = divmod(goal.index(state[i]), 3)
        distance += abs(row1 - row2) + abs(column1 - column2)
    return distance

class Node:
    def __init__(self, state, parent, goal_cost, heuristic_cost):
        self.state = state
        self.parent = parent
        self.goal_cost = goal_cost  # Cost from start state
        self.heuristic_cost = heuristic_cost  # Heuristic cost to goal
        self.final_cost = goal_cost + heuristic_cost  # Total cost (final_cost = goal_cost + heuristic_cost)

    def __lt__(self, other):
        return self.final_cost < other.final_cost

def expand_node(node, goal_state):   # Expands a node and generates its child nodes
    children = []
    for move in get_possible_moves(node.state):
        child_state = apply_move(node.state, move)
        goal_cost = node.goal_cost + 1
        heuristic_cost = manhattan_distance(child_state, goal_state)
        child_node = Node(child_state, node, goal_cost, heuristic_cost)
        children.append(child_node)
    return children

def get_possible_moves(state):   # Returns possible moves (indexes of zero) in the puzzle
    zero_index = state.index(0)
    moves = []
    if zero_index - 3 >= 0:  # upward move
        moves.append(-3)
    if zero_index + 3 < len(state):  # downward move
        moves.append(3)
    if zero_index % 3 != 0:  # left move
        moves.append(-1)
    if zero_index % 3 != 2:  # right move
        moves.append(1)
    return moves

def apply_move(state, move):  # Applies move to the puzzle and returns the new state
    new_state = state[:]
    zero_index = new_state.index(0)
    new_state[zero_index], new_state[zero_index + move] = new_state[zero_index + move], new_state[zero_index]
    return new_state

def admisible_search(initial_state, goal_state): # A* search algorithm
    frontier = PriorityQueue()
    frontier.put(Node(initial_state, None, 0, manhattan_distance(initial_state, goal_state)))
    explored = set()

    while not frontier.empty():
        current_node = frontier.get()
        explored.add(tuple(current_node.state))
        # print("Exploring", current_node.state)

        if current_node.state == goal_state:   # Solution found, backtrack to get the path
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        # Expand current node
        for child_node in expand_node(current_node, goal_state):
            if tuple(child_node.state) not in explored:
                frontier.put(child_node)

    # If no solution found
    return None

# Example usage:
initial_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
goal_state = [2, 8, 1, 0, 4, 3, 7, 6, 5]
solution = admisible_search(initial_state, goal_state)
print("Solution path:", solution)
