from fastapi import FastAPI, HTTPException

app = FastAPI()

# Lista inicial de libros
libros = [
    {"id": 1, "titulo": "El Quijote", "autor": "Cervantes"},
    {"id": 2, "titulo": "Cien años de soledad", "autor": "García Márquez"},
    {"id": 3, "titulo": "1984", "autor": "Orwell"}
]

# Endpoint DELETE para eliminar un libro por ID
@app.delete("/libros/{libro_id}")
def eliminar_libro(libro_id: int):
    for libro in libros:
        if libro["id"] == libro_id:
            libros.remove(libro)
            return {"mensaje": "Libro eliminado correctamente"}
    # Si no se encuentra el libro
    raise HTTPException(status_code=404, detail="Libro no encontrado")
