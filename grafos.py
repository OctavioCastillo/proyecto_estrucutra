'''
Imagina que estás planeando un viaje por varias ciudades y deseas explorar todas las conexiones 
entre las ciudades (por ejemplo, rutas de autobús o vuelos). Quieres asegurarte de visitar todas las 
ciudades conectadas, partiendo de una ciudad específica, explorando de manera exhaustiva cada ruta posible antes de retroceder.

Esto se puede modelar como un grafo no dirigido, donde:

Nodos: Representan las ciudades.
Aristas: Representan las rutas entre las ciudades.
'''

class Grafo:
    def __init__(self):
        self.grafo = {}  # Diccionario para almacenar nodos y sus conexiones

    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def agregar_arista(self, origen, destino):
        self.grafo[origen].append(destino)
        self.grafo[destino].append(origen)  # Grafo no dirigido

    def dfs(self, inicio):
        visitados = set()  # Conjunto para rastrear nodos visitados
        recorrido = []  # Lista para registrar el orden de visita
        self._dfs_recursivo(inicio, visitados, recorrido)
        return recorrido

    def _dfs_recursivo(self, nodo_actual, visitados, recorrido):
        visitados.add(nodo_actual)  # Marcar el nodo como visitado
        recorrido.append(nodo_actual)  # Agregar el nodo al recorrido
        for vecino in self.grafo[nodo_actual]:  # Explorar vecinos
            if vecino not in visitados:
                self._dfs_recursivo(vecino, visitados, recorrido)
