print("Cual de los tres numeros es el mas grande")

num_1 = int(input("Introduce un numero entero: "))

num_2 = int(input("Introduce un numero entero: "))

num_3 = int(input("Introduce un numero entero: "))

if num_1 > num_2 and num_1 > num_3:
    print("El numero: ",num_1,"Es le mayor de los 3")

if num_2 > num_1 and num_2 > num_3:
    print("El numero: ",num_2,"Es le mayor de los 3")

if num_3 > num_1 and num_3 > num_2:
    print("El numero: ",num_3,"Es le mayor de los 3")
