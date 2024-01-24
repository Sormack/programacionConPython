##upper() pone todo en mayúsculas
##lower() pone todo en minúscula
##capitalize() todas la primera letra en mayúscula
##count() contar una y cuantas aparecen dentro de una cadena
##find() representa el índice donde aparece un carácter dentro de un texto
##isdigit() devuelve un booleano si es un valor numérico o no
##isalum() comprueba si es alfanuméricos
##isalpha si es alpha comprueba si son solo letras
##split()  separa por palabras utilizando espacios
##strip() borra los espacios sobrante al principio y al final
##replace() cambia una palabra o una letra por otra
##rfind() representa el índice de un carácter contando desde atrás

nombreUsuario = input("Introduce un nombre de usuario: ")
print("El nombre es:",nombreUsuario.upper())

print("El nombre es:",nombreUsuario.capitalize())

print("El nombre es:",nombreUsuario.lower())

edad = input("Introduce la edad: ")
print(edad.isdigit())



