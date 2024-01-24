## Los diccionarios {}

midiccionario = {"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","Espana":"Madid"}
print(midiccionario,"\n")

## Para agregar otro elemento
midiccionario["Italia"] = "Lisboa"
print(midiccionario,"\n")

## Para sobreescribir elementos
midiccionario["Italia"] = "Roma"
print(midiccionario,"\n") 

## Para eliminar elementos
del midiccionario["Reino Unido"]
print(midiccionario,"\n")

## Dar valores de una tupla a un diccionario
Mitupla = ["Espana", "Francia", "Reino Unido", "Alemania"]
Midiccionario = {Mitupla[0]:"Madrid",Mitupla[1]:"Paris",Mitupla[2]:"Londres",Mitupla[3]:"Berlin"}
print(Midiccionario,"\n")

## Para el valor asignado a una clave 
print(Midiccionario["Francia"],"\n")

## Para guardar una tupla dentro de un diccionario
MiDiccionario = {23:"Jordan","Nombre":"Michael", "Equipo":"Chicago", "Anillos":[1991,1992,1993,1996,1997,1998]}
print(MiDiccionario["Anillos"],"\n")

## Para guardar un diccionario dentro de otro diccionario
MiDiccionario = {23:"Jordan","Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(MiDiccionario["Anillos"],"\n")

## Para imprimir las claves de in diccionario
print(MiDiccionario.keys(),"\n")

## Para imprimir los valores de un diccionario
print(MiDiccionario.values(),"\n")

## Para imprimir la longitud de un diccionario
print(len(MiDiccionario))



















