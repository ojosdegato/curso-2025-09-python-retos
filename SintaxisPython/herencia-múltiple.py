print("=== PROGRAMA: SISTEMA DE PERSONAJES CON HERENCIA MÚLTIPLE ===\n")

# Clase base Personaje
class Personaje:
    def __init__(self, nombre, nivel, experiencia, vida, **kwargs):
        super().__init__(**kwargs)  # cooperativo para herencia múltiple
        self.nombre = nombre
        self.nivel = nivel
        self.experiencia = experiencia
        self.vida = vida

    def mostrar_info(self):
        return (f"{self.__class__.__name__} | Nombre: {self.nombre} | "
                f"Nivel: {self.nivel} | EXP: {self.experiencia} | Vida: {self.vida}")

    def subir_nivel(self):
        self.nivel += 1
        self.experiencia += 100
        return f"{self.nombre} ha subido a nivel {self.nivel} (+100 EXP)."


# Clase Guerrero que hereda de Personaje
class Guerrero(Personaje):
    def __init__(self, resistencia, **kwargs):
        super().__init__(**kwargs)
        self.resistencia = resistencia

    def ataque_fisico(self):
        return f"{self.nombre} realiza un ATAQUE FÍSICO con resistencia {self.resistencia}."


# Clase Mago que hereda de Personaje
class Mago(Personaje):
    def __init__(self, mana, **kwargs):
        super().__init__(**kwargs)
        self.mana = mana

    def lanzar_hechizo(self):
        return f"{self.nombre} lanza un HECHIZO consumiendo maná ({self.mana} disponibles)."


# Clase Paladin que hereda de Guerrero y Mago (HERENCIA MÚLTIPLE)
class Paladin(Guerrero, Mago):
    def __init__(self, nombre, nivel, experiencia, vida, resistencia, mana):
        # Herencia cooperativa: todos los super().__init__ participan
        super().__init__(
            nombre=nombre,
            nivel=nivel,
            experiencia=experiencia,
            vida=vida,
            resistencia=resistencia,
            mana=mana
        )

    def mostrar_info(self):
        return (f"{self.__class__.__name__} | Nombre: {self.nombre} | "
                f"Nivel: {self.nivel} | EXP: {self.experiencia} | Vida: {self.vida} | "
                f"Resistencia: {self.resistencia} | Maná: {self.mana}")


# === CREACIÓN Y PRUEBA DE INSTANCIAS ===
print("=== CREANDO PERSONAJES ===")

# Crear una instancia de Guerrero
guts = Guerrero(nombre="Guts", nivel=5, experiencia=450, vida=320, resistencia=80)

# Crear una instancia de Mago
merlin = Mago(nombre="Merlín", nivel=7, experiencia=900, vida=200, mana=150)

# Crear una instancia de Paladin (herencia múltiple)
uther = Paladin(nombre="Uther", nivel=6, experiencia=600, vida=280, resistencia=70, mana=100)

print("\n=== INFORMACIÓN DE PERSONAJES ===")
print(guts.mostrar_info())
print(merlin.mostrar_info())
print(uther.mostrar_info())

print("\n=== DEMOSTRANDO HABILIDADES ===")
print(guts.ataque_fisico())
print(merlin.lanzar_hechizo())
print(uther.ataque_fisico())
print(uther.lanzar_hechizo())

print("\n=== SUBIR NIVEL (BONUS) ===")
print(uther.subir_nivel())
print(uther.mostrar_info())
