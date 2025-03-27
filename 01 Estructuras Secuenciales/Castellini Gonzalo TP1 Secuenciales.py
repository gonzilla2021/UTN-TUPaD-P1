import math # importamos la libreria para el ej 4

#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 
print("Hola Mundo!")

"""2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
realizar la impresión por pantalla."""

nombre = str(input("Ingrese su nombre: "))
print(f"Hola {nombre}")

"""3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
la impresión por pantalla."""

nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
edad = int(input("Ingrese su edad: "))
lugar = str(input("Ingrese su lugar de residencia: "))

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

"""4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
su perímetro."""


radio = float(input("Ingrese el radio del circulo: "))
area = math.pi* radio**2
perimetro = 2* math.pi* radio

print(f"Para una circunferencia de radio {radio}, su area es {area} y su perimetro es {perimetro}")

"""5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
cuántas horas equivale."""

segundos=int(input("Ingrese la cantidad de segundos que desea convertir: "))
#Cálculo de horas: segundos // 3600 obtiene la cantidad de horas completas.
horas = segundos // 3600
#Cálculo de minutos: (segundos % 3600) // 60 obtiene los minutos restantes después de calcular las horas.
minutos = (segundos % 3600) //60
#Cálculo de segundos: segundos % 60 obtiene los segundos restantes después de calcular las horas y los minutos.
segundos = segundos % 60
print(f"Los segundos ingresados equivalen a {horas} horas, {minutos} minutos y {segundos} segundos")

"""6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
multiplicar de dicho número. 
"""
numero = int(input("Escriba un numero para crear la tablas: "))
for i in range (11):
    print (f"{numero} x {i} = {numero * i}")

"""7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. """  

num1 = int(input("Escriba un numero: "))
num2 = int(input("Escriba otro numero: "))

print(f"SUMA: {num1} + {num2} = {num1 + num2}")
print(f"RESTA: {num1} - {num2} = {num1 - num2}")
print(f"MULTIPLICACION: {num1} X {num2} = {num1 * num2}")
if num2 != 0:
    print(f"DIVISION: {num1} / {num2} = {num1 / num2}")
else:
    print("No se puede hacer la DIVISION porque el divisor no puede ser 0")

"""8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
de masa corporal. 
"""
altura= float(input("Escriba su altura en m: "))
peso = float(input("Escriba su peso en kg: "))
# con round redondeo a 2 decimales
imc = round(peso / altura**2, 2)

print(f"Su indice de masa corporal es: {imc}")

""" 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 

temperatura en fahrenheit = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 en celsius   + 32
"""
tempcelsius = float(input("Ingresa la temperatura en grados Celsius"))
temfahrenheit = 9/5 * tempcelsius + 32
print(f"Los {tempcelsius} °C, equivalen a {temfahrenheit} °F")

""" 10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
dichos números. """

num1 = int(input("Escriba un numero: "))
num2 = int(input("Escriba otro numero: "))
num3 = int(input("Escriba el ultimo numero: "))
promedio = (num1 + num2 + num3)/3
print(f"El promedio de los numeros ingresados es : {promedio}")
