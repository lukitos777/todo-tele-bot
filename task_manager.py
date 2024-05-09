from datetime import datetime
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import SessionLocal
from models import Task
from schemas import Task_Create, Task_Read, Task_Delite


# Create a new task
async def create_task(task_create: Task_Create):
    async with SessionLocal() as session:
        new_task = Task(
            date=task_create.date,
            title=task_create.title,
            task=task_create.task
        )

        session.add(new_task)
        await session.commit() 
        await session.refresh(new_task)  

    return new_task


# Read a task by ID
async def read_task(task_read: Task_Read):
    async with SessionLocal() as session:
        result = await session.execute(select(Task).where(Task.id == task_read.id)) 
        task = result.scalar_one_or_none() 
    return task


# Delete a task by ID
async def delete_task(task_delite: Task_Delite):
    async with SessionLocal() as session:
        result = await session.execute(select(Task).where(Task.id == task_delite.id))
        task = result.scalar_one_or_none()  

        if task:
            session.delete(task)  
            await session.commit()  

    return task


# Get all tasks from the table
async def get_all_tasks():
    async with SessionLocal() as session:
        result = await session.execute(select(Task)) 
        tasks = result.scalars().all() 
    return tasks
