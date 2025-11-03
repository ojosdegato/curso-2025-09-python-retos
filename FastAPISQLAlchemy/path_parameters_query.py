from fastapi import FastAPI

app = FastAPI(title="API de Usuarios", description="Ejemplo con path y query parameters", version="1.0")


# Endpoint que combina path y query parameters
@app.get("/users/{user_id}")
def obtener_usuario(user_id: int, include_email: bool = False, format: str = "basic"):
    """
    Obtiene la información de un usuario específico.
    - user_id: parámetro de ruta (path parameter)
    - include_email: parámetro opcional (query parameter)
    - format: parámetro opcional (query parameter)
    """
    
    usuario = {
        "user_id": user_id,
        "name": f"Usuario {user_id}",
        "format": format
    }
    
    if include_email:
        usuario["email"] = f"user{user_id}@example.com"
    
    return usuario
