from Bebida import Bebida

class Alcohol(Bebida):
    def __init__(self, nombre, marca, disponible, grado, tipo):
        super().__init__(nombre, marca, disponible)
        self.grado = grado
        self.tipo = tipo

    def mostrar(self):
        print(f"-- {self.nombre} ---\nMarca: {self.marca}\nDisponible: {self.disponible}\nGrado: {self.grado}°\nTipo: {self.tipo}\n")