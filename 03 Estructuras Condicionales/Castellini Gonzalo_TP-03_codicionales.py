"""1) Escribir un programa que solicite la edad del usuario."
" Si el usuario es mayor de 18 años, deberá mostrar un mensaje"
" en pantalla que diga “Es mayor de edad”."""

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")


"""2) Escribir un programa que solicite su nota al usuario."
" Si la nota es mayor o igual a 6, deberá mostrar por pantalla "
"un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”."""

nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("APROBADO")
else:
    print("DESAPROBADO")

"""3) Escribir un programa que permita ingresar solo números pares. "
"Si el usuario ingresa un número par, imprimir por en pantalla el mensaje"
" "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "
""Por favor, ingrese un número par"."""

num = int(input("Ingrese un numero par: "))
if num % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")


"""4) Escribir un programa que solicite al usuario su edad e imprima por pantalla "
"a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años. "
"● Adolescente: mayor o igual que 12 años y menor que 18 años. "
"● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. "
"● Adulto/a: mayor o igual que 30 años."""

edad = int(input("Ingrese su edad: "))
if edad < 0:
    print("Valor no valido")
elif edad >= 30:
    print("Adulto (mayor a 30 años)")
elif edad >= 18:
    print("Adulto joven (de 18 a 30 años)")
elif edad >= 12:
    print("Adolecente (de 12 a 18 años)")
else:
    print("Niño (menor de 12 años)")

"""5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14)."
" Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "
""Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "
""Por favor, ingrese una contraseña de entre 8 y 14 caracteres"."""

contrasenia = str(input("Ingrese una contraseña valida entre 8 y 14 caracteres: "))

if len(contrasenia) >= 8 and len(contrasenia) <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


"""6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y "
"calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente:

from statistics import mode, median, mean mi_lista = [1,2,5,5,3] mean(mi_lista)

En la documentación oficial se puede encontrar más información sobre este paquete: https://docs.python.org/es/3.8/library/statistics.html.
La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: "
"● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. "
"● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. "
"● Sin sesgo: cuando la media, la mediana y la moda son iguales. Teniendo en cuenta lo antes mencionado,"
" escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media"
" y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo."
" Imprimir el resultado por pantalla. Definir la lista numeros_aleatorios de la siguiente forma:

import random numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria."""

import random
from statistics import mean, median,mode

# Generar la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

# Calcular la moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Determinar el sesgo de la distribución
if media > mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
else:
    sesgo = "Distribución sin sesgo"

# Imprimir resultados
print(f"Números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")
print(f"Resultado: {sesgo}")

"""7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal,"
"añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario,"
" dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla."""

palabra= input("Ingrese una palabra o una frase: ").lower()
ultLetra = palabra[-1]

if ultLetra == "a" or ultLetra == "e" or ultLetra =="i" or ultLetra == "o" or ultLetra == "u":
    print(palabra + "!")
else:
    print(palabra)


"""8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 "
"dependiendo de la opción que desee:

Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
Si quiere su nombre en minúsculas. Por ejemplo: pedro.
Si quiere su nombre con la primera letra mayúscula. 
"""

nombre = input("Ingrese su nombre: ")
print("1-Si quiere su nombre en mayúsculas.")
print("2-Si quiere su nombre en minusculas.")
print("3-Si quiere su nombre con la primera letra en mayúsculas.")
opcion = int(input("Elija la opcion que desea: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opcion no valida")  

"""9) Escribir un programa que pida al usuario la magnitud de un terremoto, "
"clasifique la magnitud en una de las siguientes categorías según la escala de Richter"
"e imprima el resultado por pantalla: ● Menor que 3: "Muy leve" (imperceptible). "
"● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible). "
"● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). "
"● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). "
"● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos). "
"● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)."""

print("Ingrese la intensidad del terremoto expresada en la escala de Richter")
print("Menor que 3: 'Muy leve'")
print("Mayor o igual que 3 y menor que 4: 'Leve'")
print("Mayor o igual que 4 y menor que 5: 'Moderado'")
print("Mayor o igual que 5 y menor que 6: 'Fuerte'")
print("Mayor o igual que 6 y menor que 7: 'Muy fuerte'")
print("Mayor o igual que 7: 'Extremo'")
intensidad = float(input())

if intensidad < 3:
    print("Muy leve")
elif intensidad < 4:
    print("Leve") 
elif intensidad < 5:
    print("Moderado")
elif intensidad < 6:
    print("Fuerte")      
elif intensidad < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

"""10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año"
" Periodo del año Desde el 21 de diciembre hasta el 20 de marzo (incluidos) "
"Estación en el hemisferio norte Invierno Estación en el hemisferio sur "
"Desde el 21 de marzo hasta el 20 de junio (incluidos) Desde el 21 de junio hasta el 20 de septiembre (incluidos)"
" Desde el 21 de septiembre hasta el 20 de diciembre (incluidos) Primavera Verano Otoño Verano Otoño Invierno Primavera"
" Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), "
"qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla "
"si el usuario se encuentra en otoño, invierno, primavera o verano."""


# Pedimos los datos al usuario
hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el número del día (1-31): "))

# Verificamos si el usuario ingresó un hemisferio válido
if hemisferio not in ["N", "S"]:
    print("Error: Debe ingresar 'N' para hemisferio norte o 'S' para hemisferio sur.")
else:
    # Determinar la estación según el mes y el día
    if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and (mes != 3 or dia <= 20)):
        estacion = "Invierno" if hemisferio == "N" else "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and (mes != 6 or dia <= 20)):
        estacion = "Primavera" if hemisferio == "N" else "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and (mes != 9 or dia <= 20)):
        estacion = "Verano" if hemisferio == "N" else "Invierno"
    else:  # Desde 21 de septiembre hasta 20 de diciembre
        estacion = "Otoño" if hemisferio == "N" else "Primavera"

    print(f"Estás en la estación: {estacion}")


