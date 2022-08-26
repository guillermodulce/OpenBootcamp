from distutils.command.clean import clean
from calculadora import *

a, b = (10, 4)
    
print( "{} + {} = {}".format(a, b, suma(a, b) ) )
print( "{} - {} = {}".format(a, b, resta(a, b) ) )
print( "{} * {} = {}".format(a, b, multiplicación(a, b) ) ) 
print( "{} / {} = {}".format(a, b, división(a, b) ) )
clean