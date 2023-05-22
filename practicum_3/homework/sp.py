from typing import Any

import networkx as nx

from src.plotting import plot_graph


def dijkstra_sp(G: nx.Graph, source_node="0") -> dict[Any, list[Any]]:
    shortest_paths = {}
    heap = [(0, source_node, [])]  # priority queue of (distance, node, path)

    while heap:
        (dist, node, path) = heapq.heappop(heap)
        if node not in shortest_paths:
            shortest_paths[node] = path + [node]
            for next_node, edge_data in G[node].items():
                distance = edge_data['weight']
                heapq.heappush(heap, (dist + distance, next_node, shortest_paths[node]))

    return shortest_paths


if __name__ == "__main__":
    G = nx.read_edgelist("practicum_3/homework/graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    shortest_paths = dijkstra_sp(G, source_node="0")
    test_node = "5"
    shortest_path_edges = [
        (shortest_paths[test_node][i], shortest_paths[test_node][i + 1])
        for i in range(len(shortest_paths[test_node]) - 1)
    ]
    plot_graph(G, highlighted_edges=shortest_path_edges)
