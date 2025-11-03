from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Crear la instancia de la aplicación
app = FastAPI(title="Consultorio Médico", version="1.0")


# ===== Modelos Pydantic =====
class Contacto(BaseModel):
    telefono: str
    email: Optional[str] = None


class Paciente(BaseModel):
    nombre: str
    apellido: str
    edad: int
    contacto: Contacto
    alergias: List[str] = []
    activo: bool = True


# ===== "Base de datos" en memoria =====
_pacientes_db: List[dict] = []  # cada item: {"id": int, "data": Paciente}
_next_id: int = 1


# ===== Endpoints =====

# POST /pacientes — Registra un nuevo paciente
@app.post("/pacientes")
def crear_paciente(paciente: Paciente):
    global _next_id
    registro = {"id": _next_id, "data": paciente}
    _pacientes_db.append(registro)

    respuesta = {
        "id": _next_id,
        "mensaje": f"Paciente {paciente.nombre} {paciente.apellido} registrado exitosamente",
        "paciente": {
            "nombre": paciente.nombre,
            "apellido": paciente.apellido,
            "edad": paciente.edad,
            "telefono": paciente.contacto.telefono,
            "tiene_alergias": len(paciente.alergias) > 0
        }
    }

    _next_id += 1
    return respuesta


# GET /pacientes — Lista todos los pacientes (resumen)
@app.get("/pacientes")
def listar_pacientes():
    items = [
        {
            "id": row["id"],
            "nombre": row["data"].nombre,
            "apellido": row["data"].apellido,
            "edad": row["data"].edad,
            "activo": row["data"].activo
        }
        for row in _pacientes_db
    ]
    return {"pacientes": items, "total": len(items)}


# GET /pacientes/{paciente_id} — Devuelve un paciente específico (detalle)
@app.get("/pacientes/{paciente_id}")
def obtener_paciente(paciente_id: int):
    for row in _pacientes_db:
        if row["id"] == paciente_id:
            p = row["data"]
            return {
                "id": paciente_id,
                "nombre": p.nombre,
                "apellido": p.apellido,
                "edad": p.edad,
                "contacto": {
                    "telefono": p.contacto.telefono,
                    "email": p.contacto.email
                },
                "alergias": p.alergias,
                "activo": p.activo
            }
    raise HTTPException(status_code=404, detail="Paciente no encontrado")


# GET /pacientes/activos — Solo pacientes activos (resumen específico)
@app.get("/pacientes/activos")
def pacientes_activos():
    activos = [
        {
            "id": row["id"],
            "nombre_completo": f"{row['data'].nombre} {row['data'].apellido}",
            "edad": row["data"].edad,
            "telefono": row["data"].contacto.telefono
        }
        for row in _pacientes_db
        if row["data"].activo
    ]
    return {"pacientes_activos": activos, "cantidad": len(activos)}
