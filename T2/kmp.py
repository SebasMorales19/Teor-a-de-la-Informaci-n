#Sebastián morales Leyva 1797510
class Solution : 
    
    def strStr():
        
        haystack = input("\nIntroduzca el texto sin espacios por favor:    \n")
        needle =  input("Introduzca el patron sin espacios en blanco por favor:    ")
        #Es solo un filtro por si el patron está vacio
        print ("Longitud del Texto:  ",len (haystack))
        print("Longitud del patron:  ", len(needle))
        
        if needle == "" :  return 0
        #creamos el array LPS que es el que va contando el index de cuando hay una 
        lps = [0] * len(needle)#LPS siempre igual de grande que needle
        #Utilizamos 2 apuntadores prevLPS el tamaño del anterior lps ,i =  el valor actual
        prevLPS= 0
        i   = 1
        #Hacemos un while
        while i < len(needle):
            #si hacen match
            if prevLPS ==  0  :
                    lps[i] = 0 
                    i += 1
            
            elif needle[i] ==  needle[prevLPS]:
                lps[i] = prevLPS + 1#[ 0 , 1, aqui es el nuevo lps porque se itera]
                prevLPS += 1#para la siguiente iteración
                    
            else :
                    prevLPS = lps[prevLPS - 1]
        #para el kmp
        #ocupamos 2 contadores 
        i =  0 #ptr for haystack
        j = 0 # ptr for needle
        
        
        
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i,j = i+ 1 , j+1
            #como ya se comparo, sabemos que todo lo que se comparo antes de no
            #hacer matche está bien, solo tenemos que ver el index de lps del ultimo
            #index match = j-1
            else: 
                if j == 0:
                   i += 1 
                else : 
                    j =  lps[j-1]
            if j == len(needle):#Aqui es donde hieron match
                
                print ("\nHicieron match en el indice: " , i - len(needle))
                return i - len(needle)
        else:
            print("NO HUBO MATCH")
        return -1  #Si no encuentra un match
          
            
    

dale = Solution.strStr()  
dale

                
        
            
