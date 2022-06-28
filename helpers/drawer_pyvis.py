from pyvis.network import Network
import file_helper


def draw_graph(nodes, edges):
    net = Network(height='700px', width='11x00px')
    net.add_nodes(nodes)
    for edge in edges:
        add_edge(net, edge)
    net.set_options(options=file_helper.get_raw_string_from_file("../options.json"))
    net.show('graph-notes.html')


def add_edge(net, edge):
    title = edge["title"]
    net.add_edge(edge['u'], edge['v'], title=title, value=len(title))
