class persona():
    def __init__(self, nombre,edad,residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia
    
    def descripcion(self):
        print("nombre: ",self.nombre,"edad: ",self.edad,"Residencia: ",self.residencia)

## EL metodo super ejecuta el metodo init de la clase padre
## y se agragaran parametros extra para almacenar los valores

class empleado(persona):
    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)
        self.salario =salario
        self.antiguedad = antiguedad
## Se sobreescribe el meto descripcion
    def descripcion(self):
        super().descripcion()
        print("Salario: ",self.salario,"Antiguedad: ",self.antiguedad)

## Lo valores para los parametros haora son cinco
Javi = empleado(2000,15,"Javi",21,"Mexico")

Javi.descripcion()
## Para saber si una intancia pertenece a una clase 
print(isinstance(Javi,persona))