# Lista de palabras dada
palabras = ["python", "programación", "comprehension", "python", "lista", "conjunto", "programación"]

# 1. List comprehension para convertir todas las palabras a mayúsculas
palabras_mayusculas = [palabra.upper() for palabra in palabras]

# 2. Dict comprehension para crear un diccionario con palabras como claves y sus longitudes como valores
longitudes = {palabra: len(palabra) for palabra in palabras}

# 3. Set comprehension para obtener la primera letra de cada palabra (sin duplicados)
primeras_letras = {palabra[0] for palabra in palabras}

# Imprimir resultados para verificar
print("Lista de palabras en mayúsculas:")
print(palabras_mayusculas)

print("\nDiccionario de palabras y sus longitudes:")
print(longitudes)

print("\nConjunto de primeras letras:")
print(primeras_letras)
