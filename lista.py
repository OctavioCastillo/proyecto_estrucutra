'''
Imagina que estás administrando una biblioteca pequeña y necesitas una forma eficiente de gestionar 
los libros disponibles. Los libros se registran con un número de identificación único (ID) y un título. El objetivo es poder:

Agregar libros a la colección.
Ordenar los libros por ID para facilitar la búsqueda.
Buscar un libro específico por su ID de manera eficiente.
Para resolver este problema, usaremos una lista doblemente ligada para manejar dinámicamente la 
colección de libros, implementando quicksort para ordenar los libros y búsqueda binaria para localizar un libro rápidamente.
'''

class Nodo:
    def __init__(self, id_libro, titulo):
        self.id_libro = id_libro
        self.titulo = titulo
        self.siguiente = None
        self.anterior = None


class ListaDoblementeLigada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    # Método para agregar un libro a la lista
    def agregar_libro(self, id_libro, titulo):
        nuevo_nodo = Nodo(id_libro, titulo)
        if self.cabeza is None:  # La lista está vacía
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    # Método para mostrar todos los libros
    def mostrar_libros(self):
        print("\nLista de libros:")
        actual = self.cabeza
        while actual:
            print(f"ID: {actual.id_libro}, Título: {actual.titulo}")
            actual = actual.siguiente

    # Convierte la lista ligada en una lista simple para ordenamiento
    def convertir_a_lista(self):
        lista = []
        actual = self.cabeza
        while actual:
            lista.append((actual.id_libro, actual.titulo))
            actual = actual.siguiente
        return lista

    # Actualiza la lista doblemente ligada desde una lista simple
    def actualizar_desde_lista(self, lista):
        self.cabeza = self.cola = None
        for id_libro, titulo in lista:
            self.agregar_libro(id_libro, titulo)

    # Método para ordenar la lista usando quicksort
    def ordenar_libros(self):
        lista = self.convertir_a_lista()

        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivote = arr[len(arr) // 2]
            menores = [x for x in arr if x[0] < pivote[0]]
            iguales = [x for x in arr if x[0] == pivote[0]]
            mayores = [x for x in arr if x[0] > pivote[0]]
            return quicksort(menores) + iguales + quicksort(mayores)

        lista_ordenada = quicksort(lista)
        self.actualizar_desde_lista(lista_ordenada)

    # Método para buscar un libro por ID usando búsqueda binaria
    def buscar_libro(self, id_libro):
        lista = self.convertir_a_lista()

        def busqueda_binaria(arr, id_buscar):
            inicio, fin = 0, len(arr) - 1
            while inicio <= fin:
                medio = (inicio + fin) // 2
                if arr[medio][0] == id_buscar:
                    return arr[medio]
                elif arr[medio][0] < id_buscar:
                    inicio = medio + 1
                else:
                    fin = medio - 1
            return None

        resultado = busqueda_binaria(lista, id_libro)
        if resultado:
            print(f"\nLibro encontrado: ID: {resultado[0]}, Título: {resultado[1]}")
        else:
            print(f"\nNo se encontró un libro con ID {id_libro}")


# Ejemplo de uso
biblioteca = ListaDoblementeLigada()
biblioteca.agregar_libro(102, "Cien Años de Soledad")
biblioteca.agregar_libro(56, "El Principito")
biblioteca.agregar_libro(89, "1984")
biblioteca.agregar_libro(33, "Don Quijote")
biblioteca.agregar_libro(120, "Matar a un Ruiseñor")

# Mostrar libros antes de ordenar
biblioteca.mostrar_libros()

# Ordenar los libros
print("\nOrdenando los libros por ID...")
biblioteca.ordenar_libros()

# Mostrar libros después de ordenar
biblioteca.mostrar_libros()

# Buscar un libro por ID
id_a_buscar = int(input("\nIntroduce el ID del libro que deseas buscar: "))
biblioteca.buscar_libro(id_a_buscar)
