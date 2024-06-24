class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.mid = None
        self.right = None

def dfs(node, goal, path=[], visited_order=[]):
    if node is None:
        return False
    
    print(f"Visiting Node {node.value}")

    # Add the current node to the path
    path.append(node.value)
    visited_order.append(node.value)

    if node.value == goal:
        print("Goal state found!", goal)
        print("Path To Goal", path)
        return True, visited_order
    
    left = dfs(node.left, goal, path)
    mid = dfs(node.mid, goal, path)
    right = dfs(node.right, goal, path)

    # Remove the current node from the path (backtrack)
    path.pop()
    
    return left or mid or right

# Creating the binary tree
root = Node(1)
root.left = Node(2)
root.mid = Node(3)
root.right = Node(4)
root.left.left = Node(5)
root.left.right = Node(6)
root.right.left = Node(7)
root.right.right = Node(8)
root.left.left.left = Node(9)
root.left.left.right = Node(10)
root.right.left.left = Node(11)
root.right.left.right = Node(12)

# Calling DFS to find node with value 3 and 12
goal_state=3
found, visited_order = dfs(root, goal_state, [], [])
if not found:
    print("Goal state not found")
else:
    print("\nVisited Order", visited_order)




# Code For Deliverable 2 Conneced Components 
# I've Commented This code because it is separate from the main code

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.mid = None
#         self.right = None

# def dfs(node, visited, component):
#     if node is None:
#         return

#     visited[node.value] = True
#     component.append(node.value)
    
#     if node.left and not visited[node.left.value]:
#         dfs(node.left, visited, component)
#     if node.mid and not visited[node.mid.value]:
#         dfs(node.mid, visited, component)
#     if node.right and not visited[node.right.value]:
#         dfs(node.right, visited, component)

# def find_connected_components(root):
#     visited = {node.value: False for node in root}  # Mark all vertices as not visited
#     components = []

#     if not visited[root.value]:
#         component = []
#         dfs(root, visited, component)
#         components.append(component)

#     return components

# # Creating the binary tree
# root = Node(1)
# root.left = Node(2)
# root.mid = Node(3)
# root.right = Node(4)
# root.left.left = Node(5)
# root.left.right = Node(6)
# root.right.left = Node(7)
# root.right.right = Node(8)
# root.left.left.left = Node(9)
# root.left.left.right = Node(10)
# root.right.left.left = Node(11)
# root.right.left.right = Node(12)

# # Find and print all connected components
# connected_components = find_connected_components(root)
# for i, component in enumerate(connected_components, start=1):
#     print(f"Connected Component {i}: {component}")

