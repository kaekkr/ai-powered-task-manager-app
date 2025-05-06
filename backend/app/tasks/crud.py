from typing import Optional, List
from sqlmodel import Session, select
from app.tasks.models import Task


def create_task(session: Session, task: Task) -> Task:
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def get_task(session: Session, task_id: int) -> Optional[Task]:
    return session.get(Task, task_id)


def get_tasks(session: Session) -> List[Task]:
    return session.exec(select(Task)).all()


def update_task(session: Session, task_id: int, task_data: Task) -> Optional[Task]:
    task = session.get(Task, task_id)
    if not task:
        return None

    for field, value in task_data.dict(exclude_unset=True).items():
        setattr(task, field, value)

    session.commit()
    session.refresh(task)
    return task


def delete_task(session: Session, task_id: int) -> bool:
    task = session.get(Task, task_id)
    if not task:
        return False

    session.delete(task)
    session.commit()
    return True
