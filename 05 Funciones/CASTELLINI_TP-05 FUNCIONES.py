"""1. Crear una función llamada imprimir_hola_mundo que imprima por
 pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
 programa principal."""

#Funcion
def imprimir_hola_mundo():
    print("Hola Mundooooo!!!")
   
#Programa principal
imprimir_hola_mundo()

""" 2. Crear una función llamada saludar_usuario(nombre) que reciba
 como parámetro un nombre y devuelva un saludo personalizado.
 Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
volver: “Hola Marcos!”. Llamar a esta función desde el programa
 principal solicitando el nombre al usuario"""


#Usando return (más literal al enunciado)
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Llamada desde el programa principal
nombre_usuario = input("Ingrese su nombre de usuario: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)


""" 3. Crear una función llamada informacion_personal(nombre, apellido,
 edad, residencia) que reciba cuatro parámetros e imprima: “Soy
 [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
dir los datos al usuario y llamar a esta función con los valores in
gresados."""

#Funcion
def informacion_personal(nombre, apellido, edad, residencia):
  return f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}"

#Progama
nombre=input("Ingrese su nombre:")
apellido=input("Ingrese su apellido:")
edad=int(input("Ingrese su edad:"))
residencia=input("Ingrese su lugar de residencia")
datos=informacion_personal(nombre, apellido, edad, residencia)
print(datos)

""" 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
dio como parámetro y devuelva el área del círculo. calcular_peri
metro_circulo(radio) que reciba el radio como parámetro y devuel
va el perímetro del círculo. Solicitar el radio al usuario y llamar am
bas funciones para mostrar los resultados."""

import math #importo modulo math para obtener un valor mas aproximado de PI
def calcular_area_circulo(radio):
  return math.pi * (radio**2)

def calcular_perimetro_circulo(radio):
  return 2 * math.pi * radio


radio=float(input("Ingrese el radio del circulo "))
area=calcular_area_circulo(radio)
perimetro=calcular_perimetro_circulo(radio)
print(f"El Area calculada es: {area:.2f} cm y el Perimetro calculado es: {perimetro:.2f}") #:.2f es un especificador de formato sirve para mostrar solo 2 decimales

""" 5. Crear una función llamada segundos_a_horas(segundos) que reciba
 una cantidad de segundos como parámetro y devuelva la cantidad
 de horas correspondientes. Solicitar al usuario los segundos y mos
trar el resultado usando esta función."""
#Funcion
def segundos_a_horas(segundos):
   return segundos /3600

#Programa   
segundos=int(input("ingrese los Segundos: "))
horas=segundos_a_horas(segundos)
print(f"Los {segundos} segundos ingresados, equivalen a {horas:.2f} horas")   

""" 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
 número como parámetro y imprima la tabla de multiplicar de ese
 número del 1 al 10. Pedir al usuario el número y llamar a la fun
ción."""
#Funcion
def tabla_multiplicar(numero):
  for i in range(1,11):
    print(f"{i} x {numero} = {i*numero}")

#Programa
numero=int(input("Ingrese un numero para mostrar su tabla de multiplicar: "))
tabla_multiplicar(numero)

"""7. Crear una función llamada operaciones_basicas(a, b) que reciba
 dos números como parámetros y devuelva una tupla con el resulta
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
sultados de forma clara."""

#Funcion
def operaciones_basicas(a, b):
  suma= a+b
  resta=a-b
  multiplicacion=a*b
  # Manejo de división por cero
  if b != 0:
        division = a / b
  else:
        division = "No definida (división por cero)"
  return suma, resta, multiplicacion, division # retorna una tupla

#Porgrama
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese un numero que sea 0: "))

#muestro la tupla
operaciones=operaciones_basicas(num1,num2)
print(f"La tupla retornada por la funcion es: {operaciones}")

#Desempaquetado de la tupla para asignar susu valores a las operaciones y luego mostrarlas
suma, resta, multiplicacion, division = operaciones
print(f"\nResultados de las operaciones básicas:")
print(f"Suma:           {num1} + {num2} = {suma}")
print(f"Resta:          {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} x {num2} = {multiplicacion}")
print(f"División:       {num1} ÷ {num2} = {division}")

""" 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
 peso en kilogramos y la altura en metros, y devuelva el índice de
 masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
ción para mostrar el resultado con dos decimales."""

def calcular_imc(peso, altura):
  return peso / (altura**2)

peso=float(input("Ingrese su peso el kg: "))
altura=float(input("Ingrese su altura En m: "))  
IMC=calcular_imc(peso, altura)
print(f"El IMC es: {IMC:.2f}")

""" 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
 una temperatura en grados Celsius y devuelva su equivalente en
 Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
 resultado usando la función."""

def celsius_a_fahrenheit(celsius):
  return celsius * 1.8 + 32

celsius=float(input("Ingrese la temperatura en °C: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivale a {fahrenheit}°F")

"""10.Crear una función llamada calcular_promedio(a, b, c) que reciba
 tres números como parámetros y devuelva el promedio de ellos.
 Solicitar los números al usuario y mostrar el resultado usando esta
 función."""
#Funcion
def calcular_promedio(a, b, c):
  return (a+b+c)/3
#Programa
num1=float(input("Ingrese un numero: "))
num2=float(input("Ingrese un numero: "))
num3=float(input("Ingrese un numero: "))
promedio= calcular_promedio(num1, num2, num3) 
print(f"El promedio de los numeros {num1}, {num2}, {num3} es {promedio:.2f}")