import networkx as nx
import matplotlib.pyplot as plt


aristas = [('A', 'B', 11), ('A', 'F', 21), ('B', 'E', 3), ('E', 'D', 10), ('E', 'I', 9), ('E', 'D', 10), ('I', 'H', 8),
           ('H', 'D', 15), ('I', 'F', 19), ('I', 'J', 9), ('J', 'G', 7), ('E', 'D', 10), ('F', 'G', 28), ('F', 'J', 30), ('F', 'C', 25)]
vertices = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]


#Grafo = nx.DiGraph()
Grafo = nx.Graph()
Grafo.add_nodes_from(vertices)

Grafo.add_weighted_edges_from(aristas)
GrafoND = nx.Graph()
GrafoND.add_nodes_from(vertices)
GrafoND.add_weighted_edges_from(aristas)

print("dijkstra")
print(nx.dijkstra_path(Grafo, 'A', 'C'))
print(nx.dijkstra_path(Grafo, 'B', 'A'))


print("MST")
T = nx.minimum_spanning_tree(GrafoND)  # Kruskal
print(sorted(T.edges(data=True)))


print("coloreo")
G = nx.algorithms.coloring.strategy_connected_sequential(Grafo, ["red", "blue", "yelow"], traversal='bfs')
G = nx.algorithms.coloring.greedy_color(GrafoND, strategy='largest_first', interchange=False)
print(G)


nx.draw(Grafo, pos=nx.circular_layout(Grafo), node_color='r', edge_color='b', with_labels=True)
#nx.draw_networkx_edge_labels(Grafo, pos=nx.spring_layout(Grafo))

plt.show()
