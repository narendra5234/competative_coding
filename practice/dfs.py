def dfs_recursive(graph, vertex, path=None):
    if path is None:
        path = []
    path += [vertex]

    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)
    return path


adjacency_matrix = {2: [9], 7: [2, 9], 9: [5], 5: []}

print(dfs_recursive(adjacency_matrix, 7))
