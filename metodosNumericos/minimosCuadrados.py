import numpy as np
import math 
def minimosCuadrados(x,y):
    sumX = float(np.sum(x))
    sumY = np.sum(y)
    sumXY = np.sum(x * y)
    sumaCaudradoX = 0
    sumaCuadradoY = 0
    sumaCaudradoX = float(sumaCaudradoX)
    sumaCuadradoY = float(sumaCuadradoY)
    n = len(x)
    n = float(n)

    for i in x:
        cuadradoDeX = i * i
        sumaCaudradoX += cuadradoDeX

    for i in y:
        cuadradoDeY = i * i
        sumaCuadradoY += cuadradoDeY

    raizUno =  n * (sumaCaudradoX) - (sumX * sumX)
    raizDos =  n * (sumaCuadradoY) - (sumY * sumY)

    raizUno = math.sqrt(raizUno)
    raizDos = math.sqrt(raizDos)

    nominador = n*(sumXY) - sumX * sumY 
    denominador = raizUno * raizDos

    coeficienteCorrelacion = round(nominador / denominador,4)

    pendienteNumerador = n * sumXY - sumX * sumY
    pendienteDenominador = n * sumaCaudradoX - sumX * sumX

    pendiente = round(pendienteNumerador / pendienteDenominador,4)

    ordenadaAlOrigenNumerador = sumY * sumaCaudradoX - sumX * sumXY
    ordenadaAlOrigenDenominador = n * sumaCaudradoX - sumX * sumX

    ordenadaAlOrigen = round(ordenadaAlOrigenNumerador / ordenadaAlOrigenDenominador,4)
    return coeficienteCorrelacion,pendiente,ordenadaAlOrigen

x = np.array([178, 160 , 183, 152, 168,178,188,165,157,170,165,173])
y = np.array([69.8, 67.5, 81, 60.8, 70.2,75.6,80.1,72,59.4,65.3,62.6,68.4])

resultado = minimosCuadrados(x,y)
r = resultado[0]
m = resultado[1]
b = resultado[2]

print("Los valres para x son: ",x)
print("Los valores para y son: ",y)
print("El coeficiente de correlacion es: ",r)
print("La ecuacion queda como:")
print("y=",m,"x", b)

