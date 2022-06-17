import drawer_pyvis
import json


def get_data_from_file():
    f = open("data.json", "r")
    d = f.read()
    f.close()
    return json.loads(d)


def write_data_to_file(data):
    f = open("data.json", "w")
    s = json.dumps(data, indent=2, sort_keys=True)
    f.write(s)
    f.close()


def add_node(data, name):
    data["nodes"].append(name)


def add_edge(data, edge):
    # TODO ensure edge is valid (both nodes exist)
    data["edges"].append(edge)


if __name__ == '__main__':
    print("Welcome to your knowledge graph <3")
    print("Commands: 'n' for new node, 'e' for new edge, 's' for save & exit")

    data = get_data_from_file()
    drawer_pyvis.draw_graph(data["nodes"], data["edges"])

    i = input("Enter command:")

    while i != 'q':
        if i == 'n':
            name = input("Name of new node:")
            add_node(data, name)
            drawer_pyvis.draw_graph(data["nodes"], data["edges"])
        elif i == 'e':
            u = input("Name of first node:")
            v = input("Name of second node:")
            title = input("Title for the edge:")
            edge = {"u": u, "v": v, "title": title}
            add_edge(data, edge)
            drawer_pyvis.draw_graph(data["nodes"], data["edges"])
        elif i == 's':
            break
        else:
            print("Sorry, I didn't understand :( Try 'n' for new node, 'e' for new edge, or 's' for save & exit.")

        i = input("Enter command:")

    write_data_to_file(data)
    print("Done! See you soon!")
