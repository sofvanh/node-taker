import drawer_pyvis
import json

nodes = ["Python", "Java", "Programming language", "Package management"]
edges = [
    ("Python", "Programming language", {"title": "Python is a programming language"}),
    ("Java", "Programming language", {"title": "Java is a programming language"}),
    ("Java", "Package management", {"title": "Java requires package management"}),
    ("Python", "Package management", {"title": "Python requires package management"})
]

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


if __name__ == '__main__':
    print("We're testing out graphs :)\n")

    data = get_data_from_file()
    drawer_pyvis.draw_graph(data["nodes"], data["edges"])
    write_data_to_file(data)

    print("\nDone! See you soon!")
