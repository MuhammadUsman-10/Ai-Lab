def HillClimb_Search(start_state, end_state, iterations=1000):
    current_state = start_state[:]
    current_cost = manhattan_distance(current_state, end_state)

    for _ in range(iterations):
        neighbors = get_neighbors(current_state)
        neighbor_costs = [(neighbor, manhattan_distance(neighbor, end_state)) for neighbor in neighbors]
        neighbor_costs.sort(key=lambda x: x[1])  # Sort neighbors by their costs
        
        # Check if there's a better neighbor
        best_neighbor, best_neighbor_cost = neighbor_costs[0]
        if best_neighbor_cost >= current_cost:
            # If no better neighbor, return current state
            return current_state
        else:
            # Move to the better neighbor
            current_state = best_neighbor
            current_cost = best_neighbor_cost

    # If maximum iterations reached without finding goal state, return current state
    return current_state

def manhattan_distance(initial_state, goal_state):  # Calculates the Manhattan distance heuristic for a state
    cost = 0
    for i in range(len(initial_state)):
        row1, column1 = divmod(initial_state[i], 3)
        row2, column2 = divmod(goal_state.index(initial_state[i]), 3)
        cost += abs(row1 - row2) + abs(column1 - column2)
    return cost

def get_neighbors(state):
    zero_index = state.index(0)
    neighbors = []
    
    if zero_index - 3 >= 0:  # upward move
        neighbor = state[:]
        neighbor[zero_index], neighbor[zero_index - 3] = neighbor[zero_index - 3], neighbor[zero_index]
        neighbors.append(neighbor)
    if zero_index + 3 < len(state):  # downward move
        neighbor = state[:]
        neighbor[zero_index], neighbor[zero_index + 3] = neighbor[zero_index + 3], neighbor[zero_index]
        neighbors.append(neighbor)
    if zero_index % 3 != 0:  # left move
        neighbor = state[:]
        neighbor[zero_index], neighbor[zero_index - 1] = neighbor[zero_index - 1], neighbor[zero_index]
        neighbors.append(neighbor)
    if zero_index % 3 != 2:  # right move
        neighbor = state[:]
        neighbor[zero_index], neighbor[zero_index + 1] = neighbor[zero_index + 1], neighbor[zero_index]
        neighbors.append(neighbor)
    
    return neighbors

# Example usage:
initial_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
goal_state = [2, 8, 1, 0, 4, 3, 7, 6, 5]
solution = HillClimb_Search(initial_state, goal_state)
print("Solution state found by Hill Climbing algorithm:", solution)