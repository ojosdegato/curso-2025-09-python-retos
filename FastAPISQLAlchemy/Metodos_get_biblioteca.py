from fastapi import FastAPI

# Crear la instancia de la aplicación
app = FastAPI()

# Endpoint 1: /libros — devuelve una lista de 3 libros
@app.get("/libros")
def obtener_libros():
    return {
        "libros": [
            "Programación en Python",
            "Programación en Java",
            "2025"
        ]
    }

# Endpoint 2: /biblioteca — devuelve información básica de la biblioteca
@app.get("/biblioteca")
def obtener_biblioteca():
    return {
        "nombre": "Biblioteca Central de Javier Cachón",
        "total_libros": 3,
        "abierta": True
    }
