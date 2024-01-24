
con = input("Introduce una contraseña: ")

contador = 0
for i in range(len(con)):
    if con[i] == " ":
        contador = 1  

if len(con) < 8 or contador > 8:
    print("La contraseña es incorrecta")
else:
    print("La contraseña es correcta")

