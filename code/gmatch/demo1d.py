from myfunc import *
from constantes import *
from icecream import ic

# Compara pucp2020 con acm 2013
# Recordar G tiene los ID originales de acm2013 y enlaces originales

G = factory_graph(f_acm2013, f_acm2013_enlaces)
ic(G.nodes)
ic(G.edges)
lenGNodes = len(G.nodes)
lenGEdges = len(G.edges)
ic(lenGNodes)
ic(lenGEdges)

draw_graph(G, 'images/pucp2020/G_acm2013.png', f_acm2013)

# H tiene los id originales de los cursos equivalentes acm2013 y
#  sis2018 combinados,  con enlaces de acm2013

H = factory_graph(f_pucp2020_nodes, f_pucp2020_enlaces)
draw_graph(H, 'images/pucp2020/H_pucp2020.png', f_pucp2020_nodes)
ic(H.nodes)
ic(H.edges)

lenHNodes = len(H.nodes)
lenHEdges = len(H.edges)
ic(lenHNodes)
ic(lenHEdges)
# Comparacion

H = factory_graph(f_pucp2020_acm2013, f_pucp2020_acm2013_m1)

print("modelo 1:")
compara(G,H,"pucp2020", "acm2013")

lenHNodes = len(H.nodes)
lenHEdges = len(H.edges)
ic(lenHNodes)
ic(lenHEdges)

mcs = getMCS(G,H)
print("mcs:")
lenNodeMCS = len(mcs.nodes)
lenEdgeMCS = len(mcs.edges)
ic(mcs.nodes)
ic(mcs.edges)
ic(lenNodeMCS)
ic(lenEdgeMCS)


num_node = len(mcs.nodes)
print("MCS 3 distance:")
ged = distance(num_node, len(G.nodes), len(H.nodes))
ic(ged)

draw_graph(H, 'images/pucp2020/H_pucp2020_cmp_acm2013_m1_mcs.png', f_pucp2020_acm2013, mcs)
draw_mix_graph(H, 'images/pucp2020/H_pucp2020_cmp_acm2013_m1_mcs_mix.png', f_pucp2020_acm2013, mcs, G)

# T tiene los id originales de los cursos equivalentes acm2013 y
#  sis2018 combinados,  con enlaces de sis2018

T = factory_graph(f_pucp2020_acm2013, f_pucp2020_acm2013_m2)

lenTNodes = len(T.nodes)
lenTEdges = len(T.edges)
ic(lenTNodes)
ic(lenTEdges)

draw_graph(T, 'images/pucp2020/H_pucp2020_cmp_acm2013_m2.png', f_pucp2020_acm2013)
print("Modelo 2")
compara(G,T,"pucp2020 originales", "acm2013")

mcs = getMCS(G,T)
print("mcs 2:")
lenNodeMCS = len(mcs.nodes)
lenEdgeMCS = len(mcs.edges)
ic(mcs.nodes)
ic(mcs.edges)
ic(lenNodeMCS)
ic(lenEdgeMCS)

num_node = len(mcs.nodes)
print("MCS 4 distance:")
print(num_node)
print(f'G nodos:{len(G.nodes)}')
print(f'T nodos:{len(T.nodes)}')
ged = distance(num_node, len(G.nodes), len(T.nodes))
ic(ged)
draw_graph(T, 'images/pucp2020/H_pucp2020_cmp_acm2013_m2_mcs.png', f_pucp2020_acm2013, mcs)
draw_mix_graph(T, 'images/pucp2020/H_pucp2020_cmp_acm2013_m2_mcs_mix.png', f_pucp2020_acm2013, mcs, G)

# obtiene nodos y enlaces comunes
print("nodos y enlaces comunes model1 pucp2020-acm2013")
X = getCS(G,H)
ic(len(X.nodes))
ic(len(X.edges))

print("nodos y enlaces comunes model2  pucp2020-acm2013")
Y = getCS(G,T)
ic(len(Y.nodes))
ic(len(Y.edges))