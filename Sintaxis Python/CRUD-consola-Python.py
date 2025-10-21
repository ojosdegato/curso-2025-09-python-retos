from dataclasses import dataclass

# =========================
# MODELO
# =========================
@dataclass
class Product:
    id: int
    nombre: str
    precio: float
    stock: int

    def __str__(self) -> str:
        return f"[ID:{self.id}] {self.nombre} | Precio: €{self.precio:.2f} | Stock: {self.stock}"


# =========================
# UTILIDADES DE ENTRADA
# =========================
def input_entero(msg: str, minimo: int = None) -> int:
    while True:
        try:
            valor = int(input(msg).strip())
            if minimo is not None and valor < minimo:
                print(f" Debe ser un entero ≥ {minimo}.")
                continue
            return valor
        except ValueError:
            print(" Entrada inválida. Introduce un número entero.")


def input_flotante(msg: str, minimo: float = None) -> float:
    while True:
        try:
            valor = float(input(msg).strip().replace(",", "."))  # aceptar coma
            if minimo is not None and valor < minimo:
                print(f" Debe ser un número ≥ {minimo}.")
                continue
            return valor
        except ValueError:
            print(" Entrada inválida. Introduce un número (usa punto o coma).")


def input_texto(msg: str) -> str:
    while True:
        txt = input(msg).strip()
        if txt:
            return txt
        print(" El nombre no puede estar vacío.")


def confirmar(msg: str = "¿Confirmas? (s/N): ") -> bool:
    return input(msg).strip().lower() in {"s", "si", "sí", "y", "yes"}


# =========================
# OPERACIONES CRUD
# =========================
def id_existe(productos: list[Product], id_: int) -> bool:
    return any(p.id == id_ for p in productos)


def buscar_producto_por_id(productos: list[Product], id_: int) -> Product | None:
    for p in productos:
        if p.id == id_:
            return p
    return None


def crear_producto(productos: list[Product]) -> None:
    print("\n— Crear producto —")
    id_ = input_entero("ID (entero, único): ", minimo=0)
    if id_existe(productos, id_):
        print(f" El ID {id_} ya existe. Operación cancelada.")
        return

    nombre = input_texto("Nombre: ")
    precio = input_flotante("Precio (€): ", minimo=0.0)
    if precio <= 0:
        print(" El precio debe ser positivo.")
        return

    stock = input_entero("Stock (entero ≥ 0): ", minimo=0)

    prod = Product(id=id_, nombre=nombre, precio=precio, stock=stock)
    productos.append(prod)
    print(f" Producto creado: {prod}")


def mostrar_todos_productos(productos: list[Product]) -> None:
    print("\n— Listado de productos —")
    if not productos:
        print("  La lista está vacía.")
        return

    # Cabecera tabular simple
    print(f"{'ID':>4}  {'NOMBRE':<30} {'PRECIO (€)':>12} {'STOCK':>7}")
    print("-" * 60)
    for p in productos:
        print(f"{p.id:>4}  {p.nombre:<30.30} {p.precio:>12.2f} {p.stock:>7d}")
    print(f"\nTotal: {len(productos)} producto(s).")


def buscar_producto_interactivo(productos: list[Product]) -> None:
    print("\n— Buscar por ID —")
    if not productos:
        print("  La lista está vacía.")
        return
    id_ = input_entero("ID a buscar: ", minimo=0)
    p = buscar_producto_por_id(productos, id_)
    if p:
        print(f" Encontrado: {p}")
    else:
        print(f" No existe un producto con ID {id_}.")


def actualizar_producto(productos: list[Product]) -> None:
    print("\n— Actualizar producto —")
    if not productos:
        print("  La lista está vacía.")
        return

    id_ = input_entero("ID del producto a actualizar: ", minimo=0)
    p = buscar_producto_por_id(productos, id_)
    if not p:
        print(f" No existe un producto con ID {id_}.")
        return

    print(f"Actualizando: {p}")
    print("Pulsa Enter para mantener el valor actual.")

    # Nombre
    nuevo_nombre = input(f"Nuevo nombre [{p.nombre}]: ").strip()
    if nuevo_nombre:
        p.nombre = nuevo_nombre

    # Precio
    entrada_precio = input(f"Nuevo precio (€) [{p.precio:.2f}]: ").strip()
    if entrada_precio:
        try:
            nuevo_precio = float(entrada_precio.replace(",", "."))
            if nuevo_precio <= 0:
                print(" El precio debe ser positivo. No se actualiza el precio.")
            else:
                p.precio = nuevo_precio
        except ValueError:
            print(" Precio inválido. No se actualiza el precio.")

    # Stock
    entrada_stock = input(f"Nuevo stock [{p.stock}]: ").strip()
    if entrada_stock:
        try:
            nuevo_stock = int(entrada_stock)
            if nuevo_stock < 0:
                print(" El stock no puede ser negativo. No se actualiza el stock.")
            else:
                p.stock = nuevo_stock
        except ValueError:
            print(" Stock inválido. No se actualiza el stock.")

    print(f" Producto actualizado: {p}")


def eliminar_producto(productos: list[Product]) -> None:
    print("\n— Eliminar producto —")
    if not productos:
        print("  La lista está vacía.")
        return

    id_ = input_entero("ID del producto a eliminar: ", minimo=0)
    p = buscar_producto_por_id(productos, id_)
    if not p:
        print(f" No existe un producto con ID {id_}.")
        return

    print(f"Vas a eliminar: {p}")
    if confirmar("¿Confirmas eliminación? (s/N): "):
        # remover por identidad
        productos.remove(p)
        print("  Producto eliminado correctamente.")
    else:
        print(" Operación cancelada por el usuario.")


# =========================
# MENÚ
# =========================
def mostrar_menu() -> None:
    print(
        """
========= CRUD de Productos =========
1) Crear producto
2) Listar todos
3) Buscar por ID
4) Actualizar producto
5) Eliminar producto
0) Salir
------------------------------------
"""
    )


def main():
    productos: list[Product] = []

    while True:
        try:
            mostrar_menu()
            opcion = input("Elige una opción: ").strip()

            if opcion == "1":
                crear_producto(productos)
            elif opcion == "2":
                mostrar_todos_productos(productos)
            elif opcion == "3":
                buscar_producto_interactivo(productos)
            elif opcion == "4":
                actualizar_producto(productos)
            elif opcion == "5":
                eliminar_producto(productos)
            elif opcion == "0":
                print(" Saliendo… ¡gracias!")
                break
            else:
                print("  Opción inválida. Intenta de nuevo.")
        except KeyboardInterrupt:
            print("\n  Interrumpido por el usuario. Usa la opción 0 para salir.")
        except Exception as e:
            # “airbag” general para que la app no se caiga por errores no previstos
            print(f" Ocurrió un error inesperado: {e!r}")

        input("\nPulsa Enter para continuar…")


if __name__ == "__main__":
    main()
