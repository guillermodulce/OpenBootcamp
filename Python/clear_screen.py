# Modulo para limpiar Pantalla en Python

"""Este modulo para python si lo importas en tu proyecto podrás limpiar pantalla, que debería funcionar para Windows, Mac y Linux."""

import os, sys

def clear():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')
        
if __name__ == '__main__':
    clear()

# Se puede utilizar de esta forma:

# El modulo debe de estar en el mismo directorio
# import cleaner

# Asi lo ejecutas en tu código, y limpia la pantalla
# cleaner.cleaning()

# Tambien puede ser de esta manera:

# Si lo importas de esta manera es mas simple
# from cleaner import cleaning

# Simplemente llamas a la función sin anteponer el nombre del modulo
cleaning()
