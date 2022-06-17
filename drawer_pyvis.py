from pyvis.network import Network


def draw_graph(nodes, edges):
    net = Network()
    net.add_nodes(nodes)
    for edge in edges:
        add_edge(net, edge)
    net.show('graph-notes.html')


def add_edge(net, edge):
    net.add_edge(edge['u'], edge['v'], title=edge["title"])
