import re

países = input ("Ingrese una lista de países, separados por comas:\n  ")
países = países.replace(" ", "")

lista = [pais for pais in países.split(",")]

#print(sorted(set(lista)))

print (",".join(sorted(list(set(lista)))))



