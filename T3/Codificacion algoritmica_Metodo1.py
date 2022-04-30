from typing import List


class Algoritmica():
    def metodo1():
        alfa= float(input("Ingresa tu variable alfa:    "))
        beta= float(input("Ingresa tu variable beta:    "))
        longitud = float(input("Ingresa tu variable de longitud:    "))
        #print(alfa,beta,longitud)
        x = 0
        tcontador = 1
#primera desigualdad
        while x != 1:
            tdecimal = (1/(2**tcontador))
            if tdecimal<=longitud:
                x = 1   
            else:
                   tcontador = tcontador + 1
                   
        #print("Valores!\t",x,"\t", tdecimal,"\t",tcontador)    
        #segunda desigualdad
        t2desigualdad= 2**-tcontador
        t2_1desigualdad = 2**-tcontador
        if t2desigualdad<= t2_1desigualdad:
            p5a = round((2**tcontador*alfa))
            p5b = round((2**tcontador*beta))
            #print("p5a y b " , p5a,p5b)
            if p5a % 2 == 0 :
                r = p5a / 2**tcontador
                print("A esto le haremos la codificacion:\t",r)
                fraccion = (r).as_integer_ratio()
                print("El segundo número es el denominador para ingresarlo a continuacion:\t",fraccion)
                x = int(input("Indica por favor el denominador de la fracción para empezar con la codifiación de Shannon:\t"))
                z = r * 2
                cantidad = x 
                lista1  = [1]*(cantidad)
                lista2  = [1] * (cantidad)
                lista1[0] = z
                j= 0
                for i  in range(0 , x,1):
                    if lista1[i] < 1:

                        lista1[(i+1)] = float (lista1[i]*2)
                        lista2[i] = 0

                    else:
                        if lista1[i]> 1:
                        
                            lista2[i]= 1
                            j=i 
                        
                print("Esta es la lista de los subindices:\n")
                for s in range (0,j+1):
                    print (lista1[s],  end = " ")
                print("\nEsta es la codificacion binaria: \n")
                for k in range (0,j+1):
                    print (lista2[k],  end = " ")
                    
            elif p5b % 2 == 0 :
                r = p5b / 2**tcontador
                print("A esto le haremos la codificacion:\t",r)
                fraccion = (r).as_integer_ratio()
                print("El segundo número es el denominador para ingresarlo a continuacion:\t",fraccion)
                x = int(input("Indica por favor el denominador de la fracción para empezar con la codifiación de Shannon:\t"))
                z = r * 2
                cantidad = x 
                lista1  = [1]*(cantidad)
                lista2  = [1] * (cantidad)
                listaAm2= [1] * (cantidad)
                listaA1m2= [1] * (cantidad)
                listaBm2= [1] * (cantidad)
                listaB1m2= [1] * (cantidad)
                lista1[0] = z
                listaAm2[0] = alfa*2
                listaBm2[0] = beta*2
                j= 0
                for i  in range(0 , x,1):
                    if lista1[i] < 1:

                        lista1[(i+1)] = float (lista1[i]*2)
                        lista2[i] = 0

                    else:
                        if lista1[i]> 1:
                        
                            lista2[i]= 1
                            j=i 
#           LISTA PARA ALFA                            
                    if listaAm2[i] < 1 :
                        listaAm2[(i+1)] = float (listaAm2[i]*2)
                        listaA1m2[i] = 0   
                    else:
                        if listaAm2[i]> 1:
                            listaAm2[(i+1)] = float ((listaAm2[i] - 1 )*2)
                            listaA1m2[i]= 1
                            
                                  
#           LISTA PARA BETA 
                    if listaBm2[i] < 1 :
                        listaBm2[(i+1)] = float (listaBm2[i]*2)
                        listaB1m2[i] = 0   
                    else:
                        if listaBm2[i]> 1:
                            listaBm2[(i+1)] = float ((listaBm2[i]-1 )*2)
                            listaB1m2[i]= 1
                            
                    if listaA1m2[i] != listaB1m2[i]:
                        j=i        



#           CODIFICCACION BINARIA METODO 2
                   
                print("Esta es la lista de los subindices:\n")
                for s in range (0,j+1):
                    print (lista1[s],  end = " ")
                print("\nEsta es la codificacion binaria: \n")
                for k in range (0,j+1):
                    print (lista2[k],  end = " ")
                    
#IMPRIMIR METODO 2                    
                print("\n\nMETODO 2\n\n")    
#IMPRIMIR ALFA                
                print("Esta es la lista de los subindices de la lista de ALFA:\n")
                for s in range (0,j+1):
                    print (listaAm2[s],  end = " ")
                print("\nEsta es la codificacion binaria de la lista de ALFA: \n")
                for k in range (0,j+1):
                    print (listaA1m2[k],  end = " ")
#IMPRIMIR BETA
                print("Esta es la lista de los subindices de la lista de BETA:\n")
                for s in range (0,j+1):
                    print (listaBm2[s],  end = " ")
                print("\nEsta es la codificacion binaria de la lista de BETA: \n")
                for k in range (0,j+1):
                    print (listaB1m2[k],  end = " ")
#               print("\nAlfa\n",listaA1m2, "\nBeta\n", listaB1m2) 
        

            


Algoritmica.metodo1()