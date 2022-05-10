from cProfile import label
import pygraphviz as pgv

G = pgv.AGraph(strict=False, directed=True)

name = "charmander"
G.add_node(0, label=name[0])
for i in range(1, len(name)):
  G.add_node(i, label=name[i])
  G.add_edge(i-1, i)

G = G.acyclic(copy=True)

G.layout()

G.draw("file.png")