def bisiesto():
    year = int(input("Ingresa un año: "))


    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return f"El año {year} es bisiesto"
    else:
        return f"El año {year} no es bisiesto"

print(bisiesto())
