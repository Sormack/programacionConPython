## La i puede ser cualquier variable

## Ejecuta el print por la cantidad de variables en la lista

for i in [1,2,3]:
    print("Hola \n")

## Al imprimir la vaiable i imprimira la cantidad de variables en la lista 

for i in [1,2,3]:
    print(i,"\n")

contador = 0

miEmail = input("Introduce tu direccion de correo: ")

for i in miEmail:
    if(i == "@" or i == "."):
        contador = contador + 1 

if contador == 2:
    print("El email es correcto")
else:
    print("El email es incorrecto")



















