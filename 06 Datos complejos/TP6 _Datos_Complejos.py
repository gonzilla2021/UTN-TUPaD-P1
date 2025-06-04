"""
TP6 - Datos Complejos
Trabajo Práctico sobre diccionarios, sets y tuplas en Python
"""

# ==================== EJERCICIO 1 ====================
"""
1) Dado el diccionario precios_frutas, añadir las siguientes frutas:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""

# Diccionario inicial
precios_frutas = {'Banana': 1200,
                  'Ananá': 2500,
                  'Melón': 3000,
                  'Uva': 1450}

# Método 1: Agregar elemento por elemento usando corchetes
precios_frutas["Naranja"] = 1200

# Método 2: Crear un diccionario auxiliar y usar update()
nuevas_frutas = {"Manzana": 1500, "Pera": 2300}
precios_frutas.update(nuevas_frutas)  # Agrega múltiples elementos de una vez

print("Ejercicio 1 - Diccionario con frutas agregadas:")
print(precios_frutas)
print()

# ==================== EJERCICIO 2 ====================
"""
2) Actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""

# Reinicializar el diccionario para este ejercicio
precios_frutas = {'Banana': 1200,
                  'Ananá': 2500,
                  'Melón': 3000,
                  'Uva': 1450,
                  'Naranja': 1200,
                  'Manzana': 1500,
                  'Pera': 2300}

# Actualizar precios (sobrescribir valores existentes)
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print("Ejercicio 2 - Precios actualizados:")
print(precios_frutas)
print()

# ==================== EJERCICIO 3 ====================
"""
3) Crear una lista que contenga únicamente las frutas sin los precios
"""

# Obtener solo las claves (nombres de frutas) y convertir a lista
frutas_sin_precios = list(precios_frutas.keys())

print("Ejercicio 3 - Lista de frutas sin precios:")
print(frutas_sin_precios)
print()

# ==================== EJERCICIO 4 ====================
"""
4) Programa para almacenar y consultar números telefónicos
• Cargar 5 contactos con nombre como clave y número como valor
• Buscar un contacto por nombre
"""

# Inicializar diccionario vacío para contactos
contactos = {}

print("Ejercicio 4 - Agenda telefónica")
print("Ingrese 5 contactos:")

# Cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    contactos[nombre] = numero

print(f"\nContactos guardados: {contactos}")

# Buscar un contacto
nombre_buscar = input("\nIngrese el nombre del contacto a buscar: ")
if nombre_buscar in contactos:
    print(f"El número de {nombre_buscar} es {contactos[nombre_buscar]}")
else:
    print(f"El contacto '{nombre_buscar}' no existe en la agenda")
print()

# ==================== EJERCICIO 5 ====================
"""
5) Solicitar una frase e imprimir:
• Las palabras únicas (usando un set)
• Un diccionario con la cantidad de veces que aparece cada palabra
"""

print("Ejercicio 5 - Análisis de texto")
frase = input("Introduce una frase: ")

# Dividir la frase en palabras (convertir a minúsculas para mejor análisis)
palabras = frase.lower().split()

# Crear un set con las palabras únicas
palabras_unicas = set(palabras)

# Método 1: Contar palabras manualmente
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

# Método 2 alternativo: Usar get() para simplificar
# contador_palabras = {}
# for palabra in palabras:
#     contador_palabras[palabra] = contador_palabras.get(palabra, 0) + 1

print(f"Palabras únicas: {palabras_unicas}")
print(f"Conteo de palabras: {contador_palabras}")
print()

# ==================== EJERCICIO 6 ====================
"""
6) Ingresar nombres de 3 alumnos y para cada uno una tupla de 3 notas
Mostrar el promedio de cada alumno
"""

print("Ejercicio 6 - Promedios de alumnos")
alumnos = {}

# Ingreso de datos para 3 alumnos
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    
    # Crear tupla con 3 notas
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    
    # Convertir lista a tupla y guardar en diccionario
    alumnos[nombre] = tuple(notas)

# Calcular y mostrar promedios
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f} (notas: {notas})")
print()

# ==================== EJERCICIO 7 ====================
"""
7) Dados dos sets de estudiantes que aprobaron Parcial 1 y Parcial 2:
• Mostrar los que aprobaron ambos parciales (intersección)
• Mostrar los que aprobaron solo uno de los dos (diferencia simétrica)
• Mostrar la lista total de estudiantes que aprobaron al menos un parcial (unión)
"""

print("Ejercicio 7 - Análisis de parciales")

# Sets de estudiantes que aprobaron cada parcial
primer_parcial = {"juan", "pedro", "luis", "vanesa", "gonzalo", "lautaro"}
segundo_parcial = {"jose", "david", "vanesa", "gonzalo", "lautaro"}

print(f"Aprobaron Parcial 1: {primer_parcial}")
print(f"Aprobaron Parcial 2: {segundo_parcial}")

# Intersección: estudiantes que aprobaron AMBOS parciales
ambos_parciales = primer_parcial & segundo_parcial
print(f"Aprobaron ambos parciales: {ambos_parciales}")

# Diferencia simétrica: estudiantes que aprobaron SOLO UNO de los parciales
solo_uno = primer_parcial ^ segundo_parcial
print(f"Aprobaron solo uno de los parciales: {solo_uno}")

# Unión: estudiantes que aprobaron AL MENOS UN parcial
al_menos_uno = primer_parcial | segundo_parcial
print(f"Aprobaron al menos un parcial: {al_menos_uno}")
print()

# ==================== EJERCICIO 8 ====================
"""
8) Diccionario de productos con stock. Permitir:
• Consultar el stock de un producto
• Agregar unidades al stock si el producto existe
• Agregar un nuevo producto si no existe
"""

print("Ejercicio 8 - Gestión de inventario")

# Diccionario inicial de productos y stock
productos = {"aire": 500, "estufa": 100, "ventilador": 50, "heladera": 200}

print(f"Inventario inicial: {productos}")

# Consultar stock de un producto
producto_consulta = input("Ingrese el producto para consultar stock: ")
if producto_consulta in productos:
    print(f"Stock disponible de '{producto_consulta}': {productos[producto_consulta]} unidades")
else:
    print(f"El producto '{producto_consulta}' no existe en el inventario")

# Agregar o actualizar stock
producto_stock = input("Ingrese el producto para agregar/actualizar stock: ")
cantidad = int(input(f"Ingrese la cantidad a agregar para '{producto_stock}': "))

if producto_stock in productos:
    # Producto existe: agregar al stock actual
    productos[producto_stock] += cantidad
    print(f"Stock actualizado de '{producto_stock}': {productos[producto_stock]} unidades")
else:
    # Producto no existe: crear nuevo con la cantidad especificada
    productos[producto_stock] = cantidad
    print(f"Nuevo producto '{producto_stock}' agregado con {cantidad} unidades")

print(f"Inventario final: {productos}")
print()

# ==================== EJERCICIO 9 ====================
"""
9) Crear una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos
Permitir consultar qué actividad hay en cierto día y hora
"""

print("Ejercicio 9 - Agenda con tuplas")

# Agenda usando tuplas (día, hora) como claves
agenda = {
    ("lunes", "09:00"): "Reunión de equipo",
    ("lunes", "14:00"): "Almuerzo con cliente",
    ("lunes", "16:30"): "Revisión de proyecto",
    ("martes", "10:00"): "Presentación trimestral",
    ("martes", "15:00"): "Capacitación Python",
    ("miercoles", "11:00"): "Consulta médica",
    ("miercoles", "17:00"): "Gimnasio",
    ("jueves", "08:30"): "Desayuno de trabajo",
    ("jueves", "13:00"): "Reunión con proveedores",
    ("viernes", "09:30"): "Planificación semanal",
    ("viernes", "18:00"): "Cena familiar"
}

# Mostrar toda la agenda
print("Agenda completa:")
for (dia, hora), evento in agenda.items():
    print(f"{dia.capitalize()} {hora} - {evento}")

# Consultar actividad específica
dia_consulta = input("\nIngrese el día de la semana a consultar: ").lower()
hora_consulta = input("Ingrese la hora (formato HH:MM): ")

# Crear tupla para buscar en el diccionario
clave_busqueda = (dia_consulta, hora_consulta)

if clave_busqueda in agenda:
    print(f"El {dia_consulta} a las {hora_consulta} tienes: {agenda[clave_busqueda]}")
else:
    print(f"No hay actividades programadas el {dia_consulta} a las {hora_consulta}")
print()

# ==================== EJERCICIO 10 ====================
"""
10) Dado un diccionario que mapea países con sus capitales, construir un nuevo diccionario donde:
• Las capitales sean las claves
• Los países sean los valores
"""

print("Ejercicio 10 - Inversión de diccionario")

# Diccionario original: países -> capitales
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "Perú": "Lima",
    "Uruguay": "Montevideo",
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma",
    "Japón": "Tokio"
}

print("Diccionario original (países -> capitales):")
for pais, capital in paises_capitales.items():
    print(f"{pais} -> {capital}")

# Invertir el diccionario usando comprensión de diccionario
# Intercambia claves y valores: capitales -> países
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

print("\nDiccionario invertido (capitales -> países):")
for capital, pais in capitales_paises.items():
    print(f"{capital} -> {pais}")



