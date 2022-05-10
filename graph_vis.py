# First networkx library is imported
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt


g = nx.Graph()

# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.add_edge(3, 4)
# g.add_edge(1, 4)
# g.add_edge(1, 5)
# g.add_edge(5, 6)
# g.add_edge(5, 7)
# g.add_edge(4, 8)
# g.add_edge(3, 8)

g.add_edge('c', 'h')
g.add_edge('h', 'a')
g.add_edge('a', 'r')
g.add_edge('r', 'm')
g.add_edge('m', 'a')
g.add_edge('a', 'n')


# drawing in spectral layout
nx.draw(g, with_labels=True)
# plt.savefig("filename4.png")
plt.savefig("test1.png")
