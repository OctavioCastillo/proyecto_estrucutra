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

# Definición del Árbol Binario
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

    # Recorrido en preorden (raíz, izquierda, derecha)
    def preorden(self, nodo_actual):
        if nodo_actual:
            print(f"Prioridad: {nodo_actual.prioridad}, Tarea: {nodo_actual.descripcion}")
            self.preorden(nodo_actual.izquierda)
            self.preorden(nodo_actual.derecha)

    # Recorrido en inorden (izquierda, raíz, derecha)
    def inorden(self, nodo_actual):
        if nodo_actual:
            self.inorden(nodo_actual.izquierda)
            print(f"Prioridad: {nodo_actual.prioridad}, Tarea: {nodo_actual.descripcion}")
            self.inorden(nodo_actual.derecha)

    # Recorrido en postorden (izquierda, derecha, raíz)
    def postorden(self, nodo_actual):
        if nodo_actual:
            self.postorden(nodo_actual.izquierda)
            self.postorden(nodo_actual.derecha)
            print(f"Prioridad: {nodo_actual.prioridad}, Tarea: {nodo_actual.descripcion}")

# Ejemplo de uso del árbol
arbol = ArbolBinario()
arbol.insertar(5, "Terminar el proyecto de estructura de datos")
arbol.insertar(2, "Llamar a un amigo")
arbol.insertar(8, "Preparar la reunión de mañana")
arbol.insertar(1, "Comprar café")
arbol.insertar(7, "Revisar correos electrónicos")

print("\nRecorrido en Preorden:")
arbol.preorden(arbol.raiz)

print("\nRecorrido en Inorden:")
arbol.inorden(arbol.raiz)

print("\nRecorrido en Postorden:")
arbol.postorden(arbol.raiz)
