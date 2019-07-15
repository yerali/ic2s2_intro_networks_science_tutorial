import matplotlib.pyplot as plt
import networkx as nx
#import numpy as np

#1. We read the data
fh=open("small_network.txt", 'rb')

#G=nx.read_edgelist(fh,create_using=nx.DiGraph())
G=nx.read_edgelist(fh)
fh.close()

#2. We print the nodes, the edges and the adjacency matrix
print G.nodes
print G.edges

A= nx.adjacency_matrix(G, nodelist=None)
print(A.todense())

#3. Finally, we plot the netwok

pos = nx.spring_layout(G)
nx.draw_networkx(G,pos,node_size=70,alpha=0.5,with_labels=True)

plt.show()
