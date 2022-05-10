import pygraphviz as pgv

G = pgv.AGraph(strict=False, directed=True)

G.add_edge("c", "h")
G.add_edge("h", "a", 1)
G.add_edge("a", "r", 1)
G.add_edge("r", "m")
G.add_edge("m", "a", 2)
G.add_edge("a", "n", 2)
G.add_edge("n", "d")
G.add_edge("d", "e")
G.add_edge("e", "r")

G = G.acyclic(copy=True)

G.layout()

G.draw("file.png")