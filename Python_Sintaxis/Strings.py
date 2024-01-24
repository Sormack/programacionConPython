print("String Asignacion")
mensaje = "Hola"
mensaje += " "   ##los signos += sirve para guardar la varable anterio
                   ## y sumarla con la nueva variable
mensaje += "Javier "
print(mensaje)


print("Concatenacion:")
mensaje = "Hola"
espacio = " "
nombre = "Javier"
print(mensaje + espacio + nombre)

print("---------")
num_1 = 4
num_2 = 6
resultados = num_1 + num_2
resultados = str(resultados)##convertir un cadena de enteros a string  
print("El resultado de la suma:" + resultados)

print("La busqueda")
mensaje = "Hola Mundo"
buscar_subcadena = mensaje.find( "Mundo" )
print(buscar_subcadena)

print("Extraer")
mensaje = "Hola Mundo"
extraer_subcadena = mensaje[1:8]
print(extraer_subcadena)

print("Comporacion")
mensaje_uno = "Hola"
mensaje_dos = "Hola"
print(mensaje_uno == mensaje_dos)

