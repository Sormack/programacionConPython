## Para crea listas []

Milista = ["Maria","Pepe","Marta","Javi"]

print(Milista[:],"\n")

## Para accerder a un nombre en concreto
print(Milista[2],"\n")

## Al introducir un numero negativo accede desde el final
print(Milista[-2],"\n")

## Para acceder a una porcion de lista
print(Milista[0:3],"\n")

## Accede a los dos ultimos elementos de la lista
print(Milista[2:],"\n")

## Para agregar un elemento mas a la lista y lo agrega al final
Milista.append("Sandra")
print(Milista[:], "\n")

## Para agrar un elemento en la lista en un lugar en concreto
Milista.insert(2,"Nesi")
print(Milista[:],"\n")

## Para agregar varios elementos a una lista
Milista.extend(["Ana","Lucia"])
print(Milista[:],"\n")

## Para saber en que posicion se encuentra un elemento de la lista
print(Milista.index("Javi"),"\n")

## Para saber si hay un elemento en mis lista
print("Pepe" in Milista,"\n")

## Para eliminar un elemento en la lista
Milista.remove("Ana")
print(Milista[:], "\n")

## Para eliminar el ultimo elemento de la lista
Milista.pop()
print(Milista[:])





















