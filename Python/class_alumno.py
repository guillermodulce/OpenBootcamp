class Alumno():
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
               print("Nombre: ",self.nombre)
               print("Nota: ",self.nota)
 
 
    def aprobación(self):
            if self.nota < 5:
                print("Reprobado")
            else:
                print("Aprobado")
                
alumno=Alumno()
alumno.inicializar("Valentino Dulce", 9)

alumno.imprimir()
alumno.aprobación()
