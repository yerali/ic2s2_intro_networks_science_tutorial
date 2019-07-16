import networkx as nx
from matplotlib import pyplot as plt

#G = nx.complete_graph(30, create_using=None)
#G = nx.watts_strogatz_graph(100, 4, 0.1, seed=None)
#nx.draw_networkx(G,pos)

G = nx.barabasi_albert_graph(500, 2, seed=None)
pos = nx.spring_layout(G)

nx.draw_networkx(G,pos,node_size=10,alpha=0.5,with_labels=False)

plt.show()
