from sqlalchemy.orm import Session
from app.models.task_model import TaskModel
from app.schemas.tasks import TaskCreate, TaskUpdate

def get_tasks(
        db: Session,
        user_id: int
):
    return db.query(TaskModel).filter(
        TaskModel.owner_id == user_id
    ).all()

#####################################################################

def create_task(
        db: Session,
        task: TaskCreate,
        user_id: int
):
    new_task = TaskModel(
        title=task.title,
        description=task.description,
        owner_id=user_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

#####################################################################

def get_task(
        db: Session,
        task_id: int,
        user_id: int
):
    return db.query(TaskModel).filter(
        TaskModel.id == task_id,
        TaskModel.owner_id == user_id
    ).first()

#####################################################################

def update_task(
        db: Session,
        current_task: TaskModel,
        task: TaskUpdate
):
    current_task.title == task.title
    current_task.description = task.description

    db.commit()
    db.refresh(current_task)

    return current_task

#####################################################################

def delete_task(
        db: Session,
        task: TaskModel
):
    db.delete(task)
    db.commit()
