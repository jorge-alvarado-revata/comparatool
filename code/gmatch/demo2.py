import networkx as nx
import gmatch4py as gm #validado solo para obtener la distancia de isomorfismo
# Prueba de networkx
from  networkx.algorithms import matching
from networkx.algorithms import isomorphism
from  networkx.algorithms import similarity
import matplotlib.pyplot as plt

"""
1. Testeo de networkx para encontrar subgraph isomorphism o similaridad o matching
La idea es identificar la lista de subgrafos comunes por ello no se descarta 
implementar el algoritmo de mcGregor modificado para que sean conectados o usar
otra alternativa basada en clique pero que se encuentre implementada en esta libreria.

2. La otra opción es usar la libreria graph-tool.skewed.de con el modulo topology

"""



nodosG = [1, 2, 3, 4, 5, 6, 7]
nodosH = [1, 2, 3, 4, 5]

enlacesG = [(1,2), (1,3), (1,5), (1,4), (4,7), (3,6), (5,6)]
enlacesH = [(1,2), (1,3), (1,5), (3,4)]

G = nx.Graph()
G.add_nodes_from(nodosG)
G.add_edges_from(enlacesG)


H = nx.Graph()
H.add_nodes_from(nodosH)
H.add_edges_from(enlacesH)


ged=gm.GraphEditDistance(1,1,1,1)
result1=ged.compare([H,G],None)
out1 = ged.distance(result1)

print(out1)
gt = gm.MCS()
result2 = gt.compare([H,G], None)

out2 = ged.distance(result2)
print(out2)


# funcion devuelve el Maximo comun subgrafo
def getMCS(g1, g2):
    matching_graph = nx.Graph()
    for n1, n2 in g2.edges():
        if g1.has_edge(n1,n2):
            matching_graph.add_edge(n1,n2)
    components = nx.connected_components(matching_graph)
    largest_component = max(components, key=len)    
    #return nx.induced_subgraph(matching_graph, largest_component)
    return nx.subgraph(matching_graph, largest_component)

def distance(num_mcs, numg1, numg2):
        return 1 - (abs(num_mcs) / max(abs(numg1), abs(numg2)))

mcs = getMCS(H,G)
print("mcs:")
print(mcs.nodes)
print(mcs.edges)
num_node = len(mcs.nodes)
print("MCS distance:")
ged = distance(num_node, len(H.nodes), len(G.nodes))
print(ged)

nx.draw(G, with_labels = True)
plt.savefig('G.png')
plt.clf()
nx.draw(H, with_labels = True)
plt.savefig('H.png')
plt.clf()
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='yellow')
nx.draw_networkx_nodes(mcs, pos, node_color='green')
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edge_color='blue', width=0.5)
nx.draw_networkx_edges(G, pos, edgelist=mcs.edges, edge_color='red', width=2)
plt.savefig('H_G.png')

