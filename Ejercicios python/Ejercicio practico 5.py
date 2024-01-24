print("Serie Fibonacci")

## Para crea dos variables en una sola linea

num_1 , num_2 = 0 , 1 

while num_2 <= 1597:
    print(num_1 , num_2 , end = " ")
    num_1 = num_1 + num_2
    num_2 = num_1 + num_2

print("Fin")
