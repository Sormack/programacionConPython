def interpolacionLineal(xCero, yCero, xUno, yUno, x):
    """
    Realiza interpolación lineal para encontrar el valor correspondiente a x.

    Parámetros:
    - x0, y0: Coordenadas del primer punto conocido.
    - x1, y1: Coordenadas del segundo punto conocido.
    - x: Valor para el cual deseamos interpolar y.

    Retorna:
    - El valor interpolado correspondiente a x.
    """
    if xCero == xUno:
        raise ValueError("Los valores de x0 y x1 no pueden ser iguales.")

    # Fórmula de interpolación lineal: y = y0 + (x - x0) * (y1 - y0) / (x1 - x0)
    y = yCero + (x - xCero) * (yUno - yCero) / (xUno - xCero)
    return y

xCero = float(input("Ingresa el valor x0: "))
yCero = float(input("Ingresa el valor y0: "))
xUno = float(input("Ingresa el valor x1: "))
yUno = float(input("Ingresa el valor y1: "))

xInterpolado = float(input("Ingresa el valor a interpolar: "))

resultadoDeLaInterpolacion = interpolacionLineal(xCero, yCero, xUno, yUno, xInterpolado)
print(f"Para x = {xInterpolado}, el valor interpolado es: {resultadoDeLaInterpolacion}")





