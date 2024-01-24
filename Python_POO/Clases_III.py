class coche():
    ## Encapsulamieto de atributos
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False


    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos
        
        if(self.__enmarcha):
            chequeo = self.__chequeo_interno()
        
        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        
        elif(self.__enmarcha and chequeo== False):
            return "Hubo errores durante el chequeo"
        
        else:
            return "El coche esta parado"    
        
        
    
    def estado(self):
        print("El coche tiene: ", self.__ruedas,"ruedas.Um ancho: ",self.__anchoChasis,"y un largo de:",
            self.__largoChasis,"\n")

    ## Encapsulamiento de metodos
    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        
        self.gasolina= "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"
        
        if(self.gasolina=="ok" and self.aceite == "ok" and self.puertas=="cerradas" ):
            return True
        else:
            return False

miCoche = coche() 
print(miCoche.arrancar(True))

miCoche.estado()

print("Creacion del segundo objeto o Instancia \n")

miCoche2 = coche()

print(miCoche2.arrancar(False))


miCoche2.estado()