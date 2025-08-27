
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from daemon.database.models import Character
from daemon.database.models.user_character import UserCharacter


async def create_user_character(session: AsyncSession, **kwargs):
    new_task = UserCharacter(**kwargs)
    session.add(new_task)
    await session.commit()

    return new_task


async def update_user_character(session: AsyncSession, user_character_id: int, **kwargs: dict) -> bool:
    await session.execute(
        update(UserCharacter).where(UserCharacter.id == user_character_id).values(**kwargs)
    )
    await session.commit()


async def get_user_character(session: AsyncSession, user_character_id: int) -> UserCharacter | None:
    result = await session.execute(
        select(UserCharacter).where(UserCharacter.id == user_character_id)
    )
    task = result.scalar_one_or_none()
    return task
