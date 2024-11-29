import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
G = nx.DiGraph()

# Agregar nodos (clientes, depósitos)
G.add_node("Depósito")
G.add_node("Cliente 1")
G.add_node("Cliente 2")
G.add_node("Cliente 3")

# Agregar aristas (rutas de entrega)
G.add_edge("Depósito", "Cliente 1", weight=10)
G.add_edge("Depósito", "Cliente 2", weight=20)
G.add_edge("Cliente 1", "Cliente 3", weight=5)

# Dibujar el grafo
nx.draw(G, with_labels=True, node_size=3000, node_color="skyblue", font_size=10)
plt.show()
