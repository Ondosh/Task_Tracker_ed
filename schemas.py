from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Схема для создания задачи (то, что присылает клиент)
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

# Схема для обновления задачи
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_done: Optional[bool] = None

# Схема для ответа (то, что отдаём клиенту)
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    is_done: bool
    created_at: datetime

    class Config:
        from_attributes = True