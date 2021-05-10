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
#ordenar datos
datos.sort()
#imprimir datos obtenidos
print("*******************************LISTA DATOS*******************")
print(datos, "\n")
print("El tamaño de la muestra es: ", n)

#calculo media
for x in datos:
    suma += x
media = suma/n
print("La media es: ", media)

#calculo mediana
mediana  = 0
if n%2 != 0: #si es impar
    z = int((n+1)/2)
    mediana = datos[z-1]
else: #si es par
    z = int(n/2)
    datoUno = datos[z-1]
    datosDos = datos[z]
    mediana = (datoUno + datosDos) / 2
print("La mediana es: ", mediana)

#calculo varianza
sumaCuadrados = 0
for x in datos:
    sumaCuadrados += math.pow((x-media), 2)
varianza = sumaCuadrados/(n-1)
print("La varianza es: ", varianza)

#calculo desviacion
desviacion = math.sqrt(varianza)
print("La desviacion es: ", desviacion)
