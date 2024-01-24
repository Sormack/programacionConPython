## Paython genera una lista de elementos

for i in range(5):
    print(i, end =" ",) 

print("\n")

for i in range(5):
    ## Al usar el valor f" texto { i }" se pueden unir los textos con variables
    print(f"Valor de la variable {i}")

## Permite iniciar con una variables y terminar con otra variable
print("\n")

for i in range(5,10):
    print(f"Valor de la variable {i}","\n")

## Tambien permite de cuanto a cuento aumentara el conteo

for i in range(5,50,3):
    print(f"Valor de la variable {i}")

valido = False 

email = input("Introduce tu direccon de email: ")

for i in range(len(email)):
    if email[i] == "@":
        valido = True

if valido:
    print("Email correcto")
else:
    print("Email incorrecto")









