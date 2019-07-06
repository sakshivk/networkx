# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:34:27 2019

@author: SAKSHI SHARMA<imsakshivk@gmail.com, sakshi.cse18@nitttrchd.ac.in>
"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
G=nx.Graph()
node_list=['A','B','C','D','E','F']
G.add_nodes_from(node_list)
G.add_edge('A','B',weight=6)
G.add_edge('A','F',weight=3)
G.add_edge('B','C',weight=2)
G.add_edge('B','F',weight=4)
G.add_edge('C','D',weight=4)
G.add_edge('C','E',weight=1)
G.add_edge('D','E',weight=2)
G.add_edge('B','E',weight=1)
G.add_edge('F','E',weight=5)
pos = nx.circular_layout(G)
labels = nx.get_edge_attributes(G,'weight')
print("Nodes of the Graph:",G.nodes())
print("Edges of the Graph:",G.edges())
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
nx.draw(G,pos,with_labels=True, node_color='r')
plt.savefig("Problem_graph.png")#save as png
plt.show()
print("*********************************************************************")
#DIJKSTRA ALGORITM
print("The Solution using Dijkstra Algorithm is shown:")
final= nx.dijkstra_path(G, 'A','D')
print(final,type(final))
h = G.subgraph(final)
plt.figure("Solution Graph")
labels_d = nx.get_edge_attributes(h,'weight')
nx.draw_networkx_edge_labels(h,pos,edge_labels=labels_d)
nx.draw(h,pos,with_labels=True, node_color='b')
plt.savefig("dijkstra.png")#save as png
plt.show() 
total_weight_d=np.sum(labels_d)
print("Nodes of the Graph with shortest path using Dijkstra: ",h.nodes())
print("Edges of the Graph with shortest path using Dijkstra: ",h.edges())
print("Total Weight of shortest path :",total_weight_d)
p_l_d=nx.dijkstra_path_length(h,'A','D')
print("Path Length using Dijkstra From A to D :",p_l_d)
print("*********************************************************************")
#BELLMAN FORD ALGORITHM
print("The Solution using Bellman Ford Algorithm is shown:")
final2= nx.bellman_ford_path(G, 'A','D')
print(final2,type(final2))
j=G.subgraph(final2)
plt.figure("Solution Graph 2")
labels_b = nx.get_edge_attributes(j,'weight')
nx.draw_networkx_edge_labels(j,pos,edge_labels=labels_b)
nx.draw(j,pos,with_labels=True, node_color='g')
plt.savefig("bellman.png")# save as png
plt.show()
total_weight_b=np.sum(labels_b)
print("Nodes of the Graph with shortest path using Bellman Ford: ",j.nodes())
print("Edges of the Graph with shortest path using Bellman Ford: ",j.edges())
print("Total Weight of shortest path :",total_weight_b)
p_l_b=nx.bellman_ford_path_length(j,'A','D')
print("Path Length using Bellman Ford From A to D :",p_l_b)