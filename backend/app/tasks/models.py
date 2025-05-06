from datetime import datetime, timezone
from typing import Optional
from sqlmodel import Field, SQLModel


class Task(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str = Field(index=True)
    description: Optional[str] = Field(default=None)
    priority: int = Field(index=True)
    deadline: Optional[datetime] = Field(default=None)
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    deleted_at: Optional[datetime] = Field(default=None)
