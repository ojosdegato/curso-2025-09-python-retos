from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# ---------------------------
# Modelos Pydantic
# ---------------------------
class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int

class ProductoPatch(BaseModel):
    nombre: Optional[str] = None
    precio: Optional[float] = None
    stock: Optional[int] = None

# ---------------------------
# Datos iniciales (in-memory)
# ---------------------------
productos = [
    {"id": 1, "nombre": "Teclado Mecánico", "precio": 59.99, "stock": 25},
    {"id": 2, "nombre": "Ratón Inalámbrico", "precio": 24.50, "stock": 40},
]

def _indice_por_id(producto_id: int) -> Optional[int]:
    return next((i for i, p in enumerate(productos) if p["id"] == producto_id), None)

# ---------------------------
# Endpoint PUT (reemplazo total)
# ---------------------------
@app.put("/productos/{producto_id}")
async def actualizar_producto(producto_id: int, producto: Producto):
    idx = _indice_por_id(producto_id)
    if idx is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    # Reemplaza completamente los campos (conservando el id)
    productos[idx] = {"id": producto_id, **producto.model_dump()}
    return productos[idx]

# ---------------------------
# Endpoint PATCH (actualización parcial)
# ---------------------------
@app.patch("/productos/{producto_id}")
async def actualizar_producto_parcial(producto_id: int, cambios: ProductoPatch):
    idx = _indice_por_id(producto_id)
    if idx is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    # Solo aplica los campos enviados
    datos_parciales = cambios.model_dump(exclude_unset=True)
    productos[idx].update(datos_parciales)
    return productos[idx]
