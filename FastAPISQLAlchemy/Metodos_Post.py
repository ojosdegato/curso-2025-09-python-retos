from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo Pydantic: Libro
class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int

# Endpoint POST para crear un libro
@app.post("/libros")
async def crear_libro(libro: Libro):
    return {
        "mensaje": "Libro creado exitosamente",
        "datos": libro
    }
