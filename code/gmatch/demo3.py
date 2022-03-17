import networkx as nx
import gmatch4py as gm
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
        (10, {'nombre':'I1'})]


enlacesG = [(3,1), (4,2), (5,2), (6,1), (6,4), (6,5), (7,4), (8,2), (9,5), \
(9,4), (10,5), (10,6)]

G = nx.Graph()
G.add_nodes_from(nodosG)
G.add_edges_from(enlacesG)

# sistemas 2009 model 1 (relaciones originales acm68)
nodosH = [(2, {'nombre':'M1'}),
        (5, {'nombre':'M2'}),
        (3, {'nombre':'B2'}),
        (1, {'nombre':'B1'}),
        (9, {'nombre':'M4'}),
        (4, {'nombre':'M3'}),
        (10, {'nombre':'I1'}),
        (6, {'nombre':'B3'}),
        (7, {'nombre':'B4'}),
        (8, {'nombre':'M2P'})]

enlacesH = [(9,5),
        (9,4),
        (4,2),
        (10,3),
        (10,6),
        (6,1),
        (8,2),
        (7,1),
        (7,5),
        (7,4)]

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

mcs = getMCS(H,G)
print((mcs.node), len(mcs.node))
print(mcs.edges, len(mcs.edges))
print("edit distance desde algoritmo local:")
num_node = len(mcs.node)
print("MCS ged:")
ged = getGED(num_node, len(H.node), len(G.node))
print(ged)
print("similaridad desde algoritmo local:")
print(1-ged)

gt1 = gm.MCS()
result2 = gt1.compare([H, G], None)
ged1=gm.GraphEditDistance(1,1,1,1)
out1 = ged1.distance(result2)
print("edit distance desde algoritmo gmatch4py:")
print("MCS ged:")
print(out1)
print("similaridad desde algoritmo gmatch4py:")
out2 = ged1.similarity(result2)
print(out2)


