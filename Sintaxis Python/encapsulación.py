print("=== PROGRAMA: SISTEMA DE CUENTA BANCARIA ===\n")

class CuentaBancaria:
    # Constructor de la clase
    def __init__(self, titular, saldo=0):
        # Inicializar atributos privados
        self._titular = titular
        
        # Usamos la propiedad setter para validar saldo inicial
        self.saldo = saldo
    
    # Propiedad para el titular (solo lectura)
    @property
    def titular(self):
        # Retornar el titular
        return self._titular
    
    # Propiedad getter para el saldo
    @property
    def saldo(self):
        # Retornar el saldo actual
        return self._saldo
    
    # Propiedad setter para el saldo (con validación)
    @saldo.setter
    def saldo(self, nuevo_saldo):
        # Verificar que el saldo no sea negativo
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        # Si es válido, asignar el nuevo saldo
        self._saldo = nuevo_saldo
    
    # Método para depositar dinero
    def depositar(self, cantidad):
        # Verificar que la cantidad sea positiva
        if cantidad > 0:
            # Incrementar el saldo
            self._saldo += cantidad
            # Retornar True indicando éxito
            return True
        # Si la cantidad no es válida, retornar False
        return False
    
    # Método para retirar dinero
    def retirar(self, cantidad):
        # Verificar que la cantidad sea positiva y que haya suficiente saldo
        if cantidad > 0 and cantidad <= self._saldo:
            # Disminuir el saldo
            self._saldo -= cantidad
            # Retornar True indicando éxito
            return True
        # Si no se puede retirar, retornar False
        return False


# === PRUEBAS DE LA CLASE ===
print("=== CREANDO CUENTA BANCARIA ===")
# Crear una cuenta bancaria
cuenta = CuentaBancaria("Javier Cachón", 1000)

print(f"Titular: {cuenta.titular}")
print(f"Saldo inicial: ${cuenta.saldo}")

print("\n=== PROBANDO DEPÓSITOS ===")
# Probar depósito válido
exito_deposito = cuenta.depositar(500)
print(f"Depósito válido (500): {exito_deposito}")

# Probar depósito inválido
exito_deposito_invalido = cuenta.depositar(-200)
print(f"Depósito inválido (-200): {exito_deposito_invalido}")

print(f"Saldo después de operaciones: ${cuenta.saldo}")

print("\n=== PROBANDO RETIROS ===")
# Probar retiro válido
exito_retiro = cuenta.retirar(300)
print(f"Retiro válido (300): {exito_retiro}")

# Probar retiro que excede el saldo
exito_retiro_excedido = cuenta.retirar(5000)
print(f"Retiro excedido (5000): {exito_retiro_excedido}")

print(f"Saldo final: ${cuenta.saldo}")

print("\n=== PROBANDO VALIDACIONES ===")
# Intentar establecer un saldo negativo
try:
    cuenta.saldo = -100
except ValueError as e:
    print(f"Error capturado: {e}")
