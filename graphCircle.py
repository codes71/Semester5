class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = [[] for _ in range(vertices)]  # Adjacency list

    def add_edge(self, v, w):
        self.graph[v].append(w)  # Add w to v’s list
        self.graph[w].append(v)  # Add v to w’s list (since undirected)

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:  # If the node hasn't been visited yet
                if self.is_cyclic_util(i, visited, v):
                    return True
            elif parent != i:  # If a node is visited and is not the parent of the current node
                return True
        return False

    def is_cyclic(self):
        visited = [False] * self.V  # Mark all the vertices as not visited
        for i in range(self.V):  # Iterate through each vertex
            if not visited[i]:  # If the vertex is not visited
                if self.is_cyclic_util(i, visited, -1):
                    return True
        return False

# Example Usage
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 4)

if g.is_cyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")
