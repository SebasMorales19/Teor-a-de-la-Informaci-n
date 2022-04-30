import math
class Canales():
    def Modular():
        
        tamañoA=int(input("Indica la cantidad de valores que tiene tu canal A: \t\t"))
        tamañoA = tamañoA + 1
        tamañoB=int(input("Indica la cantidad de valores que tiene tu canal B: \t\t"))
        tamañoB = tamañoB + 1
        
        longitud= int (input("Indica la longitud de la tabla que se creará: \t\t"))
        longitud= longitud + 1 
        canalA= [1]*tamañoA 
        canalB= [1]*tamañoB
        arrayDigitosA = [1]*tamañoA
        arrayDigitosB = [1]*tamañoB
        arrayelementosA= [1]*longitud
        arrayelementosB=[1]*longitud
                
        for i in range (1,tamañoA,1):
                print(tamañoB,tamañoA)
                canalA[i] =  input("Introduce los valores de tu canal A:\t\t")
                numeroA = 0
                
                for c in canalA[i]:
                        if c.isdigit():
                                numeroA += 1
                        else:
                                pass
                arrayDigitosA[i] = numeroA                
                canalA[i] =  int(canalA[i])
                print ("Digitos de Canal A en la posicion:  ",i, " ",numeroA, "\n\n")

                
                
        for j in range (1,tamañoB,1):
                
                canalB[j] =  input("Introduce los valores de tu canal B:\t\t")
                numeroB = 0
                
                for c in canalB[j]:
                        if c.isdigit():
                                numeroB += 1
                        else:
                                pass        
                canalB[j] =  int(canalB[j])
                arrayDigitosB[j] = numeroB 
                print ("Digitos de Canal A en la posicion:  ",j, " ",numeroB, "\n\n")
                  
        for k in range (1,longitud,1):# K es la equivalente a L 
                        ## Array A
                    # 3^4*piso(L/4): 2^piso(L/4)    
                
                if ((k % arrayDigitosA[1])  == 0):
                                        #       2     ^  1 *piso (L/4)
                        num_elementos2  =  pow ((tamañoA-1),(arrayDigitosB[1]*(math.floor(k/arrayDigitosA[1]))))
                        arrayelementosA[k] = num_elementos2
                        
                else:
                        arrayelementosA[k] = arrayelementosA[(k-1)]
                 ##Array B 
                if ((k % arrayDigitosB[1])  == 0):
                                                 #       3     ^  4 *piso (L/4)
                        num_elementos2  =  pow ((tamañoB-1),(arrayDigitosA[1]*(math.floor(k/arrayDigitosA[1]))))
                        arrayelementosB[k] = num_elementos2
                        
                else:
                        arrayelementosB[k] = arrayelementosB[(k-1)]
                        
                        
                        
                
         #####LO OCUPARE PARA IMPRIMIR
        print(f"Canal A : ","\t\t\t","Canal B: \t\t")           
        for i in range (1,(tamañoB-1),1):
            print(canalA[i],"\t\t\t", canalB[i] , tamañoA, tamañoB)
            
            
        print("Array de elementos: \n\n")
        print("L\t\t nA^\t\t nB^")
        for i in range (1,longitud,1):  
                print(i,"\t\t" ,arrayelementosA[i], "\t\t", arrayelementosB[i])
                                        #3^4*piso(L/4): 2^piso(L/4) (tamañoB-1),(arrayDigitosA[1]*(math.floor(k/arrayDigitosA[1])#####(tamañoA-1),(arrayDigitosB[1]*(math.floor(k/arrayDigitosA[1])
        print("Longitud de salida : longitud de entrada-> " , (tamañoB-1) ,"^", arrayDigitosA[1], "* piso(L/", arrayDigitosA[1], ") :" , (tamañoA-1) ,"^", arrayDigitosB[1], "* piso(L/", arrayDigitosA[1], ")")
        print("Canal Modular")
        
       
Canales.Modular()