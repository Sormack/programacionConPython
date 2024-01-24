## Al poner un " * " antes del argumento de una funcion indicamos
## que se recibira un numero indeterminados de elemtos
## y esos elementos los recibira en forma de tupla
def devuelve_ciudades(*Ciudades):
    for elementos in Ciudades:
        #for subElemento in elementos:
            yield from elementos
        

Ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona","Bilbao","Valencia")

print(next(Ciudades_devueltas))

print(next(Ciudades_devueltas))

