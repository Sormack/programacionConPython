import numpy as np
from sympy import symbols, simplify, expand
import math 

def interpolacionLineal(xCero, yCero, xUno, yUno, x):
    if xCero == xUno:
        raise ValueError("Los valores de x0 y x1 no pueden ser iguales.")
    y = yCero + (x - xCero) * (yUno - yCero) / (xUno - xCero)
    return y

def valoresDeInterplacionLineal():
    print("Ingresa los dos puntos en forma x,y")
    puntoCero = input("Ingresa el punto A: ")
    puntoCero = puntoCero.split(",")
    xCero = float(puntoCero[0])
    yCero = float(puntoCero[1])
    puntoDos = input("Ingresa el punto C: ")
    puntoDos = puntoDos.split(",")
    xUno = float(puntoDos[0])
    yUno = float(puntoDos[1])
    xInterpolado = float(input("Ingresa el valor a interpolar: "))
    return xCero,yCero,xUno,yUno,xInterpolado

def valoresInterPolacionCuadrantica():
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
    return puntoXCero,puntoYCero,puntoXUno,puntoYUno,puntoXDos,puntoYDos 

def matriz(puntoXCero,puntoYCero,puntoXUno,puntoYUno,puntoXDos,puntoYDos):
    coeficientes = np.array([[puntoXCero * puntoXCero, puntoXCero, 1], [puntoXUno*puntoXUno, puntoXUno, 1], [puntoXDos*puntoXDos,puntoXDos, 1]])
    constantes = np.array([puntoYCero, puntoYUno, puntoYDos])
    return coeficientes,constantes

def resolverSistemaDeEcuaciones(coeficientes, constantes):
    soluciones = np.linalg.solve(coeficientes, constantes)
    return soluciones

def resultadoInterpolacionCuadrantica(soluciones):
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
    print("Ingresa el numero correspindiente para escojer un Metodo de Interpolacion")

def valoresParaPolinomioLagrange():
    valoresX = input("Ingresa los valores de x en forma de xn,x4,x3...: ")
    valoresY = input("Ingresa los valores de y en forma de yn,y4,y3...: ")
    valoresX = valoresX.split(",")
    valoresY = valoresY.split(",")    
    return valoresX,valoresY

def polinomioLagrange(valoresX, valoresY):
    x = symbols('x')
    polinomioDeLagrange = 0

    for i in range(len(valoresX)):
        term = valoresY[i]
        for j in range(len(valoresX)):
            if i != j:
                term *= (x - valoresX[j]) / (valoresX[i] - valoresX[j])
        polinomioDeLagrange += term
    return simplify(expand(polinomioDeLagrange))

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

def resultadoMinimosCuadrados(x,y,r,m,b):
    print("Los valres para x son: ",x)
    print("Los valores para y son: ",y)
    print("El coeficiente de correlacion es: ",r)
    print("La ecuacion queda como:")
    print("y=",m,"x", b)

tipoDeMetodo = int(input("1 = Interplacion Lineal \n2 = interpolacion Cuadrantica\n3 = Polinomio de Lagrange\n4 = Minimos Cuadrados\nMetodo a escojer: "))

if(tipoDeMetodo == 1):
    valores = valoresDeInterplacionLineal()
    resultadoDeLaInterpolacion = interpolacionLineal(valores[0],valores[1],valores[2],valores[3],valores[4])
    print("Para x =",valores[4]," el valor interpolado es:",resultadoDeLaInterpolacion)
elif(tipoDeMetodo == 2):
    valores = valoresInterPolacionCuadrantica()
    valorDeMatriz = matriz(valores[0],valores[1],valores[2],valores[3],valores[4],valores[5])
    solucion = resolverSistemaDeEcuaciones(valorDeMatriz[0],valorDeMatriz[1])
    resultadoInterpolacionCuadrantica(solucion)
elif(tipoDeMetodo==3):
    valoresLagrange = valoresParaPolinomioLagrange()
    valoresParaX = valoresLagrange[0]
    valoresParaY = valoresLagrange[1]
    cantidadPuntos = len(valoresParaX)
    listaX = []
    listaY = []
    i = 0
    l = 0
    while(i != cantidadPuntos):
        i += 1  
        for j in valoresParaX:
            x = valoresParaX.pop()
            x = int(x)
            listaX.append(x)
            
    while(l != cantidadPuntos):
        l += 1  
        for h in valoresParaY:
            y = valoresParaY.pop()
            y = int(y)
            listaY.append(y)
    ecuacionPolinomica = polinomioLagrange(listaX,listaY)
    print("El polinomio de Lagrange es: ",ecuacionPolinomica)
elif(tipoDeMetodo == 4):
    x = np.array([178, 160 , 183, 152, 168,178,188,165,157,170,165,173])
    y = np.array([69.8, 67.5, 81, 60.8, 70.2,75.6,80.1,72,59.4,65.3,62.6,68.4])
    resultado = minimosCuadrados(x,y)
    r = resultado[0]
    m = resultado[1]
    b = resultado[2]
    resultadoMinimosCuadrados(x,y,r,m,b)
else:
    print("El valor introducido no es valido")