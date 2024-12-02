import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
directions = ""
# open the file and read in the lines
with open("day08.txt", "r") as f:
    for line in f:
        if "LR" in line:
            directions = line
        elif len(line) > 1:
            node, edges = line.strip().split(" = ")
            edgetuple = edges.split("(")[1].split(")")[0].split(", ")
            # print(node, edgetuple)
            G.add_node(node)
            if edgetuple[0] == edgetuple[1]:
                G.add_edge(node, edgetuple[0], direction="LR")
            else:
                G.add_edge(node, edgetuple[0], direction="L")
                G.add_edge(node, edgetuple[1], direction="R")
print(G.adj)

# nx.draw(G, with_labels=True)
# ax = plt.gca()
# ax.margins(0.20)
# plt.axis("off")
# plt.show()

here = G["AAA"]

print(G['ZZZ'])

steps = 0
while here != G["ZZZ"]:
    for d in directions:
        for nbr in here:
            if d in here[nbr]['direction']:
                here = G[nbr]
                steps += 1
                break

print("***", steps)
# 4300000
