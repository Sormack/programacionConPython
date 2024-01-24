print("Cuenta de numeros Positio")

i = 1

while i > 0:
    num_1 = int(input("Introduce un numero positivo entero: "))
    
    if num_1 >= 1:
        num_2 = int(input("Introduce un numero positivo entero: "))
    
    if num_1 == num_2 or num_2 < num_1:
        print("Se introdujo un numero igual o menor al anterior")
        break



