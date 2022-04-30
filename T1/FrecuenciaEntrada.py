#Frecuencia de entrada

Fentradas = [] # Array de frecuencias de entrada
NoFentrada = int(input("Ingresa la cantidad de frecuencias de entrada: "))

for i in range(NoFentrada):
    Fentrada = input(f"Ingresa probabilidad de entrada {i + 1}: ") #Pedimos la probabiidad i
    Fentrada = float(Fentrada) # Convertir a float, pues input regresa una cadena
    Fentradas.append(Fentrada)   # Lo agregamos al arreglo con append

# Creacion de la matriz
filas = int(input("Ingresa la cantidad de filas de la matriz: "))
columnas = int(input("Ingresa la cantidad de columnas de la matriz: "))
matriz = [filas, columnas] 
matriz2 = [filas, columnas] 
k=-1
for i in range(filas):
    k=k+1
    for j in range(columnas):
        pEntrada = input(f"Ingresa probabilidad de entrada en la posición {i + 1} , {j + 1}: ") #Pedimos la probabilidad de entrada
        pEntrada = float(pEntrada) # Convertir a float, pues input regresa una cadena
        matriz.append(pEntrada)   # Lo agregamos a la matriz con append
        mult = pEntrada * Fentradas[k]
        matriz2.append(mult)    


print(matriz)
print(matriz2)

