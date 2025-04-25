from typing import Annotated

from fastapi import APIRouter, Depends

from schemas import STaskAdd
from repository import TaskRepository

router = APIRouter(
    prefix='/tasks'
)

@router.post('')
async def add_task(
    task: Annotated[STaskAdd, Depends()]
):
    tasks.append(task)
    return {'ok': True}

@router.get('')
def get_tasks():
    task = Task(name='Write this video')
    return {'data': task}