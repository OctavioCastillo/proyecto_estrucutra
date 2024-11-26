'''
En esté archivo se encuentra el menú y de aquí se pueden probar el resto de clases
'''

from arbol import ArbolBinario
from grafos import Grafo
from cafeteria import GestionPedidos
from lista import ListaDoblementeLigada

print("Bienvenido a mi proyecto final de estructura de datos")

while True:
    print("---------------MENU---------------")
    print("Selecciona la opción que quieres testear a continuación")
    print("1. Arbol Binario - Tareas")
    print("2. Grafos - Viajes")
    print("3. Arreglos - Cafeteria")
    print("4. Listas Doblemente liadas - Bilbioteca")
    print("5. Salir")
    test = int(input("Introduce la opción que deseas testear: "))
    if test == 1:
        arbol = ArbolBinario()
        res = int(input("¿Cuántas tareas desea ingresar?: "))
        for i in range(res):
            value, tarea = input("Ingresa la prioridad de la tarea y el nombre separados por un espacio: ").split(maxsplit=1)
            arbol.insertar(int(value), tarea)
        print("\nRecorrido en Preorden:")
        arbol.preorden(arbol.raiz)
        print("\nRecorrido en Inorden:")
        arbol.inorden(arbol.raiz)
        print("\nRecorrido en Postorden:")
        arbol.postorden(arbol.raiz)
        buscar_tarea = "S"
        while buscar_tarea == "S":
            busqueda = int(input("¿Qué tarea te gustaría buscar?(introduce la prioridad): "))
            nodo_encontrado = arbol.buscar(busqueda)
            if nodo_encontrado:
                print(f"Nodo encontrado: Prioridad {nodo_encontrado.prioridad}, Tarea: {nodo_encontrado.descripcion}")
            else:
                print(f"No se encontró una tarea con la prioridad {busqueda}")
            buscar_tarea = input("¿Desea buscar otra tarea? (S/N): ").upper()
        eliminar_tarea = "S"
        while eliminar_tarea == "S":
            eliminar = int(input("Ingresa la prioridad de la tarea que deseas eliminar: "))
            arbol.eliminar(eliminar)
            print("\nRecorrido preorden después de eliminar:")
            arbol.preorden(arbol.raiz)
            eliminar_tarea = ("¿Deseas seguir eliminando tareas?(S/N): ").upper()
    
    elif test == 2:
        grafo = Grafo()
        ciudades = ["Ciudad A", "Ciudad B", "Ciudad C", "Ciudad D", "Ciudad E"]
        for ciudad in ciudades:
            grafo.agregar_nodo(ciudad)
        
        grafo.agregar_arista("Ciudad A", "Ciudad B")
        grafo.agregar_arista("Ciudad A", "Ciudad C")
        grafo.agregar_arista("Ciudad B", "Ciudad D")
        grafo.agregar_arista("Ciudad C", "Ciudad E")
        grafo.agregar_arista("Ciudad D", "Ciudad E")

        # Realizar un recorrido DFS desde "Ciudad A"
        inicio = "Ciudad A"
        recorrido = grafo.dfs(inicio)
        print(f"Recorrido DFS desde {inicio}: {recorrido}")

    elif test == 3:      
        gestion = GestionPedidos()
        while True:
            print("\n--- Gestión de pedidos de la cafetería ---")
            print("1. Agregar pedido")
            print("2. Procesar bebida")
            print("3. Procesar comida")
            print("4. Mostrar pedidos actuales")
            print("5. Salir de la gestión de pedidos")
            opcion_cafeteria = input("Elige una opción: ")
            
            if opcion_cafeteria == "1":  # Agregar pedidos
                tipo = input("Escribe si es bebida o comida: ").lower()
                if tipo in ["bebida", "comida"]:
                    producto = input("Ingresa el nombre del producto: ")
                    gestion.agregar_pedido(tipo, producto)
                else:
                    print("Tipo no válido. Intenta de nuevo.")
            
            elif opcion_cafeteria == "2":  # Procesar bebida
                gestion.procesar_bebida()
            
            elif opcion_cafeteria == "3":  # Procesar comida
                gestion.procesar_comida()
            
            elif opcion_cafeteria == "4":  # Mostrar pedidos actuales
                gestion.mostrar_pedidos()
            
            elif opcion_cafeteria == "5":  # Salir de la opción 3
                print("Saliendo de la gestión de pedidos...")
                break
            
            else:
                print("Opción no válida. Intenta de nuevo.")
            


