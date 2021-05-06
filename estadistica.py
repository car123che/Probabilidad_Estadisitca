import math
seguir = True
datos = []
#obtener datos
while(seguir):
    try:
        dato = input("Ingrese el dato seguido de enter: ")
        datos.append(float(dato))
    except:
        seguir = False
#inicializacion de variables
suma = 0
n = len(datos)
varianza = 0
desviacion = 0
#imprimir datos obtenidos
print("*******************************LISTA DATOS*******************")
print(datos, "\n")
print("El tamaño de la muestra es: ", n)

#calculo media
for x in datos:
    suma += x
media = suma/n
print("La media es: ", media)

#calculo varianza
sumaCuadrados = 0
for x in datos:
    sumaCuadrados += math.pow((x-media), 2)
varianza = sumaCuadrados/(n-1)
print("La varianza es: ", varianza)

#calculo desviacion
desviacion = math.sqrt(varianza)
print("La desviacion es: ", desviacion)
