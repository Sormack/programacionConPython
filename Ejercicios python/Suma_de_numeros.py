
num = int(input("Introduce un numero entero : "))

while num > 0:
    num_2 = int(input("Introduce un numero entero: "))
    num +=num_2
    
    if num <= 0 or num_2 <= 0:
        print("La suma de los numeros es: ",num)
        break 

#! Forma dos

num_1 = int(input("Introduce un numero entero : "))
suma = 0

while num_1 > 0:
    suma += num_1
    num_1 = int(input("Introduce un numero entero : "))

print("La suma de los numeros es: ",num_1)


