class Algoritmica():
    def tablaOriginal():
            
        cantidadDatos = int(input("Ingresa la cantidad de frecuencias de entrada que ingresaras:\t"))

        intensidad=[1]*cantidadDatos
        longitud=[1]*cantidadDatos
        alfa=[1]*cantidadDatos
        beta=[1]*cantidadDatos



        for i in range(0,cantidadDatos,1):
            x= float (input("Ingresa la intensidad de frecuencias: \t"))
            intensidad[i] =  x
            longitud[i] =  intensidad[i]
            
        alfa[0] = 0

        for j in range(0,cantidadDatos,1) :
        
            if j != 0:     
                alfa[j] = beta[(j-1)]    
            beta[j] = alfa[j] + longitud[j]
            #print(alfa[j], j)
            #alfa[j+1] = float( beta[j])
            
            

        print("Estas son als intensidades de frecuenta \n")
        print(intensidad, "\n")
        print("Estas son las longitudes:\n")
        print(longitud, "\n")
        print("Fila de ALFA: \n")
        print(alfa, "\n")
        print("Fila de BETA: \n")
        print(beta, "\n")
        
    
        z =  int(input("Deseas realizar una segunda codificación con otra letra de la palabra? (1 para sí , 0 para  no ): \n "))    
        while z == True:
            indiceN=int(input("Indica el indice de la letra de la cual quieres hacer una nueva codificación contando como la primera letra 0 "))
        #Las intensidades siguen igual
        #como es la segunda tabla el indice que escogio se va a multiplicar por el valor de la intencidad del indice 
        #abcdef -> con el indice c = ca cb cc ce cf
            longitudN = [1]* cantidadDatos
            alfaN=[1]*cantidadDatos
            betaN=[1]*cantidadDatos   
            for i in range(0,cantidadDatos,1):
            
                longitudN[i] =  intensidad[indiceN] * intensidad[i]
            
            alfaN[0] = 0

            for j in range(0,cantidadDatos,1) :
            
                if j != 0:     
                    alfaN[j] = betaN[(j-1)]    
                betaN[j] = alfaN[j] + longitudN[j]
                #print(alfa[j], j)
                #alfa[j+1] = float( beta[j])
                
                

            print("Estas son als intensidades de frecuenta \n")
            print(intensidad, "\n")
            print("Estas son las nuevas longitudes:\n")
            print(longitudN, "\n")
            print("Fila de ALFA: \n")
            print(alfaN, "\n")
            print("Fila de BETA: \n")
            print(betaN, "\n")
            z =  int(input("Deseas realizar una otra codificación con otra letra de la palabra? (1 para sí , 0 para  no ): \n "))

    tablaOriginal()