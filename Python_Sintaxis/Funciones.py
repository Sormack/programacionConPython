## Sirven para reutilizar codigo

## Esta es una declaracion

def mensaje():
    print("Esto va dentro de una funcion 'def'")

## Se tiene que llamar la funcion para dar el print

mensaje()

print("----------------------")

print("Sin parametros ()")

def suma():
    num_1 = 5
    num_2 = 7
    print(num_1 + num_2)

suma()

print("-----------------")

print("Con parametros")

def suma(num_1 , num_2):
    print(num_1 + num_2)

## Al hacer la llamda hay que darle los valores a la funcion reutilizada

suma(5,7)
suma(2,3)
suma(35,358)

print("----------------------")
print(" Funcion def con return")
def suma(num_1 , num_2):
    resultado = num_1 + num_2
    return resultado

print(suma(5,7))
print(suma(2,3))
print(suma(35,358))


