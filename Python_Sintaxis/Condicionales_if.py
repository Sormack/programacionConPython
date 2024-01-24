print("Sintema para calcular el promedio de un alumno.")

nombre = input("Para comenzar, Cual es tu nombre?: ")

matematicas = int(input(nombre + "Cual es tu califacion en matematicas?: "))
quimica = int(input(nombre + "Cual es tu calificacion en quimica? "))
biologia= int(input(nombre + "Cual es tu calificacion en biologia: "))

promedio = (matematicas + quimica + biologia)/3
promedio = int(promedio)## Para que el resultado sea en entero

if promedio >= 6:
    print('Felicidades ' + nombre + ' "aprobaste" con un promedio de:', promedio)

print("Fin.")
    
