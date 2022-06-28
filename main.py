from helpers import drawer_pyvis, file_helper

# TODO add tracking of how the graph has grown over time


data_file_path = "data/data.json"


def add_node(data, name):
    data["nodes"].append(name)


def add_edge(data, edge):
    # TODO ensure edge is valid (both nodes exist)
    data["edges"].append(edge)


if __name__ == '__main__':
    print("Welcome to your knowledge graph <3")
    print("Commands: 'n' for new node, 'e' for new edge, 'l' for load visuals, 's' for save & exit")

    data = file_helper.get_data_from_file(data_file_path)
    drawer_pyvis.draw_graph(data["nodes"], data["edges"])

    i = ''

    while i != 'q':
        i = input("Enter command:")
        if i == 'n':
            name = input("Name of new node:")
            add_node(data, name)
        elif i == 'e':
            u = input("Name of first node:")
            v = input("Name of second node:")
            title = input("Title for the edge:")
            edge = {"u": u, "v": v, "title": title}
            add_edge(data, edge)
        elif i == 'l':
            drawer_pyvis.draw_graph(data["nodes"], data["edges"])
        elif i == 's':
            break
        else:
            print("Sorry, I didn't understand :( Try 'n' for new node, 'e' for new edge, or 's' for save & exit.")

    file_helper.write_data_to_file(data_file_path, data)
    print("Done! See you soon!")
