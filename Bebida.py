class Bebida():
    def __init__(self, nombre, marca, disponible):
        self.nombre = nombre
        self.marca = marca
        self.disponible = disponible

    def mostrar(self):
        print(f"-- {self.nombre} ---\nMarca: {self.marca}\nDisponible: {self.disponible}\n")