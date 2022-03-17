import networkx as nx
import gmatch4py as gm
import math
# model acm68 
nodosG = [(1, {'nombre':'B1'}),
        (2, {'nombre':'M1'}),
        (3, {'nombre':'B2'}),
        (4, {'nombre':'M3'}),
        (5, {'nombre':'M2'}),
        (6, {'nombre':'B3'}),
        (7, {'nombre':'B4'}),
        (8, {'nombre':'M2P'}),
        (9, {'nombre':'M4'}),
        (10, {'nombre':'I1'}),
        (11, {'nombre':'I2'}),
        (12, {'nombre':'I3'}),
        (13, {'nombre':'M7'}),
        (14, {'nombre':'M5'}),
        (15, {'nombre':'I4'}),
        (16, {'nombre':'I6'}),
        (17, {'nombre':'I7'}),
        (18, {'nombre':'A1'}),
        (19, {'nombre':'A4'}),
        (20, {'nombre':'A5'}),
        (21, {'nombre':'A6'}),
        (22, {'nombre':'A7'}),
        (23, {'nombre':'A8'}),
        (24, {'nombre':'A9'}),
        (25, {'nombre':'I8'}),
        (26, {'nombre':'I9'}),
        (27, {'nombre':'A2'}),
        (28, {'nombre':'A3'})]


enlacesG = [(3,1), (4,2), (5,2), (6,1), (6,4), (6,5), (7,4), (8,2), (9,5), \
(9,4), (10,5), (10,6), (11,3), (11,6), (12,3), (13,8), (14,8), (15,10), (15,11), \
(16,12), (16,6), (17,6), (18,10), (18,11), (19,13), (19,14), (19,9), (21,9), \
(22,6), (22,17), (23,19), (24,9), (25,9), (26,9), (27, 12), (28,6), (28,11)]
G = nx.Graph()
G.add_nodes_from(nodosG)
G.add_edges_from(enlacesG)

# sistemas 2009 model 1 (relaciones originales acm68)
nodosH = [(2, {'nombre':'M1'}),
        (5, {'nombre':'M2'}),
        (3, {'nombre':'B2'}),
        (1, {'nombre':'B1'}),
        (11, {'nombre':'I2'}),
        (9, {'nombre':'M4'}),
        (4, {'nombre':'M3'}),
        (10, {'nombre':'I1'}),
        (22, {'nombre':'A7'}),
        (6, {'nombre':'B3'}),
        (8, {'nombre':'M2P'}),
        (21, {'nombre':'A6'}),
        (14, {'nombre':'M5'}),
        (16, {'nombre':'I6'}),
        (13, {'nombre':'M7'}),
        (20, {'nombre':'A5'}),
        (7, {'nombre':'B4'}),
        (18, {'nombre':'A1'}),
        (17, {'nombre':'I7'}),
        (12, {'nombre':'I3'}),
        (15, {'nombre':'I4'}),
        (24, {'nombre':'A9'}),
        (19, {'nombre':'A4'}),
        (23, {'nombre':'A8'}),
        (25, {'nombre':'A2'})
]

enlacesH = [(11,3),
        (11,8),
        (9,5),
        (9,4),
        (4,2),
        (10,3),
        (10,6),
        (22,6),
        (22,17),
        (6,1),
        (8,2),
        (21,10),
        (14,9),
        (16,6),
        (16,12),
        (13,8),
        (20,10),
        (7,1),
        (7,5),
        (7,4),
        (18,10),
        (18,11),
        (17,6),
        (17,16),
        (12,3),
        (12,8),
        (15,10),
        (15,11),
        (15,12),
        (24,10),
        (19,15),
        (19,13),
        (23, 19),
        (25,12)]

H = nx.Graph()
H.add_nodes_from(nodosH)
H.add_edges_from(enlacesH)

def getMCS(g1, g2):
    matching_graph = nx.Graph()
    for n1, n2 in g2.edges():
        if g1.has_edge(n1,n2):
            matching_graph.add_edge(n1,n2)
    components = nx.connected_components(matching_graph)
    largest_component = max(components, key=len)    
    #return nx.induced_subgraph(matching_graph, largest_component)
    return nx.subgraph(matching_graph, largest_component)

def getGED(num_mcs, numg1, numg2):
        return 1 - (abs(num_mcs) / max(abs(numg1), abs(numg2)))

# Resultado del grafo MCS entre H y G
print("Modelo 1: Subgrafo MCS entre H y G")
mcs = getMCS(H,G)
num_node = len(mcs.node)
print((mcs.node))
print(mcs.edges)
print(getGED(num_node, len(H.node), len(G.node)))

ged1=gm.GraphEditDistance(1,1,1,1) # all edit costs are equal to 1
result1=ged1.compare([H, G],None)
print("Distancia sin normalizar:")
print(result1)
gt1 = gm.MCS()
result2 = gt1.compare([H, G], None)
out1 = ged1.distance(result2)
print("resultado de MCS de H (sistemas 2009) subgrafo con G acm68:")
print(out1)

print("similaridad")
out1 = ged1.similarity(result2)
print(out1)

# sistemas 2009 model 2 (relaciones originales de la carrera)

G = nx.Graph()
G.add_nodes_from(nodosG)
G.add_edges_from(enlacesG)

T = nx.Graph()
T.add_nodes_from(nodosH)

enlacesT = [(11,3),
        (9,5),
        (4,2),
        (10,3),
        (22,10),
        (6,4),
        (8,9),
        (12,22),
        (14,9),
        (13,8),
        (7,14),
        (18,22),
        (18,6),
        (17,16),
        (12,17),
        (15,18),
        (24,12),
        (24,15),
        (25,23)]
T.add_edges_from(enlacesT)
# Resultado del grafo MCS entre T y G
print("Modelo 1: Subgrafo MCS entre T y G")
mcs = getMCS(T,G)
print((mcs.node))
print(mcs.edges)

print("Modelo 2")

ged2=gm.GraphEditDistance(1,1,1,1) # all edit costs are equal to 1
result3=ged2.compare([T, G],None)
print("Distancia sin normalizar:")
print(result3)

gt2 = gm.MCS()
result4 = gt2.compare([T, G], None)
out2 = ged2.distance(result4)
print("resultado de MCS de T (sistemas 2009) relaciones originales con subgrafo con G acm68:")
print(out2)
print("similaridad")
out2 = ged2.similarity(result4)
print(out2)

