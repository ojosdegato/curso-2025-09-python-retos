print("=== PROGRAMA: JERARQUÍA DE PRODUCTOS ===\n")

# Clase base Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        # Inicializar atributos básicos
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def mostrar_info(self):
        # Devolver información básica del producto
        return f"Producto: {self.nombre} | Precio: {self.precio} € | Stock: {self.stock} unidades"
    
    def hay_stock(self):
        # Verificar si hay unidades disponibles
        return self.stock > 0


# Clase Alimento que hereda de Producto
class Alimento(Producto):
    def __init__(self, nombre, precio, stock, fecha_caducidad):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, precio, stock)
        # Inicializar atributo específico de Alimento
        self.fecha_caducidad = fecha_caducidad
    
    def mostrar_info(self):
        # Sobreescribir el método para incluir fecha de caducidad
        return f"[Alimento] {super().mostrar_info()} | Fecha de caducidad: {self.fecha_caducidad}"


# Clase Electronico que hereda de Producto
class Electronico(Producto):
    def __init__(self, nombre, precio, stock, garantia):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, precio, stock)
        # Inicializar atributo específico de Electronico
        self.garantia = garantia
    
    def mostrar_info(self):
        # Sobreescribir el método para incluir información de garantía
        return f"[Electrónico] {super().mostrar_info()} | Garantía: {self.garantia} meses"


# === CREACIÓN Y PRUEBA DE INSTANCIAS ===
print("=== CREANDO PRODUCTOS ===")

# Crear una instancia de Producto genérico
producto_generico = Producto("Mochila", 25.99, 10)

# Crear una instancia de Alimento
alimento = Alimento("Pan integral", 2.50, 30, "2025-02-15")

# Crear una instancia de Electronico
electronico = Electronico("Auriculares Bluetooth", 59.90, 5, 24)

print("\n=== INFORMACIÓN DE PRODUCTOS ===")

# Mostrar información del producto genérico
print(producto_generico.mostrar_info())

# Mostrar información del alimento
print(alimento.mostrar_info())

# Mostrar información del electrónico
print(electronico.mostrar_info())

print("\n=== VERIFICANDO STOCK ===")

# Verificar stock de cada producto
print(f"{producto_generico.nombre}: {'Disponible' if producto_generico.hay_stock() else 'Agotado'}")
print(f"{alimento.nombre}: {'Disponible' if alimento.hay_stock() else 'Agotado'}")
print(f"{electronico.nombre}: {'Disponible' if electronico.hay_stock() else 'Agotado'}")
