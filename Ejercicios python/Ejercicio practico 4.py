print("Esto es una calculadora")

print("Menu de opciones: ")

print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Divicion")
print("5. Divicion Entera")
print("6. Exponente")
print("7. Modulo o Resto")

opc = int(input("Introduce la opcion deseada: "))

if opc == 1:
    print("Se selecciono el Modo suma \n")
    num = int(input("Introduce un numero entero: "))
    num += int(input("Introduce el segundo numero: "))
    print("El resultado de la suma es de: ",num)

if opc == 2:
    print("Se selecciono el Modo Resta")
    num = int(input("Introduce un numero entero: "))
    num -= int(input("Introduce el segundo numero: "))
    print("El resultado de la Resta es de: ",num)

if opc == 3:
    print("Se selecciono el Modo Multiplicacion")
    num = int(input("Introduce un numero entero: "))
    num *= int(input("Introduce el segundo numero: "))
    print("El resultado de la Multiplicaion es de: ",num)

if opc == 4:
    print("Se selecciono el Modo Divicion")
    num = int(input("Introduce un numero entero: "))
    num /= int(input("Introduce el segundo numero: "))
    print("El resultado de la suma es de: ",round (num, 2 ))

if opc == 5:
    print("Se selecciono el Modo Divicion Entera")
    num = int(input("Introduce un numero entero: "))
    num //= int(input("Introduce el segundo numero: "))
    print("El resultado de la Divion Entera es de: ",num)

if opc == 6:
    print("Se selecciono el Modo Exponente")
    num = int(input("Introduce un numero entero: "))
    num **= int(input("Introduce el segundo numero: "))
    print("El resultado del Modo Exponente es de: ",num)

if opc == 7:
    print("Se selecciono el Modo Modulo o Resto")
    num = int(input("Introduce un numero entero: "))
    num %= int(input("Introduce el segundo numero: "))
    print("El resultado del Modulo o Resto es de: ",num)

























    
