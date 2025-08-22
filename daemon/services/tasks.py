from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, select

from daemon.database.models.task import Task


async def add_new_task(session: AsyncSession, **kwargs):
    new_task = Task(**kwargs)
    session.add(new_task)
    await session.commit()

    return new_task


async def update_task(session: AsyncSession, task_id: int, **kwargs: dict) -> bool:
    await session.execute(
        update(Task).where(Task.id == task_id).values(**kwargs)
    )
    await session.commit()


async def get_task(session: AsyncSession, task_id: int) -> Task | None:
    result = await session.execute(
        select(Task).where(Task.id == task_id)
    )
    task = result.scalar_one_or_none()
    return task
