print("Evaluacion de Notas de Alumnos")

nota_alumno = int(input("Ingresa un valor Entero:"))

def evaluacion(nota):
    valoracion = "Aprovado"
    if nota < 5:
        valoracion = "Suspenso"
    return valoracion

print(evaluacion(nota_alumno))












