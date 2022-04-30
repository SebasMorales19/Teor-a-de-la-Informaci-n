import csv

# --- Clase Metodo KMP ---
class KMP:
	# Metodo constructor
	def __init__(self, texto, patron):
		# Guardar el texto y patron recibidos
		self.textoKMP = texto.lower()
		self.patronKMP = patron.lower()

		# Obtener los valores de la tabla
		self.tablaKMP = self.crearTabla()


	# Metodo para obtener los valores de la tabla
	def crearTabla(self):
		# Crea una tabla local con el numero de caracters ASCII
		tabla = [0]*len(self.patronKMP)

		# El primer valor de la tabla siempre es -1
		tabla[0] = -1

		# Regresar la tabla creada
		return tabla


	# Metodo que realiza la busqueda usando la posicion indicada
	def busqueda(self, indice):
		self.movimientos = 0
		self.comparaciones = ""

		# Realiza la busqueda del patron usando KMP
		for i in range(len(self.patronKMP)):
			# Si los caracteres del patron y del texto son el mismo
			if self.patronKMP[i] == self.textoKMP[indice+i]:
				self.movimientos = self.movimientos+1
				#print(f"{self.patronKMP[i]} es igual a: {self.textoKMP[indice+i]}")	# Impresion para verificar su correcta comparacion
				self.comparaciones += f"\n{self.patronKMP[i]} es igual a: {self.textoKMP[indice+i]}"
			else:
				#print(f"{self.patronKMP[i]} NO es igual a: {self.textoKMP[indice+i]}") # Impresion para verificar su correcta comparacion
				self.comparaciones += f"\n{self.patronKMP[i]} NO es igual a: {self.textoKMP[indice+i]}"
				# Terminar la busqueda
				return False

		# Regresar que la busqueda se completo sin interrupciones
		return True


	# Metodo que regresa el numero de saltos que se van a realizar
	def obtenerCambio(self):
		# Busca el valor de cambios usando la posicion del caracter en la tabla
		# Para obtener el cambio se usa el numero de comparaciones realizadas en la
		# iteracion menos el valor de la tabla de dicho numero de comparaciones
		return self.movimientos-self.tablaKMP[self.movimientos]


	def obtenerComparaciones(self):
		return self.comparaciones




# --- Clase Metodo BM ---
class BM:
	# Metodo constructor
	def __init__(self, texto, patron):
		# Guarda el texto y patron recibidos
		self.textoBM = texto.lower()
		self.patronBM = patron.lower()

		# Obtener los valores de la tabla
		self.tablaBM = self.crearTabla()


	# Metodo para obtener los valores de la tabla
	def crearTabla(self):
		# Crea una tabla local con el numero de caracters ASCII
		tabla = [len(self.patronBM)]*256

		# Variables locales
		listaPatronInvertido = list(self.patronBM[::-1])
		listaPatronInvertido.pop(0)		# Elimina el ultimo valor del patron (primero en esta lista)
		listaTemporal = list()	# Lista que contendra los caracteres con valores ya asignados

		# Asignar valores a los caracteres dentro del patron
		for i in range(len(listaPatronInvertido)):
			if listaPatronInvertido[i] not in listaTemporal:
				tabla[ord(listaPatronInvertido[i])] = i+1
				listaTemporal.append(listaPatronInvertido[i])

		# Regresar la tabla creada
		return tabla


	# Metodo que realiza la busqueda usando la posicion indicada
	def busqueda(self, indice):
		self.movimientos = 0
		self.caracter = ''
		self.comparaciones = ""

		# Realiza la busqueda del patron usando BM
		for i in range(len(self.patronBM)):
			# Si los caracteres del patron y del texto son el mismo
			if self.patronBM[len(self.patronBM)-1-i] == self.textoBM[len(self.patronBM)-1+indice-i]:
				self.movimientos = self.movimientos+1
				#print(f"{self.patronBM[len(self.patronBM)-1-i]} es igual a: {self.textoBM[len(self.patronBM)-1+indice-i]}") 	# Impresion de prueba
				self.comparaciones += f"\n{self.patronBM[len(self.patronBM)-1-i]} es igual a: {self.textoBM[len(self.patronBM)-1+indice-i]}"
			else:
				self.caracter = self.textoBM[len(self.patronBM)-1+indice-i]
				#print(f"{self.patronBM[len(self.patronBM)-1-i]} NO es igual a: {self.textoBM[len(self.patronBM)-1+indice-i]}")	# Impresion de prueba
				self.comparaciones += f"\n{self.patronBM[len(self.patronBM)-1-i]} NO es igual a: {self.textoBM[len(self.patronBM)-1+indice-i]}"
				# Terminar la busqueda
				return False

		# Regresar que la busqueda se completo sin interrupciones
		return True


	# Metodo que regresa el numero de saltos que se van a realizar
	def obtenerCambio(self):
		# Busca el valor de cambios usando como posicion en la tabla el codigo ASCII del caracter
		# Para obtener el cambio de este metodo se usa el valor del caracter en la tabla
		# restandole el numero de comparaciones que se realizo en la iteracion
		return abs(self.tablaBM[ord(self.caracter)]-self.movimientos)


	def obtenerComparaciones(self):
		return self.comparaciones



# --- Clase principal ---
class PIA:
	# --- Codigo de ejecucion del programa ---
	def ejecutar():
		texto = ""
		
		# Obtencion de datos
		operador = input(
			'\n\nBienvenido! Selecciona la opcion  que quieres utilizar: \n\n   1.-Ingresar datos de Manera manual\n\n   2.-Leer un archivo txt  \n\n ')

		# Obtencion del texto
		if operador == "1":
			texto = input("\nIntroduzca el texto en minusculas -> ")
		elif operador == "2":
			filename = input('\n  Escribe la direccion de tu archivo de texto :   ')
			with open(filename, "r") as file:
				texto = file.read().replace('\n', '')
				if texto == "":
					print("No se pudo leer el texto del archivo, revisa la direccion")
					return 0
		else:
			"Seleccion no valida"
		if texto == "":
			print("Texto invalido")
			return 0

		# Obtencion del patron		
		patron = input("Introduzca el patron en minusculas -> ")
		if patron == "":
			print("Patron invalido")
			return 0

		# Inicializar clases de los metodos / Creacion de tablas de los metodos
		kmp = KMP(texto, patron)
		bm = BM(texto, patron)
		#print("El texto del archivo .txt es: " + texto)


		# Inicializar texto que va a formar el archivo
		textoResultados = ""
		textoResultados += "Tabla dKMP creada de acuerdo a los principios del algoritmo de busqueda de Knuth-Morris-Prath"
		textoResultados += "\nTabla dBM creada de acuerdo a los principios del algoritmo de busqueda de Boyer-Moore"


		# Ejecucion usando el metodo Knuth-Morris-Prath
		indice = 0
		iteraciones = 0
		shiftsKMP = list()
		datosKMP = list()
		# Mientras que el texto tenga espacio suficiente para realizar la busqueda
		#print("\n\t--------------------\t Busqueda usando KMP \t-------------------")
		while len(texto) > (indice+len(patron)-1):
			# Incrementar valor de iteraciones
			iteraciones = iteraciones+1

			# Realizar una iteracion de busqueda de los metodos en el indice indicado
			resultadoKMP = kmp.busqueda(indice)

			# Si uno de los metodos encontro un match
			cambio = 0
			if resultadoKMP:
				#print(f"Patron encontrado en la posicion: {indice+1}  |  Iteraciones: {iteraciones}")	# Descomenta esta linea para comprobar su funcionamiento
				
				# Agregar los datos obtenidos a la lista de resultados
				shiftsKMP.append(iteraciones)

				indice = indice+1
				cambio = 1
			else:
				# Incrementar el indice el numero de cambios definidos
				indice = indice+kmp.obtenerCambio()
				cambio = kmp.obtenerCambio()

			datosKMP.append([iteraciones, (indice-cambio+1), resultadoKMP, cambio])
			#print(f"Iteracion: {iteraciones}\tPosicion: {indice-cambio+1}\tResultado: {resultadoKMP} \tCambio: {cambio}")
		
		# Creacion del archivo de resultados del metodo KMP
		with open('datosKMP.csv', 'w', newline='') as file:
			writer = csv.writer(file, delimiter=",")
			writer.writerows(datosKMP)

		
		# Ejecucion usando el metodo Booyer-Moore
		indice = 0
		iteraciones = 0
		shiftsBM = list()
		datosBM = list()
		#print("\n\t--------------------\t Busqueda usando BM \t-------------------")
		# Mientras que el texto tenga espacio suficiente para realizar la busqueda
		while len(texto) > (indice+len(patron)-1):
			# Incrementar valor de iteraciones
			iteraciones = iteraciones+1

			# Realizar una iteracion de busqueda de los metodos en el indice indicado
			resultadoBM = bm.busqueda(indice)

			# Si uno de los metodos encontro un match
			cambio = 0
			if resultadoBM:
				#print(f"Patron encontrado en la posicion: {indice+1}  |  Iteraciones: {iteraciones}")	# Descomenta esta linea para comprobar su funcionamiento

				# Agregar los datos obtenidos a la lista de resultados
				shiftsBM.append(iteraciones)

				indice = indice+1
				cambio = 1
			else:
				# Incrementar el indice el numero de cambios definidos
				indice = indice+bm.obtenerCambio()
				cambio = bm.obtenerCambio()

			datosBM.append([iteraciones, (indice-cambio+1), resultadoBM, cambio])
			#print(f"Iteracion: {iteraciones}\tPosicion: {indice-cambio+1}\tResultado: {resultadoBM} \tCambio: {cambio}")

		# Creacion del archivo de datos del metodo BM
		with open('datosBM.csv', 'w', newline='') as file:
			writer = csv.writer(file, delimiter=",")
			writer.writerows(datosBM)


		# Ejecucion usando los dos metodos combinados
		indice = 0
		textoResultados += "\nDefinido el valor inicial del indice i, correspondiente a la posicion del patron relativo al texto"
		iteraciones = 0
		posicionesComb = list()
		shiftsComb = list()
		datosComb = list()
		#print("\n\t--------------------\t Busqueda usando metodos combinados \t-------------------")
		# Mientras que el texto tenga espacio suficiente para realizar la busqueda
		while len(texto) > (indice+len(patron)-1):
			# Incrementar valor de iteraciones
			iteraciones = iteraciones+1
			#print(f"Iteracion {iteraciones}")
			textoResultados += f"\n\nIteracion {iteraciones}"

			# Realizar una iteracion de busqueda de los metodos en el indice indicado
			resultadoKMP = kmp.busqueda(indice)
			resultadoBM = bm.busqueda(indice)
			textoResultados += f"\nRealizando busqueda por Knuth-Morris-Prath{kmp.obtenerComparaciones()}"
			textoResultados += f"\nRealizando busqueda por Boyer-Moore{bm.obtenerComparaciones()}"

			# Si uno de los metodos encontro un match
			cambio = 0
			if resultadoKMP  or  resultadoBM:
				#print(f"Patron encontrado en la posicion: {indice+1}  |  Iteraciones: {iteraciones}")	# Descomenta esta linea para comprobar su funcionamiento
				textoResultados += f"\nPatron encontrado en la posicion: {indice+1}  |   Iteraciones: {iteraciones}"
				
				# Agregar los datos obtenidos a la lista de resultados
				posicionesComb.append(indice+1)
				shiftsComb.append(iteraciones)

				indice = indice+1
				cambio = 1
			else:
				# Obtener el mayor cambio establecido por las tablas de los metodos
				#print(f"Escoger el mayor shift entre el establecido por la tabla dKMP ({kmp.obtenerCambio()}) y por la tabla dBM ({bm.obtenerCambio()})")
				textoResultados += f"\nEscoger el mayor shift entre el establecido por la tabla dKMP ({kmp.obtenerCambio()}) y por la tabla dBM ({bm.obtenerCambio()})"
				if kmp.obtenerCambio() > bm.obtenerCambio():
					cambio = kmp.obtenerCambio()
				else:
					cambio = bm.obtenerCambio()

				# Incrementar el indice el numero de cambios definidos
				#print(f"Incrementando el valor de i ({indice}) con el valor del shift definido ({cambio})")
				textoResultados += f"\nIncrementando el valor de i ({indice}) con el valor del shift definido ({cambio})"
				indice = indice+cambio
				
			datosComb.append([iteraciones, (indice-cambio+1), (resultadoKMP or resultadoBM), cambio])
			#print(f"Iteracion: {iteraciones}\tPosicion: {indice-cambio+1}\tResultado: {resultadoKMP or resultadoBM} \tCambio: {cambio}")

		# Creacion del archivo de datos del metodo de algoritmos combinados
		with open('datosComb.csv', 'w', newline='') as file:
			writer = csv.writer(file, delimiter=",")
			writer.writerows(datosComb)


		# Impresion de resultados
		print(f"\n\nNumero de concurrencias del patron en el texto: {len(posicionesComb)}\n")
		textoResultados += f"\n\nNumero de concurrencias del patron en el texto: {len(posicionesComb)}\n"
		if len(posicionesComb) != 0:
			print("\t\t\t\t\t\tShifts")
			textoResultados += "\n\t\t\t\t\t\tShifts"
			print("\t\t\t\t", "-"*33)
			textoResultados += "\n\t\t\t\t" + "-"*33
			print("Palabra\t\tPosicion\t KMP\t\tBM\tCombinados")
			textoResultados += "\nPalabra\t\tPosicion\t KMP\t\tBM\tCombinados"
			for i in range(len(posicionesComb)):
				print(f"{patron}[{i+1}]\t {posicionesComb[i]}\t\t {shiftsKMP[i]}\t\t{shiftsBM[i]}\t    {shiftsComb[i]}")
				textoResultados += f"\n{patron}[{i+1}]\t {posicionesComb[i]}\t\t {shiftsKMP[i]}\t\t{shiftsBM[i]}\t    {shiftsComb[i]}"
		else:
			print(f"\n\nPatron '{patron}' no encontrado en el texto")
			textoResultados += f"\n\nPatron '{patron}' no encontrado en el texto"


		# Creacion del archivo del procedimiento
		file = open("procedimiento.txt", "w")
		file.write(textoResultados)




# Ejecucion del programa
PIA.ejecutar()