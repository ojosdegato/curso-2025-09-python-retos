#TIPOS DE DATOS

"""Una VARIABLE es un almacen de datos que guarda o almacena un valor específico en la memoria del programa, permitiendo su manipulación y acceso durante la ejecución del código. Utilizamos el símbolo "=" para asignar un valor a la variable. El nombre de las variables debe ser lo más descriptivo posible y no está permitido utilizar las palabras reservadas del lenguaje Python."""

#Imprimir las palabras reservadas de Python por consola.
import keyword
print(keyword.kwlist)


numero = 42 # Sintaxis: variable = valor

_numero = 3 # Los nombre de variables no pueden comenzar por un número ni por un caracter especial, a excepción del _


# Puedo declarar varias variables a la vez
nombre, edad, altura = "Juan", 30, 1

print(nombre) #Imprime "Juan"

# Namning de las variables --> Minúsculas + snake_case

cadena_caracteres = "esto es una cadena con comillas dobles" #str (String)
cadena_de_caracteres_dos = 'esto es una cadena con comillas simples'
dato_numero = 2888 #int (Entero)
dato_decimal = 345.234 #float (Decimal)

del dato_decimal # Eliminamos una variable


""" EJERCICIO 1
Crea 3 variables, una de tipo número que represente tu edad, otra de tipo string que represente tu nombre y otra de tipo decimal que represente tu peso.
Imprime estas variables utilizando la función print() """

edad = 33
nombre = "Alejandra"
peso = 23.67

print("Mi nombre es " + nombre + " y mi edad es " + str(edad)) #Conversión de variables

#Siempre antes y después de un operador, tengo que incluir un espacio (el símbolor = es en Python el operador de asignación, el que utilizamos para asignar un valor a una variable)

cadena = "Hola" #El índice hace referencia a la posición de cada uno de los caracteres dentro de una cadena. El primer caracter en cualquier cadena siempre es el índice 0
print(cadena[0])


""" EJERCICIO 2

Crea un cuento modelo que incluya al menos 10 datos diferentes personalizados del niño o niña al que va dirigido el cuento. La declaración de variables debe ser en bloque. Ejemplo:

ciudad, year, nombre_niño = "Bogotá", 2021, "Nicolás"
print("Amanece en " + ciudad + "en el año " + str(year)+ "..." ) """  

#CONVERSIÓN MAYÚSCULAS-MINÚSCULAS

texto_original = "Hola Mundo"
print(texto_original)

#Conversión a mayúsculas
texto_mayusculas = texto_original.upper()
print(f"Texto en Mayúsculas: {texto_mayusculas}")

#Conversión a minúsculas
texto_minusculas = texto_original.lower()
print(f"Texto en Minúsculas: {texto_minusculas}")  


#Cadenas de caracteres

cadena[1:2] # a una sección de la cadena, en la sección se incluye el primer índice y se excluye el segundo
cadena[1:] # desde un caracter hasta el final
cadena[:3] # desde el principio hasta un caracter
cadena[-1] # A la última posición
cadena[-2] # A la penúltima posición

nueva_cadena = "soy una nueva variable" # Podemos reasignar el valor de una variable

print(nueva_cadena[-2])


""" Para hacer comentarios de bloque --> Seleccionamos todo el texto + atajo de teclado ALT + SHIFT + A """

""" TIPOS CONVERSIÓN DE DATOS 

¿Por qué es importante realizar conversiones de datos en Python?
    · Poder realizar operaciones coherentes.
    · Presentación de los datos
    · Interacción con los usuarios
    · Compatibilidad

TIPOS --->

1 - Casting de datos: Cambiar el tipo de dato de una variable
    numero_entero = int(3.14278974)
    numero_entero_dos = "El numero entero es" +  str(numero_entero)

2 - Concatenación de variables: Combinar variables de diferentes tipos en una cadena
    print("El nombre del usuario es " + name + " y su año de nacimiento es " + str(year))

3 - F-string: Simplificar la creacción de cadenas con variables. Surge con Python3
    name = "Carlos"
    age = 35
    mensaje = f"Hola mi nombre es {name} y mi edad es {age}"

4 - .format : Alternativa más antigua para formatear cadenas. Surgió con Python1
    El método format() se utiliza para construir cadenas que contienen valores de variables.
    La sintaxis básica es:    
    mensaje = "Hola {} y su edad es {}".format(name, age)  #{} -> Marcadores
"""

# 1-2. CASTING DE DATOS
uno = int(3.14278974) #Puedo formatear el tipo de dato incluyendo el valor dentro de la función de tipo correspondiente: int(), str(), float() o bool(). En este ejemplo "3.14278974" se almacena como un número entero, es decir "3"
numero_entero_dos = "El numero entero es " +  str(uno)
print(numero_entero_dos) # En este ejemplo convertimos "uno" en un string

name = "Pepito"
year = 1990
print("El nombre del usuario es " + name + " y su año de nacimiento es " + str(year)) # En este ejemplo convertimos "year" en un string 

print(year + 10) # Operando con datos int

# 3. F-STRING
name = "Carlos"
age = 35
mensaje = f"Hola mi nombre es {name} y mi edad es {age}"
print(mensaje)

# 4. MÉTODO .FORMAT
mensaje = "Hola mi nombre es {} y mi edad es {}".format(name, age)
print(mensaje)



""" FORMATEO DE DATOS EN LA ENTRADA POR TECLADO CON INPUT

entrada_dos = int(input())
entrada_tres = str(input())
entrada_cuatro = float(input()) """
nombre_usuario = str(input("\nIngrese un nombre:\n"))  # salto de línea --> \n 
print(f"Hola, {nombre_usuario}, bienvenido a nuestro programa")