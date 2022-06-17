import drawer_pyvis

nodes = ["Python", "Java", "Programming language", "Package management"]
edges = [
    ("Python", "Programming language", {"title": "Python is a programming language"}),
    ("Java", "Programming language", {"title": "Java is a programming language"}),
    ("Java", "Package management", {"title": "Java requires package management"}),
    ("Python", "Package management", {"title": "Python requires package management"})
]

if __name__ == '__main__':
    print("We're testing out graphs :)\n")

    #graph = get_data()
    #draw_with_pyvis(graph)
    #draw_graph(graph)

    drawer_pyvis.draw_graph(nodes, edges)

    print("\nDone! See you soon!")
