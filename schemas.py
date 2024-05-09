from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# schemas for CRUD operations

class Task_Create(BaseModel):
    date: datetime
    title: str = Field(min_length=3, max_length=75)
    task: str = Field(min_length=3, max_length=200)

class Task_Delite(BaseModel):
    id: int

class Task_Read(BaseModel):
    id: int

    class Congig:
        orm_mode = True

class Task_Update(BaseModel):
    id: int
    title: Optional[str] = Field(None, min_length=3, max_length=75)
    task: Optional[str] =  Field(None, min_length=3, max_length=200)