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


if __name__ == '__main__':
    print("We're testing out graphs :)\n")

    data = get_data_from_file()
    drawer_pyvis.draw_graph(data["nodes"], data["edges"])
    write_data_to_file(data)

    print("\nDone! See you soon!")
