def numprimo():
    num=int(input("Ingrese un numero: "))

    if num > 1:
        cont=0
        i=2
        while i<num and cont==0:
            resto=num%i
            
            if resto==0:
                cont+=1
            i+=1
        if cont==0:
            return f"El {num} es un número primo"
        else:
            return f"El {num} no es un número primo"
    
print(numprimo())
