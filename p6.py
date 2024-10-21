from collections import defaultdict

def find_critical_connections(n, connections):
    def dfs(node, parent, discovery_time, low, graph, time, bridges):
        discovery_time[node] = low[node] = time[0]
        time[0] += 1

        for neighbor in graph[node]:
            if discovery_time[neighbor] == -1:  # not visited
                dfs(neighbor, node, discovery_time, low, graph, time, bridges)
                low[node] = min(low[node], low[neighbor])

                if low[neighbor] > discovery_time[node]:
                    bridges.append([node, neighbor])
            elif neighbor != parent:
                low[node] = min(low[node], discovery_time[neighbor])

    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    discovery_time = [-1] * n
    low = [-1] * n
    bridges = []
    time = [0]

    for i in range(n):
        if discovery_time[i] == -1:
            dfs(i, -1, discovery_time, low, graph, time, bridges)

    return bridges

# Example usage
n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
print(find_critical_connections(n, connections))
