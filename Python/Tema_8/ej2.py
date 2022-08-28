from pickle import *

class Vehículo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return self.marca + " " + self.modelo + " " + self.color

auto = Vehículo("Peugeot", "206", "verde")

file = open('objeto', 'w+b')

dump(auto, file)

file.seek(0)
otro_auto = load(file)
file.close()
