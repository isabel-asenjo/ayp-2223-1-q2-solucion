from Bebida import Bebida

class Refresco(Bebida):
    def __init__(self, nombre, marca, disponible, azucar, sabor):
        super().__init__(nombre, marca, disponible)
        self.azucar = azucar
        self.sabor = sabor

    def mostrar(self):
        print(f"-- {self.nombre} ---\nMarca: {self.marca}\nDisponible: {self.disponible}\nAzúcar: {self.azucar}g\nSabor: {self.sabor}\n")