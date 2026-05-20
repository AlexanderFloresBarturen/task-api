from pydantic import BaseModel

# Esto define cómo debe verse un tarea
class Task(BaseModel):
    title: str
    description: str

# Recibe datos del usuario
class TaskCreate(Task):
    pass

# Devuelve datos desde la DB
class TaskResponse(Task):
    id: int

    class Config:
        # Permite convertir modelos SQLAlchemy a respuestas FastAPI
        from_attributes = True

class TaskUpdate(Task):
    pass
