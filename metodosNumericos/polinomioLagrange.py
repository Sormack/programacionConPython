import numpy as np
import sympy as sym

xi = np.array([1,3,5])
y = np.array([2,5,3])

n = len(xi)
x = sym.Symbol('x')

polinomio = 0

divisor = np.zeros(n,dtype = float)

for i in range(0,n,1):
    numerador = 1
    denominador = 1 
    for j in range(0,n,1):
        if(j != i ):
            numerador = numerador*(x-xi[j])
            denominador = denominador*(xi[i]-xi[j])
        termino = numerador / denominador
        polinomio = polinomio + termino*y[i]
        divisor[i] = denominador

simplificacionPolinomi = polinomio.expand()

print(polinomio)
print("---------------------")
print(simplificacionPolinomi)
