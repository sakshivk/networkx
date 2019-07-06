# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:24:44 2019

@author: ME
"""

import networkx as nx
from networkx.algorithms import tree
import matplotlib.pyplot as plt
G=nx.Graph()
node_list=['B','C','D','E','F']
G.add_nodes_from(node_list)
G.add_edge('B','C',weight=2)
G.add_edge('B','F',weight=4)
G.add_edge('C','D',weight=4)
G.add_edge('C','E',weight=1)
G.add_edge('D','E',weight=2)
G.add_edge('B','E',weight=1)
G.add_edge('F','E',weight=5)
pos = nx.circular_layout(G)
labels = nx.get_edge_attributes(G,'weight')
print("----------------------------------Output MST----------------------------------")
print("Nodes of the Graph:",G.nodes())
print("Edges of the Graph:",G.edges())
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
nx.draw(G,pos,with_labels=True, node_color='y')
plt.savefig("Problem_graph2.png")#save as png
plt.show()
#KRUSKAL ALGORITHM
print("*********************************************************************")
print("The Solution using Kruskal Algorithm is shown:")
h=nx.Graph()
final= tree.minimum_spanning_edges(G, algorithm='kruskal', data=True)
edgelist = list(final)
print(sorted(edgelist))
h.add_edges_from(sorted(edgelist))
nx.draw_networkx_edge_labels(h,pos,edge_labels=labels)
nx.draw(h,pos,with_labels=True, node_color='b')
plt.savefig("kruskal.png")#save as png
plt.show() 
#PRIMS ALGORITHM
print("*********************************************************************")
print("The Solution using Prims Algorithm is shown:")
j=nx.Graph()
final2= tree.minimum_spanning_edges(G, algorithm='prim', data=True)
edgelist2 = list(final2)
print(sorted(edgelist2))
j.add_edges_from(sorted(edgelist2))
nx.draw_networkx_edge_labels(j,pos,edge_labels=labels)
nx.draw(j,pos,with_labels=True, node_color='g')
plt.savefig("Prims.png")#save as png
plt.show()
