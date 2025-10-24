print("=== EJERCICIO: RELACIÓN HABITACIONES-HOTEL ===\n")

# 1. Crear la clase Hotel con los atributos: id, nombre, direccion, estrellas
# El atributo 'habitaciones' debe inicializarse como una lista vacía
class Hotel:
    def __init__(self, id, nombre, direccion, estrellas):
        self.id = int(id)
        self.nombre = str(nombre)
        self.direccion = str(direccion)
        self.estrellas = int(estrellas)
        self.habitaciones = []  # muchas habitaciones -> 1 hotel (many-to-one)

    def agregar_habitacion(self, habitacion):
        """Asocia una habitación a este hotel garantizando la relación many-to-one."""
        # Evitar que una habitación ya asociada a otro hotel se reasigne sin control
        if habitacion.hotel is not None and habitacion.hotel is not self:
            raise ValueError(
                f"La habitación {habitacion.numero} ya pertenece al hotel '{habitacion.hotel.nombre}'."
            )
        # Evitar duplicados por id o número dentro del mismo hotel
        if any(h.id == habitacion.id or h.numero == habitacion.numero for h in self.habitaciones):
            raise ValueError(
                f"Duplicado: ya existe una habitación con id={habitacion.id} o número={habitacion.numero}."
            )
        habitacion.hotel = self  # vínculo desde la habitación hacia el hotel
        self.habitaciones.append(habitacion)

# 2. Crear la clase Habitacion con los atributos: id, numero, tipo, precio
class Habitacion:
    def __init__(self, id, numero, tipo, precio):
        self.id = int(id)
        self.numero = int(numero)
        self.tipo = str(tipo)
        self.precio = int(precio)
        self.hotel = None  # referencia al objeto Hotel (se asignará al agregar)

    def descripcion(self):
        nombre_hotel = self.hotel.nombre if self.hotel else "Sin hotel"
        return f"Hab #{self.numero} — {self.tipo} — {self.precio}€/noche — Hotel: {nombre_hotel}"

print("=== CREANDO OBJETOS ===")

# 3. Crear un hotel con id: 1, nombre: Hotel Carbonero, dirección: Plaza Parus Mayor 123, estrellas: 4
hotel = Hotel(id=1, nombre="Hotel Carbonero", direccion="Plaza Parus Mayor 123", estrellas=4)

# 4. Crear tres habitaciones:
# - id: 1, número: 101, tipo: Individual, precio: 80, hotel: Hotel Carbonero
# - id: 2, número: 102, tipo: Doble, precio: 120, hotel: Hotel Carbonero
# - id: 3, número: 103, tipo: Suite, precio: 200, hotel: Hotel Carbonero
h1 = Habitacion(id=1, numero=101, tipo="Individual", precio=80)
h2 = Habitacion(id=2, numero=102, tipo="Doble", precio=120)
h3 = Habitacion(id=3, numero=103, tipo="Suite", precio=200)

print("=== ESTABLECIENDO RELACIÓN ===")

# 5. Agregar las habitaciones al hotel (relación many-to-one)
hotel.agregar_habitacion(h1)
hotel.agregar_habitacion(h2)
hotel.agregar_habitacion(h3)

print("=== VERIFICANDO RELACIÓN ===")

# 6. Imprimir información del hotel y sus habitaciones
# Hay que mostrar:
# - Nombre del hotel y sus estrellas
# - Número total de habitaciones
# - Lista de habitaciones con sus detalles
print(f"Hotel: {hotel.nombre} ({hotel.estrellas}⭐)")
print(f"Dirección: {hotel.direccion}")
print(f"Número total de habitaciones: {len(hotel.habitaciones)}")
print("Listado de habitaciones:")
for hab in hotel.habitaciones:
    print(f" - {hab.descripcion()}")

print("\n=== RESULTADO FINAL ===")
# 7. Mostrar un mensaje confirmando la relación many-to-one
if all(h.hotel is hotel for h in hotel.habitaciones) and len(hotel.habitaciones) >= 2:
    print("Relación MANY-TO-ONE OK: varias habitaciones pertenecen a un único hotel.")
else:
    print("La relación many-to-one no está correctamente establecida.")
