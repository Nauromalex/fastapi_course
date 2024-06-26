from fastapi import APIRouter, Depends
from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@router.post("")
async def add_task(task: STaskAdd = Depends()) -> STaskId:
    new_task_id = await TaskRepository.add_task(task)
    return {"id": new_task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_tasks()
    return tasks
