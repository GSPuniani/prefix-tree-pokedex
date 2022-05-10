from cProfile import label
import pygraphviz as pgv

G = pgv.AGraph(strict=False, directed=True)

names = ["charmander", "charizard"]
for name in names:
  if G.has_node(name[0]):
    G.add_node(name[0], label=name[0])
  for i in range(1, len(name)):
    G.add_node(i, label=name[i])
    G.add_edge(i-1, i)

G = G.acyclic(copy=True)

G.layout()

G.draw("file.png")