'''
En una cafetería, los pedidos de los clientes deben gestionarse de dos maneras:

Pilas (Last-In-First-Out): Para los pedidos que son bebidas calientes (se procesan en el orden inverso al que se reciben, por practicidad).
Colas (First-In-First-Out): Para los pedidos que son comida (se procesan en el orden en que llegan).
Se implementará un sistema para gestionar los pedidos utilizando:

Pilas para almacenar y procesar bebidas calientes.
Colas para almacenar y procesar comida.
'''

from collections import deque

class GestionPedidos:
    def __init__(self):
        self.pila_bebidas = []  # Usaremos una lista como pila para bebidas
        self.cola_comida = deque()  # Usaremos deque como cola para comida

    # Agregar un pedido (bebida o comida)
    def agregar_pedido(self, tipo, nombre):
        if tipo.lower() == "bebida":
            self.pila_bebidas.append(nombre)  # Agregar a la pila
            print(f"Bebida '{nombre}' agregada a la pila de bebidas.")
        elif tipo.lower() == "comida":
            self.cola_comida.append(nombre)  # Agregar a la cola
            print(f"Comida '{nombre}' agregada a la cola de comidas.")
        else:
            print("Tipo de pedido no válido. Use 'bebida' o 'comida'.")

    # Procesar el siguiente pedido de bebidas (LIFO)
    def procesar_bebida(self):
        if self.pila_bebidas:
            bebida = self.pila_bebidas.pop()  # Quitar el último elemento de la pila
            print(f"Bebida procesada: {bebida}")
        else:
            print("No hay bebidas pendientes.")

    # Procesar el siguiente pedido de comida (FIFO)
    def procesar_comida(self):
        if self.cola_comida:
            comida = self.cola_comida.popleft()  # Quitar el primer elemento de la cola
            print(f"Comida procesada: {comida}")
        else:
            print("No hay comidas pendientes.")

    # Mostrar el estado actual de las pilas y colas
    def mostrar_pedidos(self):
        print("\nEstado actual de los pedidos:")
        print(f"Bebidas (LIFO): {self.pila_bebidas}")
        print(f"Comidas (FIFO): {list(self.cola_comida)}")