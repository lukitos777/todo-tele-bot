from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from datetime import date

from schemas import *
from task_manager import *

router = Router()

@router.message(Command(commands='start'))
async def start_handler(msg: Message):
    await msg.answer(
        'Привет! Я бот который поможет создавать, удалять, обновлять задачи\n'
    )

#=============================================================================

# Creating task
class Add_Task(StatesGroup):
    title = State()
    description = State()

@router.message(Command(commands='add'))
async def add_task_handler(msg: Message, state: FSMContext):
    await state.set_state(Add_Task.title)
    await msg.answer('Ведите заголовок задачи')

@router.message(Add_Task.title)
async def get_task_title(msg: Message, state: FSMContext):
    await state.update_data(title=msg.text)
    await state.set_state(Add_Task.description)
    await msg.answer('Enter description')

@router.message(Add_Task.description)
async def get_task_description(msg: Message, state: FSMContext):
    await state.update_data(description=msg.text)
    task_ = await state.get_data()
    await msg.answer('Task created')
    await state.clear()
    query = Task_Create(
        title=task_['title'],
        task=task_['description'],
        date=date.today()
    )
    create_task(query)

#================================================

# getting list of tasks
@router.message(Command(commands='tsk'))
async def get_tasks_list_handler(msg: Message):
    msg_ = ''
    tasks = await get_all_tasks()
    for task in tasks:
        msg_ += f'{task.title}: \n {task.task}\n'
    await msg.answer(msg_)

#================================================

# read description of the task
class Read_Task(StatesGroup):
    task_id = State()

@router.message(Command(commands='read'))
async def get_task_id(msg: Message, state: FSMContext):
    await state.set_state(Read_Task.task_id)
    await msg.answer('Введите айди задачи')

@router.message(Read_Task.task_id)
async def get_task_description(msg: Message, state: FSMContext):
    await state.update_data(task_id=msg.text)
    task_id = await state.get_data()
    ID = int(task_id['task_id'])
    await state.clear()
    query = Task_Read(id=ID)
    task = await read_task(query)
    if not task:
        await msg.answer('Такой задачи не существует')
    else:
        await msg.answer(f'{ID}\n{task.task}')

#================================================

# delliting task
class Del_Task(StatesGroup):
    task_id = State()

@router.message(Command(commands='read'))
async def get_task_id(msg: Message, state: FSMContext):
    await state.set_state(Del_Task.task_id)
    await msg.answer('Введите айди задачи')

@router.message(Del_Task.task_id)
async def del_task(msg: Message, state: FSMContext):
    await state.update_data(task_id=msg.text)
    task_id = await state.get_data()
    ID = int(task_id['task_id'])
    await state.clear()
    query = Task_Delite(id=ID)
    await del_task(query)
    msg.answer('Задача удаленна')