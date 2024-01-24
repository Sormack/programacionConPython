class Vehicluos():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.arrancar = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca:",self.marca,"\nModelo:",self.modelo,
        "\nEn marcha: ",self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena)

class Furgoneta(Vehicluos):
    def carga(self,carga):
        self.cargado = carga
        if(self.cargado):
            return "La furgoneta esta cargado"
        else:
            return "La furgoneta no esta cargada"


## Toma los atributos y metodos junto con el constructor de 
## de la clase Vehiculos
class Moto(Vehicluos):
    elCaballo = ""
    def caballito(self):
        self.elCaballo = "Esto haciendo el caballito"
    ## De esta manera se sobreescribe el motodo estado de la clases padre
    def estado(self):
        print("Marca:",self.marca,"\nModelo:",self.modelo,
        "\nEn marcha: ",self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena,
        "\n",self.elCaballo)

class VEelectricos(Vehicluos):
    def __init__(self, marca, modelo):
        super().__init__(marca,modelo)
        self.autonomia = 100
    def cargarEnergia(self):
        self.cargar = True
    
miMoto = Moto ("Honda","CBR")

miMoto.caballito()

miMoto.estado()

miFurgoneta = Furgoneta("Renaut","Kango")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))

## Se herada segun el oreden puesto la herencia multiple

class BicicletaElectrica(VEelectricos,Vehicluos):
    pass

miBici = BicicletaElectrica("Orbas","NSD")











