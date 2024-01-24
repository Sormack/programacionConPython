print("Introduce dos numeros a comparar: ")

num_1 = int(input("Introduce el primer Numero: "))

num_2 = int(input("Introduce el segundo Numero: "))

print("Los numeros a comparar son: ", num_1 , 'y' , num_2)

if num_1 != num_2:
    print("Es diferente")
else:
    print("No son diferentes")

if num_1 > num_2:
    print("Es mayor")
else:
    print("No es mayor")

if num_1 >= num_2:
    print("Es mayor o igual")
else:
    print("No es mayor o igual")
