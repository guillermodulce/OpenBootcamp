from functools import reduce

def impares(lista): 
    res = list(filter((lambda x: x % 2), lista)) 
    print(res)
    res = reduce( (lambda x, y: x + y), res) 
    print(res)

lista = list(range(200))

impares(lista)