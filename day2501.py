import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()

# open the file and read in the lines
lines = []
with open("day25.txt", "r") as f:
    for line in f:
        o, ns = line.strip().split(":")
        for n in ns.strip().split(" "):
            G.add_edge(o, n)

# print(f"nodes: {G.number_of_nodes()}, edges: {G.number_of_edges()}")

# nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()

# after looking at the graph, just need to remove:
r = G.remove_edge("sml", "jbx")
r = G.remove_edge("vxr", "zhb")
r = G.remove_edge("vqj", "szh")

print(len(nx.node_connected_component(G, "vqj"))
      * len(nx.node_connected_component(G, "szh")))
