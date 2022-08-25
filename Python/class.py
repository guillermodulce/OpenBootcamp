class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "El coche es color {}, tiene {} ruedas y {} puertas. \nSu velocidad máxima es {} km/h, y su cilindrada es {} cc.".format( self.color, self.ruedas, self.puertas, self.velocidad, self.cilindrada )

coche = Coche("verde", 4, 3, 280, 1800)
print(coche)
