## Ejemplo Para un Break

print("while con la setencia break \n")

contador = 0



while contador < 10:
    contador += 1

    if contador == 5:
        break
    print("Valor actual de la variable: " , contador)

## Ejemplo para continue

print("while con la setencia continue \n")

contador = 0

while contador < 10:
    contador += 1

    if contador == 5: ## Se omite este valor 
        continue
    print("Valor actual de la variable: " , contador)
