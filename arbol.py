'''
Descripción del problema: Organizar tareas de un día o semana según su prioridad. Esto es útil para visualizar y completar las tareas 
en el orden correcto.

Estructura del Árbol Binario
Nodos: Cada nodo representa una tarea y tiene dos valores principales:
Prioridad (clave): Un número que representa qué tan importante es la tarea (mayor número = mayor prioridad).
Descripción de la tarea: El texto que describe la tarea específica.
Métodos de ordenamiento:
 - Preorden (Prioridades antes que descripciones): Lista las tareas desde la raíz hasta las hojas. Podrías usarlo para ver todas las tareas 
en el orden en que deberían completarse.
 - Inorden (Prioridad de menor a mayor): Te permitirá listar las tareas de menor a mayor prioridad, si deseas ver primero las menos importantes.
 - Postorden (Dejar las más importantes al final): Esto podría ayudarte si deseas completar las tareas en orden inverso de importancia, 
dejando las cruciales para después de las menos urgentes.
'''

# Definición del Nodo del Árbol
class Nodo:
    def __init__(self, prioridad, descripcion):
        self.prioridad = prioridad  # Clave principal para ordenar el árbol (la prioridad de la tarea)
        self.descripcion = descripcion  # La descripción de la tarea
        self.izquierda = None  # Hijo izquierdo
        self.derecha = None  # Hijo derecho

class ArbolBinario:
    def __init__(self):
        self.raiz = None  # Inicialmente, el árbol está vacío

    # Método para insertar un nuevo nodo en el árbol
    def insertar(self, prioridad, descripcion):
        nuevo_nodo = Nodo(prioridad, descripcion)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)

    def _insertar_recursivo(self, nodo_actual, nuevo_nodo):
        if nuevo_nodo.prioridad < nodo_actual.prioridad:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.izquierda, nuevo_nodo)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.derecha, nuevo_nodo)

    # Método para buscar un nodo por su prioridad
    def buscar(self, prioridad):
        return self._buscar_recursivo(self.raiz, prioridad)

    def _buscar_recursivo(self, nodo_actual, prioridad):
        if nodo_actual is None:  # Caso base: no se encontró el nodo
            return None
        if nodo_actual.prioridad == prioridad:  # Caso base: se encontró el nodo
            return nodo_actual
        elif prioridad < nodo_actual.prioridad:  # Buscar en el subárbol izquierdo
            return self._buscar_recursivo(nodo_actual.izquierda, prioridad)
        else:  # Buscar en el subárbol derecho
            return self._buscar_recursivo(nodo_actual.derecha, prioridad)

    # Método para eliminar un nodo por su prioridad
    def eliminar(self, prioridad):
        self.raiz = self._eliminar_recursivo(self.raiz, prioridad)

    def _eliminar_recursivo(self, nodo_actual, prioridad):
        if nodo_actual is None:
            return nodo_actual  # Nodo no encontrado

        # Navegar al nodo a eliminar
        if prioridad < nodo_actual.prioridad:
            nodo_actual.izquierda = self._eliminar_recursivo(nodo_actual.izquierda, prioridad)
        elif prioridad > nodo_actual.prioridad:
            nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, prioridad)
        else:  # Nodo encontrado
            # Caso 1: Nodo sin hijos
            if nodo_actual.izquierda is None and nodo_actual.derecha is None:
                return None
            # Caso 2: Nodo con un solo hijo
            elif nodo_actual.izquierda is None:
                return nodo_actual.derecha
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierda
            # Caso 3: Nodo con dos hijos
            else:
                # Encontrar el sucesor inorden
                sucesor = self._minimo(nodo_actual.derecha)
                # Reemplazar los valores del nodo con el sucesor
                nodo_actual.prioridad = sucesor.prioridad
                nodo_actual.descripcion = sucesor.descripcion
                # Eliminar el sucesor del subárbol derecho
                nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, sucesor.prioridad)
        return nodo_actual

    # Método para encontrar el nodo con el valor mínimo en un subárbol
    def _minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    # Recorridos en el árbol
    def preorden(self, nodo_actual):
        if nodo_actual:
            print(f"Prioridad: {nodo_actual.prioridad}, Tarea: {nodo_actual.descripcion}")
            self.preorden(nodo_actual.izquierda)
            self.preorden(nodo_actual.derecha)

    def inorden(self, nodo_actual):
        if nodo_actual:
            self.inorden(nodo_actual.izquierda)
            print(f"Prioridad: {nodo_actual.prioridad}, Tarea: {nodo_actual.descripcion}")
            self.inorden(nodo_actual.derecha)

    def postorden(self, nodo_actual):
        if nodo_actual:
            self.postorden(nodo_actual.izquierda)
            self.postorden(nodo_actual.derecha)
            print(f"Prioridad: {nodo_actual.prioridad}, Tarea: {nodo_actual.descripcion}")
