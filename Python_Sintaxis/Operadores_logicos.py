# Conjuncion con "and"
print("Conjuncion con (and)")

num_uno = int(input("Escribe un mumero mayor a 2 y menor a 5: "))

if num_uno > 2 and num_uno < 5:
    print("El numero ", num_uno, "Cumple la condicon.\n")
else:
    print("El numero ", num_uno, "No cumple la condicon.\n")


# Disyuncion "or"

print("Disyuncion(or)")

palabra = input("Palabra a cumplir con la condicion escribe si o yes: ")

if palabra =="si" or palabra=="yes":
    print("La condicion se ha cumplido.\n")
else:
    print("La condicon no se ha cumplido.\n")


# Negacion "not"

print("Negacion (not)")

num_uno = int(input("Introduce un numero igual a 5: "))
if not num_uno == 5:
    print("\n El numero es diferente de 5 y si cumple la condicion.\n")
else:
    print("\n El numero es igual a cinco y no cumple la condicion.\n")
    
