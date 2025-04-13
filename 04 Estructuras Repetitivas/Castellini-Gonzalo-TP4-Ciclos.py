"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""

# Ejemplo usando for
for num in range(0,101):
    print("- ",num)

# Ejemplo con while
num=0
while num < 101: 
    print("- ",num)
    num += 1
########################################################

"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad 
de dígitos que contiene."""
numero=int(input("ingrese un numero: "))
# Tomamos el valor absoluto para contar correctamente los dígitos incluyendo numero negativos
numeroAbs = abs(numero)

# Si el número es 0, tiene una sola cifra
if numeroAbs == 0:
    cifras = 1
else:
    cifras=0
    while numeroAbs > 0:
        numeroAbs = numeroAbs//10
        cifras+=1

print(f"El numero ingresado tiene {cifras} cifra(s)")

########################################################
"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""

# Solicita dos números al usuario
val1 = int(input("Ingrese un número: "))
val2 = int(input("Ingrese otro número: "))

# Inicializa el acumulador
acum = 0

# Determina el menor y el mayor para evitar errores si el orden no es el esperado
inicio = min(val1, val2) + 1  # excluye el menor le sumo 1 para excluir el 1er valor en el calculo
fin = max(val1, val2)         # excluye el mayor también

# Suma los números entre los dos valores dados (excluyéndolos)
while inicio < fin:
    acum += inicio
    inicio += 1

# Muestra el resultado
print(f"La suma de los enteros entre {val1} y {val2}, excluyéndolos, es: {acum}")

#############################################################
"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

# Inicializa la variable que almacenará la suma total
sumatoria = 0

# Pide el primer número al usuario
numero = int(input("Ingrese un número (0 para terminar): "))

# Mientras el número no sea 0, sigue sumando
while numero != 0:
    sumatoria += numero  # Suma el número al total acumulado
    # Pide otro número dentro del bucle
    numero = int(input("Ingrese otro número (0 para terminar): "))

# Cuando se ingresa un 0, se termina el bucle y se muestra la suma total
print("La sumatoria de los números ingresados es:", sumatoria)

########################################################################

"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""  

import random  # Importamos el módulo random para generar números aleatorios

# Generamos un número secreto aleatorio entre 0 y 9
SECRETO = random.randint(0, 9)

# Pedimos al usuario que intente adivinar el número
numero = int(input("Adivina el número secreto (entre 0 y 9): "))
intentos = 1  # Contador de intentos, empezamos con 1 para incluir el ingreso fuera del ciclo

# Mientras el número ingresado no sea igual al secreto, seguimos pidiendo intentos
while numero != SECRETO:  
    intentos += 1 
    numero = int(input("Inténtalo de nuevo: "))  
print("¡Felicitaciones! Adivinaste, el número secreto era", SECRETO)
print("Lo adivinaste en", intentos, "intento(s)")

##########################################################################

"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""

for x in range(100, 0, -2):  # Comienza en 100, termina antes de 0, bajando de 2 en 2
    print("-", x)

##########################################################################
"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""

numero = int(input("Ingrese un número límite: "))

sumatoria = 0  # Inicializamos la variable que almacenará la suma

# Usamos un bucle para sumar todos los números desde 0 hasta el número ingresado (inclusive)
for x in range(0, numero + 1):
    sumatoria += x  # Sumamos el número actual a la sumatoria

# Mostramos el resultado final
print("La sumatoria es", sumatoria)

##########################################################################
"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos."""

# Inicializamos los contadores
contPares = 0
contImpares = 0
contPositivos = 0
contNegativos = 0

# Repetimos 100 veces para ingresar 100 números
for _ in range(100):
    numero = int(input("Ingrese un número: "))

    # Si el número es 0, no lo contamos en ninguna categoría
    if numero == 0:
        continue

    # Verificamos si es par o impar
    if numero % 2 == 0:
        contPares += 1
    else:
        contImpares += 1

    # Verificamos si es positivo o negativo
    if numero > 0:
        contPositivos += 1
    else:
        contNegativos += 1

# Mostramos los resultados
print("Cantidad de números pares:", contPares)
print("Cantidad de números impares:", contImpares)
print("Cantidad de números positivos:", contPositivos)
print("Cantidad de números negativos:", contNegativos)

########################################################################
"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y 
luego calcule la media de esos valores."""

sumatoria = 0  # Acumula la suma de los números
cantidad = 100  # Cantidad total de números a ingresar

# Pedimos al usuario que ingrese 100 números
for _ in range(cantidad):
    numero = int(input("Ingrese un número: "))
    sumatoria += numero  # Sumamos cada número a la sumatoria

# Calculamos y mostramos los resultados
print("Sumatoria:", sumatoria)
print("El promedio de los números es:", sumatoria / cantidad)

############################################################################
"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

numero = int(input("Ingrese un número: "))
invertido = 0  # Aquí se va acumulando el número invertido

# Mientras el número no sea cero
while numero != 0:
    digito = numero % 10            # Obtenemos el último dígito
    invertido = invertido * 10 + digito  # Agregamos el dígito al final del nuevo número
    numero = numero // 10           # Quitamos el último dígito del número original

print("Invertido es:", invertido)


