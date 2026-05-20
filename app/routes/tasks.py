from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.task_model import TaskModel
from app.schemas.tasks import TaskCreate, TaskResponse, TaskUpdate
from app.auth.dependencies import get_current_user
from app.models.user_model import UserModel
from app.crud import task_crud

router = APIRouter()

@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    return task_crud.get_tasks(
        db,
        current_user.id
    )

#####################################################################

@router.post("/", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    return task_crud.create_task(
        db,
        task,
        current_user.id
    )

#####################################################################

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    task = task_crud.get_task(
        db,
        task_id,
        current_user.id
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    
    return task

#####################################################################

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    current_task = task_crud.get_task(
        db,
        task_id,
        current_user.id
    )

    if not current_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    
    return task_crud.update_task(
        db,
        current_task,
        task
    )

#####################################################################

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    task = task_crud.get_task(
        db,
        task_id,
        current_user.id
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    
    task_crud.delete_task(
        db,
        task
    )

    return{
        "message": "Task deleted"
    }
