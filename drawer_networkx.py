import networkx as nx
import matplotlib.pyplot as plt


# Deprecated

def get_data(nodes, edges):
    graph = nx.MultiDiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


def draw_graph(graph):
    edges = [(u, v) for (u, v, d) in graph.edges(data=True)]
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, node_size=700)
    nx.draw_networkx_edges(graph, pos, edgelist=edges, width=1)
    # node labels
    nx.draw_networkx_labels(graph, pos, font_size=6, font_family="sans-serif")

    edge_labels = dict([((u, v,), d["connection"])
                        for u, v, d in graph.edges(data=True)])
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, label_pos=0.3, font_size=7)

    plt.show()
