from fastapi import FastAPI

app = FastAPI(title="API de Productos", description="Ejemplo con path y query parameters", version="1.0")


# Endpoint que combina path y query parameters para productos
@app.get("/products/{product_id}")
def obtener_producto(
    product_id: int,
    include_price: bool = False,
    include_stock: bool = False,
    format: str = "summary"
):
    """
    Obtiene información de un producto específico.
    - product_id: parámetro de ruta (path parameter)
    - include_price: incluir o no el precio
    - include_stock: incluir o no el stock
    - format: formato del resultado (summary o detalle)
    """

    producto = {
        "product_id": product_id,
        "name": f"Producto {product_id}",
        "category": f"Categoría {product_id % 3 + 1}",
        "format": format
    }

    # Añadir precio si el usuario lo solicita
    if include_price:
        producto["price"] = f"{product_id * 10}.99"

    # Añadir stock si el usuario lo solicita
    if include_stock:
        producto["stock"] = product_id * 5

    return producto
