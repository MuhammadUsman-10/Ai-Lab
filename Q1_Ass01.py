def depth_first_search(tree, initial_state, goal_state):
    stack = [(initial_state, [initial_state])]
    while stack:
        (node, path) = stack.pop()
        if node == goal_state:
            return path
        for next_node in reversed(tree[node]):
            if next_node not in path:
                stack.append((next_node, path + [next_node]))
    return None

def depth_limit_search(tree, initial_state, goal_state, depth_limit):
    stack = [(initial_state, [initial_state], 0)]
    while stack:
        (node, path, depth) = stack.pop()
        if node == goal_state:
            return path
        if depth < depth_limit:
            for next_node in reversed(tree[node]):
                if next_node not in path:
                    stack.append((next_node, path + [next_node], depth + 1))
    return "cutoff"

def iterative_deepening_search(tree, initial_state, goal_state, max_depth):
    for depth_limit in range(max_depth):
        result = depth_limit_search(tree, initial_state, goal_state, depth_limit)
        if result != "cutoff":
            return result
    return None

# Define the tree
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

initial_state= 'S'
goal_state = 'K'

# Perform DFS
dfs_result = depth_first_search(tree, initial_state, goal_state)
print("DFS Path:", dfs_result)

# Perform DLS with depth limit 4
depth_limit = 4
dls_result = depth_limit_search(tree, initial_state, goal_state, depth_limit)
print("DLS Path (Depth Limit {}):".format(depth_limit), dls_result)

# Perform IDS with maximum depth 10
max_depth = 10
ids_result = iterative_deepening_search(tree, initial_state, goal_state, max_depth)
print("IDS Path (Max Depth {}):".format(max_depth), ids_result)