from fastapi import FastAPI

# Crear la instancia de la aplicación
app = FastAPI()

@app.get("/animales")
def obtener_animales():
    return {"animales": ["León", "Elefante", "Jirafa", "Tigre"]}

@app.get("/zoologico")
def obtener_zoologico():
    return {
        "nombre": "Zoológico Safari",
        "total_animales": 250,
        "abierto": True,
        "horario": "9:00 - 18:00"
    }

@app.get("/estadisticas")
def obtener_estadisticas():
    return {
        "informacion_general": {
            "nombre": "Zoológico Safari",
            "ubicacion": "Parque Central"
        },
        "datos_animales": {
            "total_especies": 45,
            "animales_populares": ["León", "Elefante", "Mono"]
        },
        "estado_operacional": {
            "abierto": True,
            "empleados_presentes": 12
        }
    }