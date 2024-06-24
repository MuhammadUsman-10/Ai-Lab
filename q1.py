def dfs(tree, start, goal):
    stack = [(start, [start])]
    while stack:
        (node, path) = stack.pop()
        if node == goal:
            return path
        for next_node in reversed(tree[node]):
            if next_node not in path:
                stack.append((next_node, path + [next_node]))
    return None

def dls(tree, start, goal, depth_limit):
    stack = [(start, [start], 0)]
    while stack:
        (node, path, depth) = stack.pop()
        if node == goal:
            return path
        if depth < depth_limit:
            for next_node in reversed(tree[node]):
                if next_node not in path:
                    stack.append((next_node, path + [next_node], depth + 1))
    return "cutoff"

def ids(tree, start, goal, max_depth):
    for depth_limit in range(max_depth):
        result = dls(tree, start, goal, depth_limit)
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

start = 'S'
goal = 'K'

# Perform DFS
dfs_result = dfs(tree, start, goal)
print("DFS Path:", dfs_result)

# Perform DLS with depth limit 4
depth_limit = 4
dls_result = dls(tree, start, goal, depth_limit)
print("DLS Path (Depth Limit {}):".format(depth_limit), dls_result)

# Perform IDS with maximum depth 10
max_depth = 10
ids_result = ids(tree, start, goal, max_depth)
print("IDS Path (Max Depth {}):".format(max_depth), ids_result)
