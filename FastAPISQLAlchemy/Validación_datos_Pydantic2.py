from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Crear la instancia de la aplicación
app = FastAPI(title="API de Productos", description="Registro de productos con modelo Pydantic", version="1.0")


# Modelo Pydantic para representar un producto
class Producto(BaseModel):
    nombre: str
    precio: float
    categoria: str
    disponible: bool = True
    descripcion: Optional[str] = None


# Endpoint POST para registrar un producto
@app.post("/productos")
def registrar_producto(producto: Producto):
    """
    Registra un producto y devuelve un mensaje de confirmación.
    """
    mensaje = f"Producto {producto.nombre} registrado con éxito con precio {producto.precio}€"
    return {"mensaje": mensaje}
