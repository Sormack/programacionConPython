
email = input("Introduce tu direccion de email: ")

contador = 0

contador_2 = 0

for i in range(len(email)):
    if email[i] == "@":
        contador += 1

    if email[i] == ".":
        contador_2 += 1

if contador == 1 and contador_2 >= 1:
    print("La direccion de email es correcta")
else:
    print("La direccion de email es incorrecta")

