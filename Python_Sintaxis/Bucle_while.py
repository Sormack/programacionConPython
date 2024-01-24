import math

i = 1

while i <= 10:
    print("Ejecuciion", i )
    i += 1

print("Fin de la ejecucucion \n")

edad = int(input("Introduce tu edad: "))

while edad < 5 or edad > 100:
    print("Introduciste una edad incorrecta")
    edad = int(input("Introduce tu edad: "))

print("La edad es correcta" + str(edad))

print("Calculo de una raiz cuadrada: ")

num = int(input("Introduce un numero: "))

intentos = 0

while num < 0:
    print("No se puede hallar la raiz de un numero negativo")

    if intentos == 2:
        print("Has consumido demaciaos intentos")
        breack;
    
    num = int(input("Introduce un numero: "))
    if num < 0:
        intentos += 1

if intentos < 2:
    solucion = math.sqrt(num)
    print("La raiz cuadrada de " + str(num) + " es: " + str(solucion))






