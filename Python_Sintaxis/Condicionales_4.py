print("Programa de Optencion de becas")

distancia_e = int(input("Introduce la distancia a la escuela en Km: "))
num_h = int(input("Introduce el numero de hermanos: "))
salario_f = int(input("Introduce el salario familiar anual bruto: "))

if distancia_e > 40 and num_h > 2 and salario_f <= 20000:
    print("Tiene derecho a beca")
else:
    print("No tiene derecho a veca")


































