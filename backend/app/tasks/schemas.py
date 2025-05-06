from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: int
    deadline: Optional[datetime]


class TaskRead(TaskCreate):
    id: int
    completed: bool
    created_at: datetime
    updated_at: datetime
