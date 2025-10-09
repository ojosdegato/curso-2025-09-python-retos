# Tipos de datos básicos en Python

# Variables
entero = 42
decimal = 3.14159
texto = "Python"
booleano = True

# Conversiones
entero_texto = str(entero)           # entero -> texto
decimal_entero = int(decimal)        # decimal -> entero
texto_lista = list(texto)            # texto -> lista String
booleano_entero = int(booleano)      # booleano -> entero

# Imprimir por type
print("entero:", entero, "| tipo:", type(entero))
print("decimal:", decimal, "| tipo:", type(decimal))
print("texto:", texto, "| tipo:", type(texto))
print("booleano:", booleano, "| tipo:", type(booleano))

print("entero_texto:", entero_texto, "| tipo:", type(entero_texto))
print("decimal_entero:", decimal_entero, "| tipo:", type(decimal_entero))
print("texto_lista:", texto_lista, "| tipo:", type(texto_lista))
print("booleano_entero:", booleano_entero, "| tipo:", type(booleano_entero))
