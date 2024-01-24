class coche():
    ## propiedades de un objeto
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False
## Comportamientos de una clase
## simpre el valor del parentesis es "self"
    def arrancar(self):
        self.enmarcha = True
    
    def estado(self):
        if (self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

## para acceder a una propiedad de una cles es necesario 
# el nombre del objeto.nombre del atributo
miCoche = coche() ## Instanciar una clase
print("El largo de mi coches es: ",miCoche.largoChasis)
print("El coche tiene: ",miCoche.ruedas," ruedas")
miCoche.arrancar()

print(miCoche.estado(),"\n")

print("Creacion del segundo objeto o Instancia \n")
miCoche2 = coche()
print("El largo de mi coches es: ",miCoche2.largoChasis)
print("El coche tiene: ",miCoche2.ruedas," ruedas")
print(miCoche2.estado())

