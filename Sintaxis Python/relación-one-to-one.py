print("=== EJERCICIO: RELACIÓN EMPLEADO-TARJETA CORPORATIVA ===\n")

# 1. Crear la clase Empleado con los atributos: id, nombre, cargo, salario
# El atributo 'tarjeta' debe inicializarse como None
class Empleado:
    def __init__(self, id, nombre, cargo, salario):
        self.id = int(id)
        self.nombre = str(nombre)
        self.cargo = str(cargo)
        self.salario = int(salario)  # salario anual
        self.tarjeta = None          # relación one-to-one (se asignará después)

    def asignar_tarjeta(self, tarjeta):
        """
        Asigna una tarjeta corporativa a este empleado, garantizando la relación 1:1.
        Reglas:
        - Un empleado solo puede tener una tarjeta.
        - La tarjeta debe pertenecer (empleado_id) a este empleado.
        """
        if self.tarjeta is not None:
            raise ValueError(f"El empleado {self.id} ya tiene una tarjeta asignada (número: {self.tarjeta.numero}).")
        if tarjeta.empleado_id != self.id:
            raise ValueError(
                f"Inconsistencia: la tarjeta (empleado_id={tarjeta.empleado_id}) "
                f"no pertenece al empleado {self.id}."
            )
        self.tarjeta = tarjeta  # se establece el vínculo


# 2. Crear la clase TarjetaCorporativa con los atributos: id, numero, fecha_emision, empleado_id
class TarjetaCorporativa:
    def __init__(self, id, numero, fecha_emision, empleado_id):
        self.id = int(id)
        self.numero = str(numero)
        self.fecha_emision = str(fecha_emision)  # en formato 'YYYY-MM-DD'
        self.empleado_id = int(empleado_id)      # referencia al propietario


print("=== CREANDO OBJETOS ===")

# 3. Crear un empleado con id: 1, nombre: Alba Motacilla, cargo: Desarrolladora, salario: 45000
empleado = Empleado(id=1, nombre="Alba Motacilla", cargo="Desarrolladora", salario=45000)

# 4. Crear una tarjeta corporativa con id: 1, número: TC001, fecha de emisión: 2025-01-15, id de empleado: 1
tarjeta = TarjetaCorporativa(id=1, numero="TC001", fecha_emision="2025-01-15", empleado_id=1)

print("=== ESTABLECIENDO RELACIÓN ===")

# 5. Asignar la tarjeta al empleado (relación one-to-one)
empleado.asignar_tarjeta(tarjeta)

print("=== VERIFICANDO RELACIÓN ===")

# 6. Imprimir información del empleado y su tarjeta
# Hay para mostrar:
# - Nombre del empleado
# - Número de tarjeta
# - Verificar que la relación es bidireccional (empleado.tarjeta.numero y tarjeta.empleado_id == empleado.id)

print(f"Empleado: {empleado.nombre} (ID: {empleado.id})")
print(f"Cargo: {empleado.cargo}")
print(f"Salario anual: {empleado.salario}")

if empleado.tarjeta is not None:
    print(f"Tarjeta asignada: {empleado.tarjeta.numero}")
    print(f"Fecha emisión: {empleado.tarjeta.fecha_emision}")
else:
    print("Tarjeta asignada: Ninguna")

# Verificación de consistencia (assert lanza excepción si falla)
assert empleado.tarjeta is tarjeta, "El empleado no tiene la tarjeta asignada correctamente."
assert tarjeta.empleado_id == empleado.id, "La tarjeta no pertenece al empleado indicado."

print("\n=== RESULTADO FINAL ===")
# 7. Mostrar un mensaje confirmando la relación one-to-one
print(
    f"Relación ONE-TO-ONE OK: '{empleado.nombre}' tiene exactamente una tarjeta "
    f"('{empleado.tarjeta.numero}') y la tarjeta pertenece al empleado con ID {tarjeta.empleado_id}."
)
