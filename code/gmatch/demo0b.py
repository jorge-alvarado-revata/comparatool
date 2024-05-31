from myfunc import *
from constantes import *
from icecream import ic
# model G
G = factory_graph(demoGE17, demoG_enlaces17)
print("Nodo G")

ic(G.nodes)
ic(G.edges)
draw_graph(G, '/home/su/tesis-sistemas/scripts/gmatch/images/demob/demoG17.png', demoGE17)

#/home/su/tesis-sistemas/scripts/gmatch/images/demo

# model H
H = factory_graph(demoH24, demoH_enlaces24)
print("Nodo H")
ic(H.nodes)
ic(H.edges)
draw_graph(H, '/home/su/tesis-sistemas/scripts/gmatch/images/demob/demoH24.png', demoH24)

print("modelo 1:")
compara(G,H,"G", "H")

mcs = getMCS(G,H)
print("mcs:")
ic(mcs.nodes)
ic(mcs.edges)
num_node = len(mcs.nodes)
print("MCS distance:")
ged = distance(num_node, len(G.nodes), len(H.nodes))
ic(ged)

print("MCS 1 distance - nx distance:")
ged2 = graph_distance(G,H)
ic(ged2)

# def draw_graph(S, f_outname, f_inname, mcs=None) 
# S y f_inname deben ser sobre el mismo nodo
draw_graph(H, '/home/su/tesis-sistemas/scripts/gmatch/images/demob/mcs.png', demoH24, mcs)


draw_mix_graph(H,'/home/su/tesis-sistemas/scripts/gmatch/images/demob/mcs_mix.png', demoH24, mcs, G)