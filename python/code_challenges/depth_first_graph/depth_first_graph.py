from code_challenges.graphs.graphs import Graph, Vertex
def depth_traversal(node, graph):
    visited = set()
    stack = Stack()
    nodes = []
    stack.push(node)
    while stack.top:
        current = stack.pop()
        nodes.append(current)
        neighbors = graph.get_neighbors(current)
        if neighbors:
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.push(neighbor)
                    visited.add(neighbor)
    # breakpoint()
    return nodes
