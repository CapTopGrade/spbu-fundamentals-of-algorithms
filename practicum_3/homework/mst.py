from typing import Any

import matplotlib.pyplot as plt
import networkx as nx

from src.plotting import plot_graph


def prim_mst(G: nx.Graph, start_node="0") -> set[tuple[Any, Any]]:
    mst_set = set()
    rest_set = set(G.nodes())
    mst_edges = set()
    heap = []

    mst_set.add(start_node)
    rest_set.remove(start_node)

    for edge in G.edges(start_node, data=True):
        heapq.heappush(heap, (edge[2]['weight'], (edge[0], edge[1])))

    while heap:
        min_edge = heapq.heappop(heap)
        min_edge_nodes = min_edge[1]
        if min_edge_nodes[0] in mst_set and min_edge_nodes[1] in mst_set:
            continue
        mst_set.update(min_edge_nodes)
        mst_edges.add(min_edge_nodes)
        for edge in G.edges(min_edge_nodes[1], data=True):
            if edge[1] not in mst_set:
                heapq.heappush(heap, (edge[2]['weight'], (edge[0], edge[1])))

    return mst_edges


if __name__ == "__main__":
    G = nx.read_edgelist("practicum_3/homework/graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    mst_edges = prim_mst(G, start_node="0")
    plot_graph(G, highlighted_edges=list(mst_edges))
