#Práctico 11: Aplicación de la Recursividad
#Objetivo:
#Comprender el uso de recursividad en problemas matemáticos simples.
#Resultados de aprendizaje:
#✓ Comprensión y aplicación de la recursividad: El estudiante será capaz de definir y
#comprender el concepto de recursividad, identificando los casos base y recursivos en
#una función recursiva.
#✓ Diseño y desarrollo de algoritmos recursivos: El estudiante será capaz de diseñar
#funciones recursivas para resolver problemas complejos, descomponiendo el problema
#en subproblemas más sencillos.
#✓ Resolución de problemas a través de la recursividad: El estudiante será capaz de aplicar
#la recursividad en la resolución de una variedad de problemas, como la búsqueda en
#estructuras de datos, el ordenamiento y la generación de estructuras combinatorias.
#Ejercicios

"""1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario."""

#Funcion que calcula el factorial
def fact(n):
    if n == 0:      #caso base
        return 1
    else:
        return fact(n-1) * n   #caso recursivo

# Solicitar al usuario el número
numero = int(input("Ingrese un número: "))

# Calcular y mostrar el factorial de todos los números del 1 al número ingresado
for i in range(1, numero + 1):
    print(f"El factorial de {i} es: {fact(i)}")


"""
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique."""

def fibonacci(n):
    if n <= 0:
        return "La posicion debe ser un numero positivo"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_serie_fibonacci(posicion):
    serie = []
    for i in range(1, posicion + 1):
        serie.append(fibonacci(i))
    return serie

# Solicitar la posición al usuario
posicion = int(input("Introduce la posición de la serie de Fibonacci: "))

# Mostrar el valor en la posición específica
print(f"El valor de Fibonacci en la posición {posicion} es: {fibonacci(posicion)}")

# Mostrar la serie completa
serie_completa = mostrar_serie_fibonacci(posicion)
print(f"La serie de Fibonacci hasta la posición {posicion} es: {serie_completa}")


"""
3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛
𝑚 = 𝑛 ∗ 𝑛(𝑚−1)
Prueba esta función en un
algoritmo general."""

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Prueba de la función en un algoritmo general
base = int(input("Introduce el número base: "))
exponente = int(input("Introduce el exponente: "))
resultado = potencia(base, exponente)
print(f"{base} elevado a la potencia de {exponente} es: {resultado}")

"""4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
procedimiento:
1. Dividir el número por 2.
2. Guardar el resto (0 o 1).
3. Repetir el proceso con el cociente hasta que llegue a 0.
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

🧠Ejemplo:
Convertir el número 10 a binario:
10 ÷ 2 = 5 resto: 0
5 ÷ 2 = 2 resto: 1
2 ÷ 2 = 1 resto: 0
1 ÷ 2 = 0 resto: 1
Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010"."""

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Prueba de la función
numero_decimal = 100  # Puedes cambiar este valor para probar con otros números
representacion_binaria = decimal_a_binario(numero_decimal)
print(f"La representación binaria de {numero_decimal} es: {representacion_binaria}")


"""
5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
 Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed()."""

def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 caracteres, es un palíndromo
    if len(palabra) <= 1:
        return True
    # Si el primer y el último carácter son iguales, verifica el resto de la palabra
    elif palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

# Prueba de la función
palabra = input("Introduce una palabra sin espacios ni tildes: ")
resultado = es_palindromo(palabra)
print(f"¿La palabra '{palabra}' es un palíndromo? {resultado}")

"""
6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
 Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)"""

def suma_digitos(n):
    # Caso base: si n es menor que 10, retorna n
    if n < 10:
        return n
    else:
        # Suma el último dígito y llama recursivamente con el número sin el último dígito
        return n % 10 + suma_digitos(n // 10)


# Prueba de la función con ejemplos proporcionados
print(suma_digitos(1234))  # Output: 10
print(suma_digitos(9))     # Output: 9
print(suma_digitos(305))   # Output: 8


"""7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
 Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1)"""


def contar_bloques(n):
    # Caso base: si n es 1, retorna 1
    if n == 1:
        return 1
    else:
        # Suma el número de bloques en el nivel actual y llama recursivamente con el siguiente nivel
        return n + contar_bloques(n - 1)

# Prueba de la función con ejemplos proporcionados
print(f"contar_bloques(1) → {contar_bloques(1)}")  # Output: 1
print(f"contar_bloques(2) → {contar_bloques(2)}")  # Output: 3
print(f"contar_bloques(4) → {contar_bloques(4)}")  # Output: 10

# Ejemplo interactivo
n = int(input("\nIntroduce el número de bloques en el nivel más bajo: "))
total = contar_bloques(n)
print(f"Para una pirámide con {n} bloques en la base se necesitan {total} bloques en total.")



"""8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
 Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4
contar_digito(123456, 7) → 0 """


def contar_digito(numero, digito):
    # Caso especial: si el número es 0 y buscamos el dígito 0
    if numero == 0 and digito == 0:
        return 1
    # Caso base: si el número es 0, retorna 0
    elif numero == 0:
        return 0
    else:
        # Verifica si el último dígito es igual al dígito buscado y suma 1 si es así
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

# Prueba de la función con ejemplos proporcionados
print(f"contar_digito(12233421, 2) → {contar_digito(12233421, 2)}")  # Output: 3
print(f"contar_digito(5555, 5) → {contar_digito(5555, 5)}")          # Output: 4
print(f"contar_digito(123456, 7) → {contar_digito(123456, 7)}")      # Output: 0

# Casos adicionales
print(f"contar_digito(0, 0) → {contar_digito(0, 0)}")                # Output: 1
print(f"contar_digito(1020304, 0) → {contar_digito(1020304, 0)}")    # Output: 3

# Ejemplo interactivo
numero = int(input("\nIntroduce un número entero positivo: "))
digito = int(input("Introduce el dígito a buscar (0-9): "))
resultado = contar_digito(numero, digito)
print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")
