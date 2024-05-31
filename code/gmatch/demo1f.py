from myfunc import *
from constantes import *
from icecream import ic

# model acm2013
G = factory_graph(f_acm2013, f_acm2013_enlaces)
print("Nodo G")
ic(len(G.nodes))
ic(len(G.edges))
draw_graph(G, '/home/su/tesis-sistemas/scripts/gmatch/images/unsa2010/G_acm2013.png', f_acm2013)

# comparaciones
print('--------------------------------')

H = factory_graph(f_unsa2010_acm2013, f_unsa2010_acm2013_m1)
ic(len(H.nodes))
ic(len(H.edges))

print("modelo 1:")

draw_graph(H, '/home/su/tesis-sistemas/scripts/gmatch/images/unsa2010/H_unsa2010_cmp_acm2013_m1.png', f_unsa2010_acm2013)

compara(G,H,"acm2013", "unsa2010 con links de acm2013")

mcs = getMCS(G,H)
print("mcs 1:")
lenNodeMCS = len(mcs.nodes)
lenEdgeMCS = len(mcs.edges)
ic(mcs.nodes)
ic(mcs.edges)
ic(lenNodeMCS)
ic(lenEdgeMCS)
num_node = len(mcs.nodes)
print("MCS 1 distance:")
distance_num = distance(num_node, len(G.nodes), len(H.nodes))
ic(distance_num)



# def draw_graph(S, f_outname, f_inname, mcs=None) 
# S y f_inname deben ser sobre el mismo nodo
draw_graph(H, '/home/su/tesis-sistemas/scripts/gmatch/images/unsa2010/H_unsa2010_cmp_acm2013_m1_mcs.png', f_unsa2010_acm2013, mcs)

draw_mix_graph(H, '/home/su/tesis-sistemas/scripts/gmatch/images/unsa2010/H_unsa2010_cmp_acm2013_m1_mcs_mix.png', f_unsa2010_acm2013, mcs, G)
# sistemas 2009 model 2 (relaciones originales de la carrera)
# Todo


T = factory_graph(f_unsa2010_acm2013, f_unsa2010_acm2013_m2)
draw_graph(T, '/home/su/tesis-sistemas/scripts/gmatch/images/unsa2010/H_unsa2010_cmp_acm2013_m2.png', f_unsa2010_acm2013)
print("Modelo 2")
compara(G,T,"acm13", "unsa sistemas 2010 con link de acm 2013")

mcs = getMCS(G,T)
print("mcs 2:")
ic(G.nodes)
ic(G.edges)
ic(T.nodes)
ic(T.edges)
lenNodeMCS = len(mcs.nodes)
lenEdgeMCS = len(mcs.edges)
ic(lenNodeMCS)
ic(lenEdgeMCS)
num_node = len(mcs.nodes)
print("MCS2 distance:")
ic(num_node)
ic(len(G.nodes))
ic(len(G.edges))
ic(len(T.nodes))
ic(len(T.edges))
distance_num = distance(num_node, len(G.nodes), len(T.nodes))
ic(distance_num)


draw_graph(T, '/home/su/tesis-sistemas/scripts/gmatch/images/unsa2010/H_unsa2010_cmp_acm2013_m2_mcs.png', f_unsa2010_acm2013, mcs)
draw_mix_graph(T, '/home/su/tesis-sistemas/scripts/gmatch/images/unsa2010/H_unsa2010_cmp_acm2013_m2_mcs_mix.png', f_unsa2010_acm2013, mcs, G)


# obtiene nodos y enlaces comunes
print("nodos y enlaces comunes model1")
X = getCS(G,H)
ic(len(X.nodes))
ic(len(X.edges))

print("nodos y enlaces comunes model2")
Y = getCS(G,T)
ic(len(Y.nodes))
ic(len(Y.edges))