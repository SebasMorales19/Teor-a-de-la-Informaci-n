#Metodo Shannon Fannon Elias

import math

#Variables
inicial = []
acumulada = []
binaria = []
numero = []
longitud = 0
tamanio = input("Numero de frecuencias: ")
tamanio = int(tamanio)

#Pedir las frecuencias
for i in range(0, tamanio):
    elemento = input("Frecuencia: ")
    elemento = float(elemento)
    inicial.insert(i, elemento)

#Ordenar de mayor a menor
inicial.sort(reverse=True)

#Frecuencias acumuladas
suma = 0
total = 0
a = 1
for i in range(0, tamanio):
    suma = (inicial[i]/2) + total
    suma = round(suma, 4)
    acumulada.insert(i, suma)
    total = total + inicial[i]

print("Frecuencia inicial: ", inicial)
print("Frecuencia acumulada: ", acumulada)
print("")

#Expresion binaria
for i in range(0, tamanio):
    a = 0
    condicion = 0
    print("Frecuencia ", acumulada[i])
    dato = acumulada[i]
    while condicion == 0:
        if dato < 1:
            dato = dato * 2
            dato = round(dato, 4)
        else:
            dato = (dato-1)*2
            dato = round(dato, 4)
        binaria.insert(a, dato)
        for j in range(0, a):
            if dato == binaria[j]:
                condicion = 1
        if binaria[a] < 1:
            numero.insert(a, 0)
        else:
            numero.insert(a, 1)
        a = a+1

    #LK
    lk = (math.log2(1 / inicial[i]))+1
    lk = math.floor(lk)

    #Longitud media de salida
    suma = lk*inicial[i]
    longitud =suma + longitud


    print("Expresion binaria: ", binaria)
    print("Digito binario: ", numero)
    print("Li: ", lk)
    print("Digitos Li: ", numero[0:lk])
    print("")
    binaria.clear()
    numero.clear()

#Radio de comprension
radio = 8/longitud
radio = round(radio, 4)

print("Longitud media de salida: ", longitud)
print("Radio de comprension: ", radio)