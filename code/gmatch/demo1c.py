from myfunc import *
from constantes import *
from icecream import ic

G = factory_graph(f_sis2009, f_sis2009_enlaces)
ic(G.nodes)
ic(G.edges)
lenGNodes = len(G.nodes)
lenGEdges = len(G.edges)
ic(lenGNodes)
ic(lenGEdges)

draw_graph(G, '/home/su/tesis-sistemas/scripts/gmatch/images/sis2018/G_2009.png', f_sis2009)

# Comparaciones
# Enlaces sis2009
H = factory_graph(f_sis2018_sis2009, f_sis2018_sis2009_m1)
ic(H.nodes)
ic(H.edges)

lenHNodes = len(H.nodes)
lenHEdges = len(H.edges)
ic(lenHNodes)
ic(lenHEdges)

draw_graph(H, '/home/su/tesis-sistemas/scripts/gmatch/images/sis2018/H_sis2018_cmp_sis2009_m1.png', f_sis2018_sis2009)
print("modelo 1:")
compara(G,H,"sistemas 2018", "sistemas2009")

mcs = getMCS(G,H)
print("mcs 1:")
ic(mcs.nodes)
ic(mcs.edges)
lenMCSNodes = len(mcs.nodes)
lenMCSEdges = len(mcs.edges)
ic(lenMCSNodes)
ic(lenMCSEdges)
num_node = len(mcs.nodes)
print("MCS 1 distance:")
ged = distance(num_node, len(G.nodes), len(H.nodes))
ic(ged)

# def draw_graph(S, f_outname, f_inname, mcs=None) 
# S y f_inname deben ser sobre el mismo nodo
draw_graph(H, '/home/su/tesis-sistemas/scripts/gmatch/images/sis2018/H_sis2018_cmp_sis2009_m1_mcs.png', f_sis2018_sis2009, mcs)
draw_mix_graph(H, '/home/su/tesis-sistemas/scripts/gmatch/images/sis2018/H_sis2018_cmp_sis2009_m1_mcs_mix.png', f_sis2018_sis2009, mcs, G)

# sistemas 2009 model 2 (relaciones originales de la carrera)

T = factory_graph(f_sis2018_sis2009, f_sis2018_sis2009_m2)
draw_graph(T, '/home/su/tesis-sistemas/scripts/gmatch/images/sis2018/H_sis2018_cmp_sis2009_m2.png', f_sis2018_sis2009)

lenTNodes = len(T.nodes)
lenTEdges = len(T.edges)
ic(lenTNodes)
ic(lenTEdges)

print("Modelo 2")
compara(G,T,"sistemas 2018 originales", "sistemas2009")

mcs = getMCS(G,T)
print("mcs 2:")
ic(mcs.nodes)
ic(mcs.edges)

lenMCSNodes = len(mcs.nodes)
lenMCSEdges = len(mcs.edges)
ic(lenMCSNodes)
ic(lenMCSEdges)

num_node = len(mcs.nodes)
print("MCS 2 distance:")
ged = distance(num_node, len(G.nodes), len(T.nodes))
ic(ged)

draw_graph(T, '/home/su/tesis-sistemas/scripts/gmatch/images/sis2018/H_sis2018_cmp_sis2009_m2_mcs.png', f_sis2018_sis2009, mcs)
draw_mix_graph(T, '/home/su/tesis-sistemas/scripts/gmatch/images/sis2018/H_sis2018_cmp_sis2009_m2_mcs_mix.png', f_sis2018_sis2009, mcs, G)

# obtiene nodos y enlaces comunes
print("nodos y enlaces comunes model1 sis2017-sis2009")
X = getCS(G,H)
ic(len(X.nodes))
ic(len(X.edges))

print("nodos y enlaces comunes model2 sis2017-sis2009")
Y = getCS(G,T)
ic(len(Y.nodes))
ic(len(Y.edges))

# Compara 2018 con acm 2013
# Recordar G tiene los ID originales de acm2013 y enlaces originales

print("Compara 2018 con acm 2013")
G = factory_graph(f_acm2013, f_acm2013_enlaces)
ic(G.nodes)
ic(G.edges)
lenGNodes = len(G.nodes)
lenGEdges = len(G.edges)
ic(lenGNodes)
ic(lenGEdges)

draw_graph(G, '/home/su/tesis-sistemas/scripts/gmatch/images/acm2013/G_acm2013.png', f_acm2013)

# H tiene los id originales de los cursos equivalentes acm2013 y
#  sis2018 combinados,  con enlaces de acm2013

H = factory_graph(f_sis2018_acm2013, f_sis2018_acm2013_m1)
ic(H.nodes)
ic(H.edges)
print("modelo 1:")
compara(G,H,"sistemas 2018", "acm2013")

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

draw_graph(H, '/home/su/tesis-sistemas/scripts/gmatch/images/sis2018/H_sis2018_cmp_acm2013_m1_mcs.png', f_sis2018_acm2013, mcs)
draw_mix_graph(H, '/home/su/tesis-sistemas/scripts/gmatch/images/sis2018/H_sis2018_cmp_acm2013_m1_mcs_mix.png', f_sis2018_acm2013, mcs, G)

# T tiene los id originales de los cursos equivalentes acm2013 y
#  sis2018 combinados,  con enlaces de sis2018



T = factory_graph(f_sis2018_acm2013, f_sis2018_acm2013_m2)

lenTNodes = len(T.nodes)
lenTEdges = len(T.edges)
ic(lenTNodes)
ic(lenTEdges)

draw_graph(T, '/home/su/tesis-sistemas/scripts/gmatch/images/sis2018/H_sis2018_cmp_acm2013_m2.png', f_sis2018_acm2013)
print("Modelo 4")
compara(G,T,"sistemas 2018 originales", "acm2013")

mcs = getMCS(G,T)
print("mcs 4:")
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
print(ged)
draw_graph(T, '/home/su/tesis-sistemas/scripts/gmatch/images/sis2018/H_sis2018_cmp_acm2013_m2_mcs.png', f_sis2018_acm2013, mcs)
draw_mix_graph(T, '/home/su/tesis-sistemas/scripts/gmatch/images/sis2018/H_sis2018_cmp_acm2013_m2_mcs_mix.png', f_sis2018_acm2013, mcs, G)

# obtiene nodos y enlaces comunes
print("nodos y enlaces comunes model1 sis2017-acm2013")
X = getCS(G,H)
ic(len(X.nodes))
ic(len(X.edges))

print("nodos y enlaces comunes model2  sis2017-acm2013")
Y = getCS(G,T)
ic(len(Y.nodes))
ic(len(Y.edges))