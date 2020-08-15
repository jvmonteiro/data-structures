from collections import deque

# Finds all nodes.
def dfs(graph):
    pre = deque()
    post = deque()
    parent = {}

    # For every unvisited vertex in the graph
    for vertex in graph:
        if not (vertex in visited):
            # Run a DFS from this vertex
            run_dfs(graph, vertex, pre, post, parent)
    
    # Return preorder and postorder trees and parent dict
    return (pre, post, parent)


def run_dfs(graph, vertex, visited, pre, post, parent):
    # Add this node to preorder tree
    pre.append(vertex)

    # For every unvisited neighbor
    for v in graph[vertex]:
        if not (v in pre):
            # Make the current node be the parent of the next neighbor 
            parent[v] = vertex
            # Continue DFS from the current neighbor
            run_dfs(graph, v, pre, post, parent)
    # No more neighbors, add this node to postorder stack
    post.append(vertex)

# Only finds nodes that are reachable from 'vertex'
def bfs(graph, vertex):
    visited = deque()
    neighbors = deque()
    parent = {}

    # Add vertex to queue
    neighbors.append(vertex)
    # Make it the root of the span tree
    parent[vertex] = vertex    
    # While queue has vertexes
    while len(neighbors) > 0:
        # Get one vertex from the list
        neighbor = neighbors.popleft()
        # Mark it as visited
        visited.append(neighbor)
        # For every unvisited neighbor of this vertex
        for v in graph[neighbor]:
            if not (v in visited or v in neighbors):
                # Make the current vertex be this neighbor's parent
                parent[v] = neighbor
                # Add the neighbor to the queue to be explored
                neighbors.append(v)
    # No more neighbors, add this node to postorder stack       
    return (parent, visited)

def check_cycle_undirected(graph):
    pre = deque()
    parent = {}    
    # For every unvisited node in the graph
    for v in graph:
        if not (v in pre):
            parent[v] = v
            # Return true if this node has a cycle
            if (run_check_cycle_undirected(graph, v, pre, parent)):
                return True
    # Didn't return true until now, doesn't have cycles.
    return False

def run_check_cycle_undirected(graph, vertex, pre, parent):
    # Mark as visited.
    pre.append(vertex)
    
    # For every unvisited neighbor
    for v in graph[vertex]:
        if not (v in pre):
            parent[v] = vertex
            # If it has cycles, return true
            if (run_check_cycle_undirected(graph, v, pre, parent)):
                return True
        # If this neighbor has been visited but its not my parent, it was reached
        # from another node, making it a cycle.
        elif parent[vertex] != v:
            return True
    return False

def check_dag(graph, vertex, pre, post):
    pre = deque()
    post = deque()  
    # For every unvisited node in the graph
    for v in graph:
        if not (v in pre):
            pre.append(v)
            # Return true if this node is a DAG
            if (run_check_dag(graph, v, pre, post)):
                return True
    # Didn't return true until now, isn't a DAG
    return False

def run_check_dag(graph, vertex, pre, post):
    # Mark as visited.
    pre.append(vertex)
    # For every unvisited neighbor
    for v in graph[vertex]:
        if not (v in pre):
            # If it has cycles, return true
            if (run_check_dag(graph, v, pre, post)):
                return True
        # If this neighbor has been visited hasn't finished exploring, it was reached
        # from another node, so the graph can't be a DAG.
        elif not (v in post):
            return True
    post.append(vertex)
    return False

# c(1, [], [], {1:1})
# c(2, [1], [], {1: 1, 2: 1})
# c(4, [1,2], )
# c(3, [1,2,4], 4)
# c()