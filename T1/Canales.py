class Canales():
    def Lineal():
        tamañoA=int(input("Indica la cantidad de valores que tiene tu canal A: \t\t"))
        tamañoB=int(input("Indica la cantidad de valores que tiene tu canal B: \t\t"))
        longitud= int (input("Indica la longitud de la tabla que se creará: \t\t"))
        longitud= longitud + 1 
        canalA= [1]*tamañoA
        canalB= [1]*tamañoB
        arrayelementosA= [1]*longitud
        arrayelementosB=[1]*longitud
                
        for i in range (0,tamañoA,1):
                canalA[i] =  int(input("Introduce los valores de tu canal A:\t\t"))
                
                
        for j in range (0,tamañoB,1):
                
                canalB[j] =  int(input("Introduce los valores de tu canal B:\t\t"))
                
        for k in range (1,longitud,1):
                num_elementos =  pow(tamañoA,k)
                arrayelementosA[k]= num_elementos
                num_elementos2  =  pow (tamañoB,k)
                arrayelementosB[k] = num_elementos2
            
         #####LO OCUPARE PARA IMPRIMIR
        print(f"Canal A : ","\t\t\t","Canal B: \t\t")           
        for i in range (0,tamañoA,1):
            print(canalA[i],"\t\t\t", canalB[i])
            
            
        print("Array de elementos: \n\n")
        for i in range (1,longitud,1):  
                print(i,"\t\t" ,arrayelementosA[i], "\t\t", arrayelementosB[i])

        print("Longitud de salida : longitud de entrada-> " , tamañoB ,"^L : ", tamañoA,"^L\n")
        print("Canal Lineal")
Canales.Lineal()         