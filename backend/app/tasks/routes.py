from backend.app.tasks.schemas import TaskCreate, TaskRead
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db.session import get_session
from app.tasks.models import Task
from app.tasks.crud import create_task, get_task, get_tasks

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=list[TaskRead])
def read_tasks(session: Session = Depends(get_session)):
    return get_tasks(session)

@router.get("/{task_id}", response_model=TaskRead)
def read_task(task_id: int, session: Session = Depends(get_session)):
    task = get_task(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/", response_model=TaskRead)
def create(task_data: TaskCreate, session: Session = Depends(get_session)):
	task = Task.from_orm(task_data)
	return create_task(session, task)

@router.put("/{task_id}", response_model=TaskRead)
def update(task_id: int, task_data: TaskCreate, session: Session = Depends(get_session)):
    task = update_task(session, task_id, task_data)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}")
def delete(task_id: int, session: Session = Depends(get_session)):
    if not delete_task(session, task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"ok": True}