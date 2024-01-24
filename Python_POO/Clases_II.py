class coche():
    ## Estado inicial para que los objetos tengan toda 
    ## las caracteristicas desde el principio
    ## Constructor ## Encapsulamiento
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos
        if (self.__enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"    
        
    
    def estado(self):
        print("El coche tiene: ", self.__ruedas,"ruedas.Um ancho: ",self.__anchoChasis,"y un largo de:",
            self.__largoChasis,"\n")

## para acceder a una propiedad de una cles es necesario 
# el nombre del objeto.nombre del atributo
miCoche = coche() ## Instanciar una clase
## Siempre hay que darle un parametro
## Las llamadas dentro del metodo arrancar hay dar un print
print(miCoche.arrancar(True))

## EL metodo estado va sin print ya que en el metodo lo hace
miCoche.estado()

print("Creacion del segundo objeto o Instancia \n")

miCoche2 = coche()

print(miCoche2.arrancar(False))

## Para evitar cambios fuera la clases hay que encapsularlas
## Se pueden hacer cambios dentro de la clases pero no desde fuera de ellas
miCoche2.ruedas= 2 

miCoche2.estado()
