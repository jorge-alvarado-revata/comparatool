import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from  networkx.algorithms import matching
from networkx.algorithms import similarity
import gmatch4py as gm
from icecream import ic


# funcion devuelve el Maximo comun subgrafo


# Obtiene el maximo común subgrafo componente conectado
def getMCS(g1, g2):
    matching_graph = nx.Graph()
    for n1, n2 in g2.edges():
        if g1.has_edge(n1,n2):
            matching_graph.add_edge(n1,n2)
    components = nx.connected_components(matching_graph)
    largest_component = max(components, key=len)    
    #return nx.induced_subgraph(matching_graph, largest_component)
    return nx.subgraph(matching_graph, largest_component)

#Obtiene el grafo con los nodos y enlaces comunes a ambos g1, g2
def getCS(g1,g2):
    T = nx.Graph()
    for x,y in g2.edges():
        if g1.has_edge(x,y):
            T.add_edge(x,y)
    return T

# Obtiene la distancia considerando 
# los numeros del maximo comun subgrafo conectado
def distance(num_mcs, numg1, numg2):
        return 1 - (abs(num_mcs) / max(abs(numg1), abs(numg2)))

def get_data(df):
    data = []
    for pos in range(len(df)): 
        dic_names = {}
        dic_names['nombre'] = str(df['nombre'][pos])
        tupla = (df['id'][pos], dic_names)
        data.append(tupla)
    return data

def getNodes(f_name):
    df1 = pd.read_csv(f_name)
    df1_data = df1[['id','nombre']]
    data = get_data(df1_data)
    return data

def getEnlaces(f_name):
    df2 = pd.read_csv(f_name)
    enlaces = df2.to_records(index=False)
    return enlaces

def getLabels(f_name):
    df1 = pd.read_csv(f_name)
    df1_data = df1[['id','nombre']]
    #dic_label = {(k+1):v for (k,v) in df1_data.id.items()}
    dic_label = {df1_data['id'][x]:df1_data['id'][x] for x in range(len(df1_data))}

    return dic_label
# dibuja el grafo dado S, si mcs pinta el mcs de otro color
def draw_graph(S, f_outname, f_inname, mcs=None):
    pos = nx.shell_layout(S)
    #pos = nx.spring_layout(S)
    d_labels = getLabels(f_inname)
    ic(d_labels)
    nx.draw_networkx_labels(S, pos, labels=d_labels)
    nx.draw_networkx_nodes(S, pos, node_color='yellow')
    if mcs: nx.draw_networkx_nodes(S,pos, mcs.nodes, node_color='green')

    nx.draw_networkx_edges(S, pos, edge_color='blue', width=0.5)
    if mcs: nx.draw_networkx_edges(S, pos, edgelist=mcs.edges, edge_color='red', width=2)
    plt.savefig(f_outname)
    plt.clf()

# dibuja el grafo H y mcs, si viene G, pinta enlaces comunes a ambos
def draw_mix_graph(H, f_outname, f_inname, mcs=None, G=None):
    pos = nx.shell_layout(H)
    #pos = nx.spring_layout(H)
    d_labels = getLabels(f_inname)
    nx.draw_networkx_labels(H, pos, labels=d_labels)
    nx.draw_networkx_nodes(H, pos, node_color='yellow')
    if mcs: nx.draw_networkx_nodes(H,pos, mcs.nodes, node_color='green')

    nx.draw_networkx_edges(H, pos, edge_color='blue', width=0.5)
    if G: 
        listaenlace = [(x,y) for x,y in H.edges() if G.has_edge(x,y)]
        nx.draw_networkx_edges(H, pos, edgelist=listaenlace, edge_color='orange', width=1)
    if mcs: nx.draw_networkx_edges(H, pos, edgelist=mcs.edges, edge_color='red', width=2)
    plt.savefig(f_outname)
    plt.clf()

 # Crea un nodo y enlaces con nombres de archivos 
def factory_graph(f_node, f_enlaces):
    G = nx.Graph()
    data = getNodes(f_node)
    G.add_nodes_from(data)
    enlaces = getEnlaces(f_enlaces)
    G.add_edges_from(enlaces)
    return G

def compara(G, H, des1, des2):

    print("Modelo 1")
    ged1=gm.GraphEditDistance(1,1,1,1) # all edit costs are equal to 1
    result1=ged1.compare([G, H],None)
    print("Distancia sin normalizar:")
    print(result1)
    gt1 = gm.MCS()
    result2 = gt1.compare([G, H], None)
    out1 = ged1.distance(result2)
    print(f"resultado de MCS de H ({des1}) subgrafo con G ({des2}):")
    print(out1)

def graph_distance(G,H):
    return nx.graph_edit_distance(G,H)