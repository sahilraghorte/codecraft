# Function to perform Depth-First Search
def dfs(graph, vertex, visited):
    
    visited.add(vertex)
    
    print(vertex, end=' ')
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Adjacency list representation of a graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()

print("DFS Traversal starting from vertex A:")
dfs(graph, 'A', visited)
