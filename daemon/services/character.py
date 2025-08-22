from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from daemon.database.models.character import Character


async def get_all_character_ids(db: AsyncSession) -> list[int]:
    result = await db.execute(select(Character.id))
    return [row[0] for row in result.all()]


async def get_character_by_id(db: AsyncSession, character_id: int) -> Character | None:
    result = await db.execute(select(Character).where(Character.id == character_id))
    return result.scalar_one_or_none()


