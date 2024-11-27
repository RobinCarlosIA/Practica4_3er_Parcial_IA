import networkx as nx
import matplotlib.pyplot as plt

def prim_mst(grafo, nodo_inicial):
    """
    Simula el Algoritmo de Prim para encontrar el Árbol de Expansión Mínima (MST).
    """
    mst = []  # Guardamos las aristas del Árbol de Expansión Mínima
    visitados = set()  # Nodos visitados
    visitados.add(nodo_inicial)  # Empezamos con el nodo inicial
    print(f"Iniciamos desde el nodo: {nodo_inicial}\n")

    while len(visitados) < len(grafo):
        menor_peso = float('inf')
        mejor_arista = None

        # Buscar la arista más pequeña que conecta un nodo visitado con uno no visitado
        for nodo in visitados:
            for vecino, peso in grafo[nodo]:
                if vecino not in visitados and peso < menor_peso:
                    menor_peso = peso
                    mejor_arista = (nodo, vecino, peso)

        if mejor_arista:
            mst.append(mejor_arista)
            visitados.add(mejor_arista[1])  # Agregar el nuevo nodo como visitado
            print(f"Agregando arista: {mejor_arista[0]} --({mejor_arista[2]})--> {mejor_arista[1]}")

    print("\nÁrbol de Expansión Mínima completo:")
    for arista in mst:
        print(f"  {arista[0]} --({arista[2]})--> {arista[1]}")

    return mst

def dibujar_grafo(grafo, mst):
    """
    Dibuja el grafo original y el Árbol de Expansión Mínima.
    """
    G = nx.Graph()
    for nodo, vecinos in grafo.items():
        for vecino, peso in vecinos:
            G.add_edge(nodo, vecino, weight=peso)

    pos = nx.spring_layout(G)  # Posiciones de los nodos
    pesos = nx.get_edge_attributes(G, 'weight')

    # Dibujar el grafo completo
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos)

    # Dibujar el MST
    mst_edges = [(arista[0], arista[1]) for arista in mst]
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color="red", width=2)

    plt.title("Árbol de Expansión Mínima (MST)")
    plt.show()

# Grafo con los mismos nodos y datos que antes
grafo = {
    'R': [('E', 2), ('C', 4)],
    'E': [('R', 2), ('G', 7), ('F', 3)],
    'C': [('R', 4), ('F', 1), ('D', 5)],
    'G': [('E', 7), ('D', 2)],
    'F': [('E', 3), ('C', 1), ('B', 8)],
    'D': [('C', 5), ('G', 2), ('B', 6)],
    'B': [('F', 8), ('D', 6)]
}

# Nodo inicial
nodo_inicial = 'R'

# Ejecutar el Algoritmo de Prim
print("=== Algoritmo de Prim ===\n")
mst = prim_mst(grafo, nodo_inicial)

# Dibujar el grafo y el MST
dibujar_grafo(grafo, mst)
