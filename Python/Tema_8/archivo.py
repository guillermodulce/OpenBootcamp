file = open('archivo.txt', 'w')
file.write('Esta es la primera linea de mi archivo.\n')
file.close()

file = open('archivo.txt', 'r+')
file.readline()
file.write('Ahora agregamos esta segunda linea.\n')
file.close()