import networkx as nx
import matplotlib.pyplot as plt
import random

# Crear un grafo vacío
G = nx.Graph()

# Añadir nodos al grafo
G.add_node("Estación de Monitoreo")  # Cambiado el nombre del nodo principal
G.add_node("Embalse A")
G.add_node("Embalse B")
G.add_node("Embalse C")
G.add_node("Embalse D")
G.add_node("Embalse E")

# Añadir ciudades a cada embalse
G.add_node("Ciudad 1")
G.add_node("Ciudad 2")
G.add_node("Ciudad 3")
G.add_node("Ciudad 4")
G.add_node("Ciudad 5")
G.add_node("Ciudad 6")
G.add_node("Ciudad 7")
G.add_node("Ciudad 8")
G.add_node("Ciudad 9")
G.add_node("Ciudad 10")
G.add_node("Ciudad 11")
G.add_node("Ciudad 12")

# Añadir aristas al grafo
G.add_edge("Estación de Monitoreo", "Embalse A", distance=20)  # Cambiado el nombre del nodo principal
G.add_edge("Estación de Monitoreo", "Embalse B", distance=15)  # Cambiado el nombre del nodo principal
G.add_edge("Estación de Monitoreo", "Embalse C", distance=25)  # Cambiado el nombre del nodo principal
G.add_edge("Estación de Monitoreo", "Embalse D", distance=30)  # Cambiado el nombre del nodo principal
G.add_edge("Estación de Monitoreo", "Embalse E", distance=18)  # Cambiado el nombre del nodo principal

# Añadir aristas entre embalses y ciudades
G.add_edge("Embalse A", "Ciudad 1", distance=5)
G.add_edge("Embalse A", "Ciudad 2", distance=8)
G.add_edge("Embalse A", "Ciudad 3", distance=7)
G.add_edge("Embalse B", "Ciudad 4", distance=12)
G.add_edge("Embalse B", "Ciudad 5", distance=10)
G.add_edge("Embalse C", "Ciudad 6", distance=6)
G.add_edge("Embalse C", "Ciudad 7", distance=9)
G.add_edge("Embalse D", "Ciudad 8", distance=11)
G.add_edge("Embalse D", "Ciudad 9", distance=14)
G.add_edge("Embalse E", "Ciudad 10", distance=8)
G.add_edge("Embalse E", "Ciudad 11", distance=5)
G.add_edge("Embalse E", "Ciudad 12", distance=10)

# Añadir etiquetas a las aristas del grafo
for u, v, data in G.edges(data=True):
    G.edges[u, v]["label"] = f"{data['distance']} km"

# Añadir etiquetas a los nodos que son embalses
for node in G.nodes():
    if node == "Estación de Monitoreo":  # Cambiado para agregar etiqueta específica
        G.nodes[node]["label"] = "Estación de Monitoreo"
        G.nodes[node]["color"] = "black"  # Color negro para la estación de monitoreo
    elif "Embalse" in node:
        water_level = random.randint(800, 2000)  # Generar nivel de agua inicial
        cambio_nivel_agua = random.uniform(-0.2, 0.1)  # Cambio en el nivel de agua entre -0.2 y 0.1
        nuevo_nivel_agua = max(0, round(water_level + cambio_nivel_agua))  # El nivel de agua no puede ser negativo

        precipitation = random.uniform(0, 200)  # Generar precipitación aleatoria
        cambio_precipitacion = random.uniform(-0.2, 0.2)  # Cambio en la precipitación entre -0.2 y 0.2
        nueva_precipitacion = max(0, round(precipitation + cambio_precipitacion))  # La precipitación no puede ser
        # negativa

        alert_level = random.uniform(40, 100)  # Generar nivel de alerta aleatorio
        cambio_alerta = random.uniform(-0.1, 0.1)  # Cambio en el nivel de alerta entre -0.1 y 0.1
        nuevo_alerta = max(0, round(alert_level + cambio_alerta))  # El nivel de alerta no puede ser negativo

        # Definir color del nodo según el nivel de alerta
        if 40 <= nuevo_alerta < 50:
            G.nodes[node]["color"] = "red"
        elif 50 <= nuevo_alerta < 60:
            G.nodes[node]["color"] = "orange"
        elif 60 <= nuevo_alerta < 80:
            G.nodes[node]["color"] = "blue"
        elif 80 <= nuevo_alerta <= 100:
            G.nodes[node]["color"] = "green"

        G.nodes[node]["label"] = (f"{node}\nNivel de agua: {nuevo_nivel_agua:.2f} m s. n. m.\n"
                                  f"Precipitación: {nueva_precipitacion:.2f} l/m²\n"
                                  f"Nivel de alerta: {nuevo_alerta:.2f} %")
    elif "Ciudad" in node:
        # Obtener el embalse al que pertenece la ciudad
        embalse_padre = next(G.neighbors(node))
        # Asignar el color del embalse al nodo ciudad
        G.nodes[node]["color"] = G.nodes[embalse_padre]["color"]
        consumption = random.uniform(10, 50)  # Generar consumo aleatorio
        G.nodes[node]["label"] = f"{node}\nConsumo de la ciudad: {consumption:.2f} m³/s"

# Posicionar manualmente los nodos utilizando fruchterman_reingold_layout
pos = nx.fruchterman_reingold_layout(G)

# Dibujar el grafo con las etiquetas y ajustar el tamaño de los nodos
node_colors = [G.nodes[node]["color"] for node in G.nodes()]
node_labels = nx.get_node_attributes(G, "label")
edge_labels = nx.get_edge_attributes(G, "label")

# Crear una leyenda personalizada para los colores de los nodos
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', label='Sistema de Monitoreo General',
               markerfacecolor='black', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Estado Crítico',
               markerfacecolor='red', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Estado de Advertencia',
               markerfacecolor='orange', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Estado Normal',
               markerfacecolor='blue', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Estado Óptimo',
               markerfacecolor='green', markersize=10),
]

plt.figure(figsize=(10, 10), num="Sistema de Gestión Ambiental")
nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=500, font_size=8, node_color=node_colors)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='brown')
plt.title("Fruchterman Reingold Layout")
plt.legend(handles=legend_elements, loc='upper right')
plt.show()
