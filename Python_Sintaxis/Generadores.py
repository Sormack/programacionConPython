## Se extraen valores de una funcion y se almacena
## objetos iterables o que se pueden recorrer
## Los valores se almacenan de uno en uno
## Cada vez que el generador almacen un valor este permanece 
## En un estado pausado hasta que se solicita el siguiente

print("Funcion tradicional")

def generarPares(Limite):
    num = 1
    miLista = []

    while num < Limite:
        miLista.append(num*2)
        num +=1
    return miLista

print(generarPares(10))


print("Generador")

def generarPares(Limite):
    num = 1
    
    while num < Limite:
        yield num*2
        num +=1

devuelvePares = generarPares(10)

## Devuelve el primer elemento
print(next(devuelvePares))

for i in devuelvePares:
    print(i)
















