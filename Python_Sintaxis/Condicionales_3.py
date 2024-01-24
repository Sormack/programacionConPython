edad = 7

if 0 < edad < 100:
    print("La edad es correcta")
else:
    print("Edad incorecta")


salario_P = int(input("Introduce salario presidente: "))
print("Salarios presidente: ", salario_P)

## Para encadenar un string con un entero
##print("Salarios presidente: " + str(salario_P))

salario_D = int(input("Introduce salario director: "))
print("Salarios presidente: ", salario_D)

salario_JA = int(input("Introduce salario Jede de Area: "))
print("Salarios presidente: ", salario_JA)

salario_A = int(input("Introduce salario Administrativo: "))
print("Salarios presidente: ", salario_A)

if salario_A < salario_JA < salario_D < salario_P:
    print("Todo funciona corectamente")
else:
    print("Algo falla en esta empresa")




