# Creacion de las filas de las entradas 0 y 1
i0 = [0, 0]
i1 = [0, 0]


# Ingreso de las probabilidades de p para entradas 0 y 1; y probabilidad difusa r
i0[0] = float(input("Ingresa la probabilidad de exito al enviar un valor 0 (> 0.001) -> "))
while i0[0] <= 0.001:
	i0[0] = float(input("Ingresa la probabilidad de exito al enviar un valor 0 (> 0.001) -> "))

i1[1] = float(input("Ingresa la probabilidad de exito al enviar un valor 1 (> 0.001) -> "))
while i1[1] <= 0.001:
	i1[1] = float(input("Ingresa la probabilidad de exito al enviar un valor 1 (> 0.001) -> "))

r = float(input("Ingresa la probabilidad de perdida de informacion (Si no hay ingresa 0) -> "))
while r < 0:
	r = float(input("Ingresa la probabilidad de perdida de informacion (Si no hay ingresa 0) -> "))


# Calculo de las probabilidades de q para entradas 0 y 1
i0[1] = round(1-i0[0]-r, 3)
i1[0] = round(1-i1[1]-r, 3)


# Creacion e impresión de la matriz de probabilidad de transicion y resultado
if r != 0:
	i0.append(r)
	i1.append(r)
Q = [i0, i1]

print("\nMatriz de probabilidades de transicion")
for i in Q:
	print(i)

if i0[0] == i1[1]  and  i0[1] == i1[0]  and  r == 0:
	print("Canal binario simetrico")


