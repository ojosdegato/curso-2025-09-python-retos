from fastapi import FastAPI, HTTPException

# Crear la aplicación FastAPI
app = FastAPI()

# Lista de libros
libros = [
    {"id": 1, "titulo": "El Quijote", "autor": "Cervantes"},
    {"id": 2, "titulo": "Cien años de soledad", "autor": "García Márquez"},
]

# Crear el endpoint GET
@app.get("/libros/{libro_id}")
def obtener_libro(libro_id: int):
    # Buscar el libro por ID
    libro = next((l for l in libros if l["id"] == libro_id), None)
    if libro is None:
        # Si no se encuentra, lanzar HTTPException
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro
