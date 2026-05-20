from fastapi import FastAPI
from app.routes import tasks
from app.models.task_model import TaskModel
from app.routes import users
from app.models.user_model import UserModel
from app.database.connection import engine

TaskModel.metadata.create_all(bind=engine)
UserModel.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    tasks.router,
    prefix="/tasks",
    tags=["Tasks"]
)

app.include_router(
    users.router,
    prefix="/users",
    tags=["Users"]
)

@app.get("/")
def root():
    return {"message": "Task API running"}
