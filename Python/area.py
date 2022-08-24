def area_triangulo(altura, base):
    
    return ((altura * base) / 2)

a = int(input('Ingrese la altura del triangulo: '))
b = int(input('Ingrese la base del triangulo: '))

def area_circulo(radio: float) -> float:
    return (3.141592653*(radio**2))
    
r = int(input('Ingrese el radio del circulo: '))

print(f'El area del triangulo es {area_triangulo(a, b)}')
print(f'El area del circulo es {area_circulo(r)}')
