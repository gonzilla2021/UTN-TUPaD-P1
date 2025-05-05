# Crear una lista con los números del 1 al 100 que sean múltiplos de 4
# Utilizando la función range

# Método 1: Usando range con paso
multiplos_de_4 = list(range(4, 101, 4))

# Mostrar el resultado
print("Lista de múltiplos de 4 del 1 al 100:")
print(multiplos_de_4)

# Método 2: Alternativa usando comprensión de listas
multiplos_de_4_alt = [num for num in range(1, 101) if num % 4 == 0]

# Verificar que ambos métodos dan el mismo resultado
print("\nVerificación con método alternativo:")
print(multiplos_de_4_alt)

##############################################################################
print(50*"#") # separador para los ejercicios

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
#indexing con números negativos!

elementos = ["agua", "tierra", "fuego", "metal", "madera"]
#utilizando indice negativo
print(elementos[-2])
#utilizando indice positivo
print(elementos[3])

##############################################################################
print(50*"#") # separador para los ejercicios

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla.

lista_vacia = []
lista_vacia.append("Python")
lista_vacia.append("es")
lista_vacia.append("Genial :)")
print(lista_vacia)

##############################################################################
print(50*"#") # separador para los ejercicios

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
#en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"
print(animales)

##############################################################################
print(50*"#") # separador para los ejercicios

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros) 
# Lo que hace este script es remover de una lista dada el numero de mayor valor (n°22) y mostrar la lista resultante.

##############################################################################
print(50*"#") # separador para los ejercicios

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
#pantalla los dos primeros.

lista_num = list(range(10,31,5))
#utilizo la técnica de slicing (rebanado) para mostrar solo los dos primeros elementos.
print(lista_num[:2])

##############################################################################
print(50*"#") # separador para los ejercicios

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
#cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]
autos[1]="fiat"
autos[2]="VW"
print(autos)

##############################################################################
print(50*"#") # separador para los ejercicios

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
#directamente. Imprimir la lista resultante por pantalla.
lista=[5, 10, 15]
dobles=[]
dobles.append(lista[0]*2)
dobles.append(lista[1]*2)
dobles.append(lista[2]*2)
print(dobles)

######Usando un for#############################################################
lista = [5, 10, 15]
dobles = []
for num in lista:
    dobles.append(num * 2)
print(dobles)


##############################################################################
print(50*"#") # separador para los ejercicios

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
#diferentes clientes:

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")

#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
compras[1][1]="tallarines"

#c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")

#d) Imprimir la lista resultante por pantalla
print(f"La lista de compras modificada es: {compras}")

##############################################################################
print(50*"#") # separador para los ejercicios

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.
lista_anidada=[15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)