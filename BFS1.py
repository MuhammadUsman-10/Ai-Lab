class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.mid = None
        self.right = None


def breadth_firts_search(root, goal):
    if root is None:
        return None

    queue = []
    queue.append(root)

    while queue:
        current_node = queue.pop(0)

        if current_node.data == goal:
            return current_node

        if current_node.left:
            queue.append(current_node.left)
        if current_node.mid:
            queue.append(current_node.mid)
        if current_node.right:
            queue.append(current_node.right)

    return None


# Create the tree from the diagram
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


# Find the goal state (11) using BFS
goal_node = breadth_firts_search(root, 11)

if goal_node is not None:
    print("Goal state found:", goal_node.data)
else:
    print("Goal state not found")

# Print Adjacency List
def print_adjacency_list(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while queue:
        current_node = queue.pop(0)
        print(f"Node {current_node.data} ->", end=" ")

        if current_node.left:
            print(current_node.left.data, end=" ")
            queue.append(current_node.left)
        if current_node.mid:
            print(current_node.mid.data, end=" ")
            queue.append(current_node.mid)
        if current_node.right:
            print(current_node.right.data, end=" ")
            queue.append(current_node.right)

        print()

print("\nAdjacency List:")
print_adjacency_list(root)

# Count of Vertices and Edges
def count_vertices(root):
    if root is None:
        return 0

    count = 1
    queue = []
    queue.append(root)

    while queue:
        current_node = queue.pop(0)

        if current_node.left:
            count += 1
            queue.append(current_node.left)
        if current_node.mid:
            count += 1
            queue.append(current_node.mid)
        if current_node.right:
            count += 1
            queue.append(current_node.right)

    return count

def count_edges(root):
    if root is None:
        return 0

    edges = 0
    queue = []
    queue.append(root)

    while queue:
        current_node = queue.pop(0)

        if current_node.left:
            edges += 1
            queue.append(current_node.left)
        if current_node.mid:
            edges += 1
            queue.append(current_node.mid)
        if current_node.right:
            edges += 1
            queue.append(current_node.right)

    return edges

# Check if the vertex is valid
def is_valid_vertex(vertex, root):
    if vertex < 1 or vertex > count_vertices(root):
        return False
    return True

# Count of Edges with Error Handling
def count_edges_with_error_handling(root):
    if root is None:
        return 0

    edges = 0
    queue = []
    queue.append(root)

    while queue:
        current_node = queue.pop(0)

        if current_node.left:
            edges += 1
            queue.append(current_node.left)
        if current_node.mid:
            edges += 1
            queue.append(current_node.mid)
        if current_node.right:
            edges += 1
            queue.append(current_node.right)

    return edges


print("\nCount of Vertices:", count_vertices(root))
print("Count of Edges:", count_edges_with_error_handling(root))