# First networkx library is imported
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt
import string




paths = ["charmander", "charizard", "charmeleon"]
G, root = nx.prefix_tree(paths)

mapping = dict(zip(G, string.ascii_lowercase))
G = nx.relabel_nodes(G, mapping)


# drawing in spectral layout
nx.draw(G, with_labels=True)

# plt.show()

plt.title('draw_networkx')
plt.savefig("filename4.png")


# drawing in spectral layout
nx.draw(g, with_labels=True)
# plt.savefig("filename4.png")
plt.savefig("test1.png")
