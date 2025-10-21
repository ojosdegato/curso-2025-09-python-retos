print("=== PROGRAMA: INFORMACIÓN DE PRODUCTO ===\n")

# Crear una tupla llamada 'producto' con: nombre, precio y disponibilidad
producto = ("Laptop", 1200.50, True)

print("=== OPERACIÓN 1: VERIFICAR TIPO DE DATO ===")
# 1. Imprime el tipo de dato de la variable 'producto'
print(type(producto))

print("\n=== OPERACIÓN 2: ACCEDER AL NOMBRE ===")
# 2. Accede e imprime el nombre del producto (primer elemento)
print(producto[0])

print("\n=== OPERACIÓN 3: ACCEDER AL PRECIO ===")
# 3. Accede e imprime el precio (segundo elemento)
print(producto[1])

print("\n=== OPERACIÓN 4: DESEMPAQUETADO DE TUPLA ===")
# 4. Utiliza el desempaquetado para asignar cada valor a variables separadas
nombre, precio, disponible = producto

print(f"Variables desempaquetadas:")
print(f"nombre: {nombre}")
print(f"precio: {precio}")
print(f"disponible: {disponible}")

print("\n=== OPERACIÓN 5: MENSAJE FORMATEADO ===")
# 5. Imprime un mensaje formateado con la disponibilidad
estado = "está disponible" if disponible else "no está disponible"

print(f"El producto {nombre} cuesta {precio} euros y {estado}.")
