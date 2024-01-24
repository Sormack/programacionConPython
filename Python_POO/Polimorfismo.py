class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")


class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")


class Camion():
    def desplazamiento(self):
        print("Me desplazamiento utilizando seis ruedas")

## Esta funcion cambia segun a sus parametros
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo = Camion()
desplazamientoVehiculo(miVehiculo)

miVehiculo2 = Coche()
desplazamientoVehiculo(miVehiculo2)