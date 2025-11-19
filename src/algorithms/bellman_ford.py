def bellman_ford(graph, start_node):
    """
    Retorna (distances, predecessors, negative_cycle_detected)
    """
    distances = {node: float('inf') for node in graph.nodes}
    predecessors = {node: None for node in graph.nodes}
    distances[start_node] = 0
    
    for _ in range(len(graph.nodes) - 1):
        updated = False
        for u in graph.nodes:
            if distances[u] == float('inf') or u not in graph.adj_list: continue
            
            for v, weight in graph.adj_list[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u
                    updated = True
        if not updated: break
    
    negative_cycle = False
    for u in graph.nodes:
        if distances[u] == float('inf') or u not in graph.adj_list: continue
        for v, weight in graph.adj_list[u].items():
            if distances[u] + weight < distances[v]:
                negative_cycle = True
                break
                
    return distances, predecessors, negative_cycle