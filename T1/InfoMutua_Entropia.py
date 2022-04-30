import math
import sys
import random


 ######             Menu 1                          ###########################################  
class Menu1:
     def __init__(self):
          
        self.operador = input('\n\nBienvenido! Selecciona la opcion  que quieres utilizar: \n\n   1.-Ingresar datos de Manera manual\n\n   2.-Leer un archivo txt  \n\n   3.-Generar datos aleatoriamente\t\t')

    
        if self.operador =="1":
                Manual()

    
        elif self.operador=="2":
                Archivo()


    
        elif self.operador  =="3":
                Random()
        

################################################# Menu 2 #################################################
class Manual: 
    def __init__(self):    
        self.opciones = input('\n\nSeleccionaste "INGRESAR LOS DATOS MANUALMENTE" , ahora selecciona las unidades que quieres utilizar: \n\n   1.-Cuantificables  (hartleys/simbolo)\n\n   2.-Transmision de datos binaria (bits/simbolo)  \n\n   3.-Transmision entre estados (nats/simbolo)\t\t')
        if self.opciones =="1":
            Cuantificables()
        
        elif self.opciones =="2":
            Transmision_binaria()
    
        elif self.opciones  =="3":
            Transmision_estado()
            
            
class Cuantificables:
    def __init__(self):
        self.cantidad1 = input(f"\nCuantos datos deseas ingresar:  \t")
        
        cantidad = int(self.cantidad1)
        
        datos= [1]*(cantidad)
        infomutua = [1]*(cantidad)
        entropia = [1]*(cantidad)
        suma_info_mutua = 0
        suma_entropia = 0
        print('\n')
        for i in range (0,cantidad,1):
            datos[i] =float(input(f"\Ingresa el dato por favor : "))
            infomutua[i] = math.log10(datos[i])*-1
            entropia[i] = (infomutua[i] * datos[i]) 
            suma_info_mutua = suma_info_mutua + infomutua[i]
            suma_entropia = suma_entropia + entropia[i]

            
        for i in range (0, cantidad, 1):
            
            print(f"\nEsta es la probabilidad del evento individual:  {datos[i]}")
            print(f"Esta es la informacion:  {infomutua[i]}")
            print (f"Esta es la entropia:  {entropia[i]}")
            print (f"\n")
        print(f"Tabla final: \n P(E)\t\tI(E)\t\tH(E)")    
        for i in range (0, cantidad, 1): print(f"{datos[i]}  {infomutua[i]}  {entropia[i]}")
        print(f"\n\nSuma de informacionn mutua : {suma_info_mutua} \t Suma de Entropia : {suma_entropia}\n\n")
        self.vector_proba = datos
        self.vector_IM = infomutua
        self.vector_entropia = entropia
        
        
        
class Transmision_binaria:
    def __init__(self):
        self.cantidad1 = input(f"Cuantos datos deseas ingresar:  \t\t")
        
        cantidad = int(self.cantidad1)
        
        datos= [1]*(cantidad)
        infomutua = [1]*(cantidad)
        entropia = [1]*(cantidad)
        suma_info_mutua = 0
        suma_entropia = 0
        print('\n')
        for i in range (0,cantidad,1):
            datos[i] =float(input(f"Ingresa el dato por favor : \t"))
            infomutua[i] = math.log2(datos[i])*-1
            entropia[i] = (infomutua[i] * datos[i])
            suma_info_mutua = suma_info_mutua + infomutua[i]
            suma_entropia = suma_entropia + entropia[i]
        print('\n')    
        for i in range (0, cantidad, 1):
            
            print(f"Esta es la probabilidad del evento individual:  {datos[i]}")
            print(f"Esta es la informacion:  {infomutua[i]}")
            print (f"Esta es la entropia:  {entropia[i]}")
            print (f"\n")
        print(f"Tabla final: \n P(E)\t\tI(E)\t\tH(E)")    
        for i in range (0, cantidad, 1): print(f"{datos[i]}  {infomutua[i]}  {entropia[i]}")
        print(f"\n\nSuma de informacionn mutua : {suma_info_mutua} \t Suma de Entropia : {suma_entropia}\n\n")
        self.vector_proba = datos
        self.vector_IM = infomutua
        self.vector_entropia = entropia
        
                
class Transmision_estado:
    def __init__(self):
        self.cantidad1 = input(f"Cuantos datos deseas ingresar:  \t\t")
        
        cantidad = int(self.cantidad1)
        
        datos= [1]*(cantidad)
        infomutua = [1]*(cantidad)
        entropia = [1]*(cantidad)
        suma_info_mutua = 0
        suma_entropia = 0
        print('\n')
        for i in range (0,cantidad,1):
            datos[i] =float(input(f"Ingresa el dato por favor :\t "))
            infomutua[i] = math.log(datos[i])*-1
            entropia[i] = (infomutua[i] * datos[i])
            suma_info_mutua = suma_info_mutua + infomutua[i]
            suma_entropia = suma_entropia + entropia[i]
        print('\n')
        for i in range (0, cantidad, 1):
            
            print(f"Esta es la probabilidad del evento individual:  {datos[i]}")
            print(f"Esta es la informacion:  {infomutua[i]}")
            print (f"Esta es la entropia:  {entropia[i]}")
            print (f"\n")
        print(f"Tabla final: \n P(E)\t\tI(E)\t\tH(E)")    
        for i in range (0, cantidad, 1): print(f"{datos[i]}  {infomutua[i]}  {entropia[i]}")
        print(f"\n\nSuma de informacionn mutua : {suma_info_mutua} \t Suma de Entropia : {suma_entropia}\n\n")
        self.vector_proba = datos
        self.vector_IM = infomutua
        self.vector_entropia = entropia
        
#######################             OPERADOR 2          #########################        
class Archivo():
     def __init__(self):    
        
        self.opciones = input('\n\nSeleccionaste "LEER UN ARCHIVO DE TEXTO" , ahora selecciona las unidades que quieres utilizar: \n\n   1.-Cuantificables  (hartleys/simbolo)\n\n   2.-Transmision de datos binaria (bits/simbolo)  \n\n   3.-Transmision entre estados (nats/simbolo)\t\t')
        print(f"Es importante tomar en cuenta que solo puedo haber un valor por cada fila del archivo ejemplo :\n0.5\n0.3\n0.8333\netc.")
       
        if self.opciones =="1":
            ArchivoCuantificable()
        
        elif self.opciones =="2":
            ArchivoBinario()
    
        elif self.opciones  =="3":
            ArchivoTransicionEstados()
            
            
class ArchivoCuantificable():   
    arreglo = [] 
    
    def __init__(self):
        
        cantidad = 0 
        
        suma_info_mutua = 0
        suma_entropia = 0
        
        filename = input('\n  Escribe la direccion de tu archivo de texto :   ')
        archivo= open(filename,"r")
        #Para poder llenar el arreglo LEER
        for row in archivo:
           self.arreglo.append(float(row))
        #Para imprimir   
        #for row in self.arreglo:
        #    cantidad = cantidad + 1
            
        cantidad = len(self.arreglo)
        infomutua = [1]* (cantidad)
        entropia = [1]*(cantidad)
        print (cantidad)
        
        for i in range(0,cantidad, 1):
                nuevo_valor = self.arreglo[i]
                infomutua [i] =   (math.log10(nuevo_valor)) * (-1)
                entropia[i] = (infomutua[i] * self.arreglo[i])
                suma_info_mutua = suma_info_mutua + infomutua[i]
                suma_entropia = suma_entropia + entropia[i]
                
            
            
        print(f"Tabla final: \n P(E)\t\tI(E)\t\tH(E)")    
        for i in range (0, cantidad, 1): print(f"{self.arreglo[i]}  {infomutua[i]}  {entropia[i]}")
        print(f"\n\nSuma de informacionn mutua : {suma_info_mutua} \t Suma de Entropia : {suma_entropia}\n\n")
        
        
        
class ArchivoBinario ():
    arreglo = [] 
    
    def __init__(self):
        
        cantidad = 0 
        
        suma_info_mutua = 0
        suma_entropia = 0
        
        filename = input('\n  Escribe la direccion de tu archivo de texto :   ')
        archivo= open(filename,"r")
        #Para poder llenar el arreglo LEER
        for row in archivo:
           self.arreglo.append(float(row))
        #Para imprimir   
        #for row in self.arreglo:
        #    cantidad = cantidad + 1
            
        cantidad = len(self.arreglo)
        infomutua = [1]* (cantidad)
        entropia = [1]*(cantidad)
        print (cantidad)
        
        for i in range(0,cantidad, 1):
                nuevo_valor = self.arreglo[i]
                infomutua [i] =   (math.log2(nuevo_valor)) * (-1)
                entropia[i] = (infomutua[i] * self.arreglo[i])
                suma_info_mutua = suma_info_mutua + infomutua[i]
                suma_entropia = suma_entropia + entropia[i]
                
               
            
            
        print(f"Tabla final: \n P(E)\t\tI(E)\t\tH(E)")    
        for i in range (0, cantidad, 1): print(f"{self.arreglo[i]}  {infomutua[i]}  {entropia[i]}")
        print(f"\n\nSuma de informacionn mutua : {suma_info_mutua} \t Suma de Entropia : {suma_entropia}\n\n")
        
        
class ArchivoTransicionEstados() :
    arreglo = [] 
    
    def __init__(self):
        
        cantidad = 0 
        
        suma_info_mutua = 0
        suma_entropia = 0
        
        filename = input('\n  Escribe la direccion de tu archivo de texto :   ')
        archivo= open(filename,"r")
        #Para poder llenar el arreglo LEER
        for row in archivo:
           self.arreglo.append(float(row))
        #Para imprimir   
        #for row in self.arreglo:
        #    cantidad = cantidad + 1
            
        cantidad = len(self.arreglo)
        infomutua = [1]* (cantidad)
        entropia = [1]*(cantidad)
        print (cantidad)
        
        for i in range(0,cantidad, 1):
                nuevo_valor = self.arreglo[i]
                infomutua [i] =   math.log(nuevo_valor) * -1
                entropia[i] = (infomutua[i] * nuevo_valor)
                suma_info_mutua = suma_info_mutua + infomutua[i]
                suma_entropia = suma_entropia + entropia[i]
                
               
            
            
        print(f"Tabla final: \n P(E)\t\tI(E)\t\tH(E)")    
        for i in range (0, cantidad, 1): print(f"{self.arreglo[i]}  {infomutua[i]}  {entropia[i]}")
        print(f"\n\nSuma de informacionn mutua : {suma_info_mutua} \t Suma de Entropia : {suma_entropia}\n\n")    


class Random(): 
    def __init__(self):
        #datos  =  input(f"Ingresa por favor la cantidad de datos que quieres generar aleatoriamente")
        
        self.opciones = input('\n\nSeleccionaste " GENERAR DATOS ALEATORIAMENTE" , ahora selecciona las unidades que quieres utilizar: \n\n   1.-Cuantificables  (hartleys/simbolo)\n\n   2.-Transmision de datos binaria (bits/simbolo)  \n\n   3.-Transmision entre estados (nats/simbolo)\t\t')
        if self.opciones =="1":
            Random_Cuantificables()
        
        elif self.opciones =="2":
            Random_Transmision_binaria()
    
        elif self.opciones  =="3":
            Random_Transmision_estado()     
            
            
class Random_Cuantificables():
    def __init__ (self):
        self.cantidad1 = int (input(f"\nCuantos datos deseas ingresar? :  \t"))
        
        
        datos= [1]*(self.cantidad1)
        infomutua = [1]*(self.cantidad1)
        entropia = [1]*(self.cantidad1)
        suma_info_mutua = 0
        suma_entropia = 0
        print('\n')
        for i in range (0,self.cantidad1,1):
            datos[i] = random.random()
            print (datos[i])            
            infomutua[i] = math.log10(datos[i])*-1
            entropia[i] = (infomutua[i] * datos[i]) 
            suma_info_mutua = suma_info_mutua + infomutua[i]
            suma_entropia = suma_entropia + entropia[i]

            
        for i in range (0, self.cantidad1, 1):
            
            print(f"\nEsta es la probabilidad del evento individual:  {datos[i]}")
            print(f"Esta es la informacion:  {infomutua[i]}")
            print (f"Esta es la entropia:  {entropia[i]}")
            print (f"\n")
        print(f"Tabla final: \n P(E)\t\tI(E)\t\tH(E)")    
        for i in range (0, self.cantidad1, 1): print(f"{datos[i]}  {infomutua[i]}  {entropia[i]}")
        print(f"\n\nSuma de informacionn mutua : {suma_info_mutua} \t Suma de Entropia : {suma_entropia}\n\n")
        self.vector_proba = datos
        self.vector_IM = infomutua
        self.vector_entropia = entropia
        
        
        

class Random_Transmision_binaria(): 
    def __init__ (self):
        self.cantidad1 = int (input(f"\nCuantos datos deseas ingresar? :  \t"))
        
        
        datos= [1]*(self.cantidad1)
        infomutua = [1]*(self.cantidad1)
        entropia = [1]*(self.cantidad1)
        suma_info_mutua = 0
        suma_entropia = 0
        print('\n')
        for i in range (0,self.cantidad1,1):
            datos[i] = random.random()
            print (datos[i])            
            infomutua[i] = math.log2(datos[i])*-1
            entropia[i] = (infomutua[i] * datos[i]) 
            suma_info_mutua = suma_info_mutua + infomutua[i]
            suma_entropia = suma_entropia + entropia[i]

            
        for i in range (0, self.cantidad1, 1):
            
            print(f"\nEsta es la probabilidad del evento individual:  {datos[i]}")
            print(f"Esta es la informacion:  {infomutua[i]}")
            print (f"Esta es la entropia:  {entropia[i]}")
            print (f"\n")
        print(f"Tabla final: \n P(E)\t\tI(E)\t\tH(E)")    
        for i in range (0, self.cantidad1, 1): print(f"{datos[i]}  {infomutua[i]}  {entropia[i]}")
        print(f"\n\nSuma de informacionn mutua : {suma_info_mutua} \t Suma de Entropia : {suma_entropia}\n\n")
        self.vector_proba = datos
        self.vector_IM = infomutua
        self.vector_entropia = entropia
        
        
class Random_Transmision_estado():
    def __init__ (self):
        self.cantidad1 = int (input(f"\nCuantos datos deseas ingresar? :  \t"))
        
        
        datos= [1]*(self.cantidad1)
        infomutua = [1]*(self.cantidad1)
        entropia = [1]*(self.cantidad1)
        suma_info_mutua = 0
        suma_entropia = 0
        print('\n')
        for i in range (0,self.cantidad1,1):
            datos[i] = random.random()
            print (datos[i])            
            infomutua[i] = math.log(datos[i])*-1
            entropia[i] = (infomutua[i] * datos[i]) 
            suma_info_mutua = suma_info_mutua + infomutua[i]
            suma_entropia = suma_entropia + entropia[i]

            
        for i in range (0, self.cantidad1, 1):
            
            print(f"\nEsta es la probabilidad del evento individual:  {datos[i]}")
            print(f"Esta es la informacion:  {infomutua[i]}")
            print (f"Esta es la entropia:  {entropia[i]}")
            print (f"\n")
        print(f"Tabla final: \n P(E)\t\tI(E)\t\tH(E)")    
        for i in range (0, self.cantidad1, 1): print(f"{datos[i]}  {infomutua[i]}  {entropia[i]}")
        print(f"\n\nSuma de informacionn mutua : {suma_info_mutua} \t Suma de Entropia : {suma_entropia}\n\n")
        self.vector_proba = datos
        self.vector_IM = infomutua
        self.vector_entropia = entropia
        
        
#####################           AQUI INDICAREMOS QUE VA A CORRER EL MENU 1          ###############################


correr =  Menu1()
correr
    

    
 