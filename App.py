from Alcohol import Alcohol
from Refresco import Refresco

class App():
    def __init__(self):

        # estructura con almacén viejo
        self.almacen_desactualizado = {
            "Alcoholica":
            [
            { "nombre": "Linaje", "marca": "Santa Teresa", "grado": 40, "tipo": "Ron", "disponible": True },
            { "nombre": "Black Label 18", "marca": "Jonnie Walker", "grado": 43, "tipo": "Whisky", "disponible": True },
            { "nombre": "Solera Verde", "marca": "Polar", "grado": 6, "tipo": "Cerveza", "disponible": True }
            ],

            "Refresco":
            [
            { "nombre": "Maltin Polar", "marca": "Polar", "azucar": 7, "sabor": "Malta", "disponible": True },
            { "nombre": "Pepsi", "marca": "Pepsico", "azucar": 7, "sabor": "Cola", "disponible": True },
            { "nombre": "Chinoto", "marca": "The Coca-Cola Company", "azucar": 4, "sabor": "Limon", "disponible": True }
            ] 
        }

        # estructura con bebidas del almacén como objetos
        self.almacen = { "Alcohol": [], "Refresco": [] }


    def cargar_bebidas(self):
        """
        Método para transofmar la información del almacén viejo en objetos
        """

        for tipo, lista in self.almacen_desactualizado.items():
            for bebida in lista:
                if tipo == "Alcoholica":
                    b = Alcohol(bebida["nombre"], bebida["marca"], bebida["disponible"], bebida["grado"], bebida["tipo"])
                else:
                    b = Refresco(bebida["nombre"], bebida["marca"], bebida["disponible"], bebida["azucar"], bebida["sabor"])
                
                self.almacen["Refresco" if isinstance(b, Refresco) else "Alcohol"].append(b)


    def ver_inventario(self):
        print("INVENTARIO ----")
        for tipo, bebidas in self.almacen.items():
            print(f"\n{tipo.upper()} >>>\n")
            for bebida in bebidas:
                bebida.mostrar()
    

    def eliminar_producto(self):
        print("MÓDULO DE ELIMINACIÓN DE PRODUCTOS ----")
        # tengo una lista auxiliar que va a guardar a todos los productos, sin clasificarlos por tipo. Esto me va a ayudar a numerarlos y encontrar más rápido al que se vaya a eliminar
        inventario_aux = [bebida for tipo, bebidas in self.almacen.items() for bebida in bebidas]
        for i, bebida in enumerate(inventario_aux):
            print(f"{i + 1}. {bebida.nombre}")
        
        print()

        opcion = input("Ingrese el número del producto que desea eliminar: ")

        while not opcion.isnumeric() or int(opcion) not in range(1, len(inventario_aux) + 1):
            opcion = input("Ingreso inválido. Ingrese el número del producto que desea eliminar: ")
        
        inventario_aux[int(opcion) - 1].disponible = False

        print(f"El producto {inventario_aux[int(opcion) - 1].nombre} ha sido eliminado del inventario.")


    def estadisticas(self):
        print("MÓDULO DE ESTADÍSTICAS ----\n")

        self.mayor_grado_alcoholico()

        print()

        self.menor_cantidad_azucar()

        print()

        self.marcas_comunes()


    def mayor_grado_alcoholico(self):
        # voy a ir reemplazando lo que está en la variable mayor_grado a medida que vaya encontrando alcoholes con mayor grado alcohólico
        mayor_grado = ("", 0)
        for tipo, bebidas in self.almacen.items():
            for bebida in bebidas:
                if isinstance(bebida, Alcohol) and bebida.grado > mayor_grado[1]: # la built in function "isinstance" sirve para validar si un objeto viene de una clase en específico
                    mayor_grado = (bebida.nombre, bebida.grado)
        
        print(f"* Bebida alcoholica con mayor grado: {mayor_grado[0]} ({mayor_grado[1]}°)")

    
    def menor_cantidad_azucar(self):
        # voy a ir reemplazando lo que está en la variable menor_azucar a medida que vaya encontrando refrescos con menos gramos de azucar
        menor_azucar = ("", 1000)
        for tipo, bebidas in self.almacen.items():
            for bebida in bebidas:
                if isinstance(bebida, Refresco) and bebida.azucar < menor_azucar[1]:
                    menor_azucar = (bebida.nombre, bebida.azucar)
        
        print(f"* Refresco con menor cantidad de azúcar: {menor_azucar[0]} ({menor_azucar[1]}g)")

        
    def marcas_comunes(self):
        print("* Marcas con bebidas en ambas categorías:")

        # hago un diccionario con las bebidas separadas por marca
        marcas = {}
        for tipo, bebidas in self.almacen.items():
            for bebida in bebidas:
                if bebida.marca in marcas:
                    marcas[bebida.marca].append(bebida)
                else:
                    marcas[bebida.marca] = [bebida]

        # reviso en qué marcas hay bebidas de tipos diferentes (o sea, de la clase Alcohol y de la clase Refresco)
        for marca in marcas:
            if len(marcas[marca]) > 1 and any([type(marcas[marca][0]) != type(bebida) for bebida in marcas[marca][1:]]):
                print("     ", marca)
                for bebida in marcas[marca]:
                    print(f"        - {bebida.nombre}")
                print()



    def start(self):
        self.cargar_bebidas()
        while True:
            print("PLATAFORMA ADMINISTRATIVA DEL BODEGÓN\n1. Ver inventario\n2. Eliminar producto\n3. Estadísticas\n4. Salir\n")
            opcion = input("Ingrese una opción: ")
            while not opcion.isnumeric() or int(opcion) not in range(1, 5):
                opcion = input("Ingreso inválido. Ingrese una opción: ")

            print()

            if opcion == "1":
                self.ver_inventario()
            elif opcion == "2":
                self.eliminar_producto()
            elif opcion == "3":
                self.estadisticas()
            else:
                print("Hasta pronto!")
                break

            print()