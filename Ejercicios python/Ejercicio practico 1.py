print("Dias de Vacaciones Correspondientes a los trabajadores de Rappi.\n")

print("Clave 1 'Atencion a Clientes'")
print("Clave 2 'Logistica'")
print("Clave 3 'Gerencia'")

nom = input("Cual es el nombre del trabajador: ")

clave = int(input("Cual es la clavel del trabajador: " ))

tiempo = int(input("Cuanto tiempo ha trabajado: " ))

## Clave 1

if clave == 1 and tiempo == 1 :
    print("El tiempo de vacaciones de", nom,"Es de 6 dias")

elif clave == 1 and tiempo == 2:
    print("El tiempo de vaciones de" , nom , "Es de 14 dias")
    
elif clave == 1 and tiempo <= 6:
    print("El tiempo de vaciones de" , nom , "Es de 14 dias")
    
elif clave == 1 and tiempo >= 7 :
    print("El tiempo de vaciones de" , nom , "Es de 20 dias")



## Clave 2

if clave == 2 and tiempo == 1 :
    print("El tiempo de vacaciones de", nom,"Es de 7 dias")

elif clave == 2 and tiempo == 2:
    print("El tiempo de vaciones de" , nom , "Es de 15 dias")
    
elif clave == 2 and tiempo <= 6:
    print("El tiempo de vaciones de" , nom , "Es de 15 dias")
    
elif clave == 2 and tiempo >= 7 :
    print("El tiempo de vaciones de" , nom , "Es de 22 dias")


## Clave 3

if clave == 3 and tiempo == 1 :
    print("El tiempo de vacaciones de", nom,"Es de 10 dias")

elif clave == 3 and tiempo == 2:
    print("El tiempo de vaciones de" , nom , "Es de 20 dias")
    
elif clave == 3 and tiempo <= 6:
    print("El tiempo de vaciones de" , nom , "Es de 20 dias")
    
elif clave == 3 and tiempo >= 7 :
    print("El tiempo de vaciones de" , nom , "Es de 30 dias")














    
    
    
