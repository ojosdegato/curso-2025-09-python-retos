print("=== EJERCICIO: RELACIÓN CARPETA-ARCHIVOS ===\n")

# 1. Crear la clase Carpeta con los atributos: id, nombre, fecha_creacion
# El atributo 'archivos' debe inicializarse como una lista vacía
class Carpeta:
    def __init__(self, id, nombre, fecha_creacion):
        self.id = int(id)
        self.nombre = str(nombre)
        self.fecha_creacion = str(fecha_creacion)
        self.archivos = []  # relación one-to-many: 1 carpeta -> muchos archivos

    def agregar_archivo(self, archivo):
        # Validación de consistencia
        if archivo.carpeta_id != self.id:
            raise ValueError(
                f"Inconsistencia: el archivo '{archivo.nombre}.{archivo.extension}' "
                f"(carpeta_id={archivo.carpeta_id}) no pertenece a la carpeta {self.id}."
            )
        # Evitar duplicados por id o por (nombre, extensión)
        if any(a.id == archivo.id or (a.nombre == archivo.nombre and a.extension == archivo.extension)
               for a in self.archivos):
            raise ValueError(
                f"Duplicado: ya existe un archivo con id={archivo.id} o con nombre y extensión "
                f"{archivo.nombre}.{archivo.extension} en la carpeta."
            )
        self.archivos.append(archivo)

# 2. Crear la clase Archivo con los atributos: id, nombre, extension, tamaño, carpeta_id
class Archivo:
    def __init__(self, id, nombre, extension, tamaño, carpeta_id):
        self.id = int(id)
        self.nombre = str(nombre)
        self.extension = str(extension)
        self.tamaño = int(tamaño)       # en bytes
        self.carpeta_id = int(carpeta_id)

    def descripcion(self):
        return f"{self.nombre}.{self.extension} — {self.tamaño} bytes (carpeta_id={self.carpeta_id})"


print("=== CREANDO OBJETOS ===")

# 3. Crear una carpeta con id: 1, nombre: Proyecto Aviberico, fecha de creación: 2025-01-15
carpeta = Carpeta(id=1, nombre="Proyecto Aviberico", fecha_creacion="2025-01-15")

# 4. Crear tres archivos:
# - id: 1, nombre: main, extensión: py, tamaño: 1024, id de carpeta: 1
# - id: 2, nombre: config, extensión: json, tamaño: 512, id de carpeta: 1
# - id: 3, nombre: readme, extensión: md, tamaño: 256, id de carpeta: 1
a1 = Archivo(id=1, nombre="main", extension="py", tamaño=1024, carpeta_id=1)
a2 = Archivo(id=2, nombre="config", extension="json", tamaño=512, carpeta_id=1)
a3 = Archivo(id=3, nombre="readme", extension="md", tamaño=256, carpeta_id=1)

print("=== ESTABLECIENDO RELACIÓN ===")

# 5. Agregar los archivos a la carpeta (relación one-to-many)
carpeta.agregar_archivo(a1)
carpeta.agregar_archivo(a2)
carpeta.agregar_archivo(a3)

print("=== VERIFICANDO RELACIÓN ===")

# 6. Imprimir información de la carpeta y sus archivos
# Hay que mostrar:
# - Nombre de la carpeta
# - Número total de archivos
# - Lista de archivos con sus detalles
print(f"Carpeta: {carpeta.nombre}")
print(f"Fecha de creación: {carpeta.fecha_creacion}")
print(f"Número total de archivos: {len(carpeta.archivos)}")
print("Listado de archivos:")
for archivo in carpeta.archivos:
    print(f" - {archivo.descripcion()}")

print("\n=== RESULTADO FINAL ===")
# 7. Mostrar un mensaje confirmando la relación one-to-many
if all(arch.carpeta_id == carpeta.id for arch in carpeta.archivos) and len(carpeta.archivos) >= 2:
    print("Relación ONE-TO-MANY OK: una carpeta contiene múltiples archivos y cada archivo pertenece a una sola carpeta.")
else:
    print("La relación one-to-many no está correctamente establecida.")
