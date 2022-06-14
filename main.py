import networkx as nx
import matplotlib.pyplot as plt

nodes = ["Python", "Java", "Programming language", "Package management"]
edges = [
    ("Python", "Programming language", {"connection": "is"}),
    ("Java", "Programming language", {"connection": "is"}),
    ("Java", "Package management", {"connection": "requires"}),
    ("Python", "Package management", {"connection": "requires"})
]

def get_data():
    graph = nx.MultiDiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph

def this_is_function():
    print("hey!")

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


if __name__ == '__main__':
    print("We're testing out graphs :)\n")

    graph = get_data()
    draw_graph(graph)

    print("\nDone! See you soon!")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
