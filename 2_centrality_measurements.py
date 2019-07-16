import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import math

#1. We read the data
fh=open("small_network.txt", 'rb')

G=nx.read_edgelist(fh)
fh.close()

#2. We calculate some centralities
bet=nx.betweenness_centrality(G)
#clos=nx.closeness_centrality(G)
#deg=nx.degree_centrality(G)

#3. We print the output
print bet
#print clos
#print deg

#3. What about directness?
#G=nx.read_edgelist(fh,create_using=nx.DiGraph())
#fh.close()
#bet=nx.betweenness_centrality(G)
#print bet
