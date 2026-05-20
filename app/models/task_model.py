from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.connection import Base

# Definimos la tabla tasks
class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    description = Column(String)

    owner_id = Column(Integer, ForeignKey("users.id"))