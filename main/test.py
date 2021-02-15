import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3)])
print(list(G.nodes))
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()