## Las tuplas son inmutables o no se pueden modificar
## No permite anadir, eliminar, mover elementos
## Permite comprobar si un elemento se encuentra en la tupla
## Las tuplas ()

mitupla = ("Juan",13,1,1995)
print(mitupla[1],"\n")
## Para convertir una tupla a lista
milista = list(mitupla)
print(milista,"\n")

milista = ["Juan",13,1,1995]
## Para convertir una lista a tupla
mitupla = tuple(milista)
print(mitupla,"\n")

## Para saber si un elemento esta dentro de la tupla
print("Juan" in mitupla,"\n")

## Para saber cuantos elementos iguales hay
print(mitupla.count(13),"\n")

## Para saber la cantidad de elementos
print(len(mitupla),"\n")

## Para una tupla con un unico elemento "Unitaria"
Mitupla = ("Juan",)
print(len(Mitupla),"\n")

## Desempaquetado de tuplas
nombre, dia, mes, age = mitupla
print(nombre)
print(dia)
print(age)
print(mes)
