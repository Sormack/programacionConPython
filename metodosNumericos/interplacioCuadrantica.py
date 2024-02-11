import numpy as np

def resolver_sistema_ecuaciones(coeficientes, constantes):
    soluciones = np.linalg.solve(coeficientes, constantes)
    return soluciones

print("Ingresa los 3 puntos en forma x,y")

puntoA = input("Ingresa el punto A: ")
puntoA = puntoA.split(",")
puntoXCero = float(puntoA[0])
puntoYCero = float(puntoA[1])

puntoB = input("Ingresa el punto B: ")
puntoB = puntoB.split(",")
puntoXUno = float(puntoB[0])
puntoYUno = float(puntoB[1])

puntoC = input("Ingresa el punto C: ")
puntoC = puntoC.split(",")
puntoXDos = float(puntoC[0])
puntoYDos = float(puntoC[1])

coeficientes = np.array([[puntoXCero * puntoXCero, puntoXCero, 1], [puntoXUno*puntoXUno, puntoXUno, 1], [puntoXDos*puntoXDos,puntoXDos, 1]])
constantes = np.array([puntoYCero, puntoYUno, puntoYDos])

soluciones = resolver_sistema_ecuaciones(coeficientes, constantes)

print(f"Las soluciones son: {soluciones}")
valorA = round(soluciones[0],4)
valorB = round(soluciones[1],4)
valorC = round(soluciones[2],4)


print("El valor de a = ",valorA)
print("El valor de b = ",valorB)
print("El valor de c = ",valorC)

print("La formula cuadrantica quedarria como:")
print("y = ",valorA,"x^2",valorB,"x",valorC)

valorDeInterpolacion = float(input("Ingres el valor para la interpolacion: "))
interpolado = valorA*(valorDeInterpolacion * valorDeInterpolacion) + valorB * valorDeInterpolacion + valorC

print("El punto es: ",valorDeInterpolacion,",",interpolado)

