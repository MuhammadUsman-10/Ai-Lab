from collections import deque

# Define the tree structure
tree = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['G', 'H'],
    'C': ['E', 'F'],
    'D': [],
    'E': [],
    'F': [],
    'G': ['I'],
    'H': [],
    'I': ['K'],
    'K': []
}

# Define the tree problem class
class Tree:
    def __init__(self, tree, initial_state, goal_state):
        self.tree = tree
        self.start = initial_state
        self.goal = goal_state
    def actions(self, state):
        return self.tree.get(state, [])
    def result(self, state, action):
        return action
    def goal_test(self, state):
        return state == self.goal

# Define BFS algorithm
def breadth_first_search(problem):
    frontier = deque([(problem.start, [])])
    explored = set()
    while frontier:
        state, path = frontier.popleft()
        if problem.goal_test(state):
            return path
        explored.add(state)
        for action in problem.actions(state):
            if action not in explored:
                frontier.append((action, path + [action]))


# Define DLS algorithm
def depth_limit_search(problem, depth_limit):
    def recursive_depth_limit_search(state, path, depth):
        if problem.goal_test(state):
            return path
        elif depth == depth_limit:
            return None
        else:
            for action in problem.actions(state):
                result = recursive_depth_limit_search(action, path + [action], depth + 1)
                if result is not None:
                    return result
            return None
    return recursive_depth_limit_search(problem.start, [problem.start], 0)

# Define IDS algorithm
def iterative_deepening_search(problem, max_depth=20):
    for depth_limit in range(max_depth):
        result = depth_limit_search(problem, depth_limit)
        if result is not None:
            return result
    return None


# Define Bidirectional Search algorithm
def bidirectional_search(problem):
    forward_frontier = deque([(problem.start, [])])
    backward_frontier = deque([(problem.goal, [])])
    forward_explored = set()
    backward_explored = set()
    while forward_frontier and backward_frontier:
        forward_state, forward_path = forward_frontier.popleft()
        backward_state, backward_path = backward_frontier.popleft()

        if forward_state in backward_explored:
            return forward_path + backward_path[::-1]
        if backward_state in forward_explored:
            return backward_path[::-1] + forward_path
        
        forward_explored.add(forward_state)
        backward_explored.add(backward_state)

        for action in problem.actions(forward_state):
            if action not in forward_explored:
                forward_frontier.append((action, forward_path + [action]))

        for action in problem.actions(backward_state):
            if action not in backward_explored:
                backward_frontier.append((action, backward_path + [action]))

# Define the problem instance
problem = Tree(tree, 'S', 'K')

# Perform BFS
bfs_path = breadth_first_search(problem)
print("BFS Path:", bfs_path)

# Perform IDS
ids_path = iterative_deepening_search(problem)
print("IDS Path:", ids_path)

# Perform Bidirectional Search
bidirectional_path = bidirectional_search(problem)
print("Bidirectional Path:", bidirectional_path)