from myfunc import *
from constantes import *
from icecream import ic

# model acm68 
G = factory_graph(f_acm68, f_acm68_enlaces)
print("Nodo G")
ic(G.nodes)
ic(G.edges)
ic(len(G.nodes))
ic(len(G.edges))
draw_graph(G, 'images/sis2018/G_acm68.png', f_acm68)


# Comparaciones
H = factory_graph(f_sis2018_acm68, f_sis2018_acm68_m1)
print("Nodo H")
ic(H.nodes)
ic(H.edges)
ic(len(H.nodes))
ic(len(H.edges))

draw_graph(H, 'images/sis2018/H_sis2018_acm68_m1.png', f_sis2018_acm68)

print("modelo 1:")
compara(G,H,"sistemas 2018", "acm68")

mcs = getMCS(G,H)
print("mcs 1:")
lenNodeMCS = len(mcs.nodes)
lenEdgeMCS = len(mcs.edges)
ic(mcs.nodes)
ic(mcs.edges)
ic(lenNodeMCS)
ic(lenEdgeMCS)

num_node = len(mcs.nodes)
print("MCS 1  distance:")
ged = distance(num_node, len(G.nodes), len(H.nodes))
ic(ged)

# def draw_graph(S, f_outname, f_inname, mcs=None) 
# S y f_inname deben ser sobre el mismo nodo
draw_graph(H, 'images/sis2018/H_sis2018_acm68_m1_mcs.png', f_sis2018_acm68, mcs)
draw_mix_graph(H, 'images/sis2018/H_sis2018_acm68_m1_mcs_mix.png', f_sis2018_acm68, mcs, G)

# sistemas 2017 model 2 (relaciones originales de la carrera)

T = factory_graph(f_sis2018_acm68, f_sis2018_acm68_m2)
draw_graph(T, 'images/sis2018/H_sis2018_acm68_m2.png', f_sis2018_acm68)
print("Modelo 2")
compara(G,T,"sistemas 2018 originales", "acm68")

ic(G.nodes)
ic(G.edges)
ic(len(G.nodes))
ic(len(G.edges))

ic(T.nodes)
ic(T.edges)
ic(len(T.nodes))
ic(len(T.edges))


mcs = getMCS(G,T)
print("mcs 2 :")
lenNodeMCS = len(mcs.nodes)
lenEdgeMCS = len(mcs.edges)
ic(mcs.nodes)
ic(mcs.edges)
ic(lenNodeMCS)
ic(lenEdgeMCS)

num_node = len(mcs.nodes)
print("MCS 1 distance:")
print(num_node)

ged = distance(num_node, len(G.nodes), len(T.nodes))
ic(ged)
draw_graph(T, 'images/sis2018/H_sis2018_acm68_m2_mcs.png', f_sis2018_acm68, mcs)
draw_mix_graph(T, 'images/sis2018/H_sis2018_acm68_m2_mcs_mix.png', f_sis2018_acm68, mcs, G)

# obtiene nodos y enlaces comunes
print("nodos y enlaces comunes model1")
X = getCS(G,H)
ic(len(X.nodes))
ic(len(X.edges))

print("nodos y enlaces comunes model2")
Y = getCS(G,T)
ic(len(Y.nodes))
ic(len(Y.edges))

