def evaluaEdad(edad):
    if edad < 0:
        raise TypeError("No se permiten edades negativas")
    if edad< 20:
        return "eres mut joven"
    elif edad < 40:
        return "Ere Joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return(" Cuidate")

    

