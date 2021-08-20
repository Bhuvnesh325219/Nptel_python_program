

import networkx as nx
import matplotlib.pyplot as plt

g=nx.gnm_random_graph(25,1)

nx.draw(g)
plt.show()