from myfunc import *
from constantes import *
from icecream import ic

# model acm68
G = factory_graph(f_acm68, f_acm68_enlaces)
print("Nodo G")
ic(len(G.nodes))
ic(len(G.edges))
draw_graph(G, 'images/sisuni2018/G_acm2013.png', f_acm68)

# comparaciones
print('--------------------------------')

H = factory_graph(f_uni2018_acm68, f_uni2018_acm68_m1)
ic(len(H.nodes))
ic(len(H.edges))

print("modelo 1:")

draw_graph(H, 'images/sisuni2018/H_sisuni2018_cmp_acm68_m1.png', f_uni2018_acm68)

compara(G,H,"acm68", "sisuni2018 con links de acm68")

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
ged = distance(num_node, len(G.nodes), len(H.nodes))
ic(ged)



# def draw_graph(S, f_outname, f_inname, mcs=None) 
# S y f_inname deben ser sobre el mismo nodo
draw_graph(H, 'images/sisuni2018/H_sisuni2018_cmp_acm68_m1_mcs.png', f_uni2018_acm68, mcs)

draw_mix_graph(H, 'images/sisuni2018/H_sisuni2018_cmp_acm68_m1_mcs_mix.png', f_uni2018_acm68, mcs, G)
# sistemas 2009 model 2 (relaciones originales de la carrera)
# Todo


T = factory_graph(f_uni2018_acm68, f_uni2018_acm68_m2)
draw_graph(T, 'images/sisuni2018/H_sisuni2018_cmp_acm68_m2.png', f_uni2018_acm68)
print("Modelo 2")
compara(G,T,"acm68", "uni sistemas 2018 con link de sistemas 2018")

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
ged = distance(num_node, len(G.nodes), len(T.nodes))
ic(ged)


draw_graph(T, 'images/sisuni2018/H_sisuni2018_cmp_acm68_m2_mcs.png', f_uni2018_acm68, mcs)
draw_mix_graph(T, 'images/sisuni2018/H_sisuni2018_cmp_acm68_m2_mcs_mix.png', f_uni2018_acm68, mcs, G)


# obtiene nodos y enlaces comunes
print("nodos y enlaces comunes model1")
X = getCS(G,H)
ic(len(X.nodes))
ic(len(X.edges))

print("nodos y enlaces comunes model2")
Y = getCS(G,T)
ic(len(Y.nodes))
ic(len(Y.edges))