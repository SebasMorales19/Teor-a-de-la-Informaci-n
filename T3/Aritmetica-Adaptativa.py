#from itertools import combinations
from itertools import combinations_with_replacement, permutations
from itertools import compress, product

secu = input("Introdusca la secuencia: ")
secu = list(secu) #La secuencia se transformo en lista
lonlis = len(secu) #Longitud de la lista

def permutaciones_repeticion(cadena, tamagnio):
    caracteres= list(cadena)
    permutaciones = []

    for c in product(caracteres, repeat=tamagnio):
        permutaciones.append(c)

    return permutaciones


"""for  i in range(lonlis):
    k=i+1
    cont = -1
    bsum=0
    asum=0
    for j in range(k):
        cont = cont + 1
        l=1/k
        asum = asum
        bsum = l + bsum
        a=asum
        b=bsum
        lisdos= secu[0:k]
        lisdos.sort()
        print(lisdos[cont] + " " +"alfa= " + str(a) + " " + "beta= " + str(b) + " " + "long= " + str(l))
        sup = bsum
        asum= sup
        bsum= bsum """


for i in range(lonlis):
    k=i+1
    listre=secu[0:k]
    listre.sort()
    cont = 0
    for j in range(k):
        cont = cont + 1 
        print("Nivel= " + str(cont))
        print(permutaciones_repeticion(listre[0:k], cont))
        cant = permutaciones_repeticion(listre[0:k], cont)
        # print(cant[0:1])
        liscan=list(cant)
        #print(liscan)
        o = len(cant)
        contd = -1
        bsum=0
        asum=0
        for u in range(o):
            contd = contd + 1
            l=1/o
            asum = asum
            bsum = l + bsum
            a=asum
            b=bsum
            #liscua= secu[0:k]
            #liscua.sort()
            print(liscan[contd])
            print(" " +"alfa= " + str(a) + " " + "beta= " + str(b) + " " + "long= " + str(l))
            sup = bsum
            asum= sup
            bsum= bsum
