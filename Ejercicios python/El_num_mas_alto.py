
num_1 = int(input("Introduce un Numero: "))

num_2 = int(input("Introduce el segundo Numero: "))

def DevuelveMax():
    if num_1 > num_2:
        print("El primer numero: ",num_1," es el mayor")
    elif num_1 < num_2:
        print("El segundo numero: ",num_2," es el mayor")
    else:
        print("Son iguales")

