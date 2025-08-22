from datetime import datetime, timedelta

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from daemon.database.models import User


async def user_exists(session: AsyncSession, user_id: int) -> bool:
    query = select(User).where(User.user_id == user_id)
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    return user is not None


async def add_user(session: AsyncSession, **kwargs):
    new_user = User(**kwargs)
    session.add(new_user)
    await session.commit()

    return new_user


async def get_user(session: AsyncSession, user_id: int) -> User:
    result = await session.execute(select(User).where(User.user_id == user_id))
    user = result.scalar_one_or_none()

    return user


async def remove_energy(session, user_id: int, amount: int):
    user = await session.get(User, user_id)
    user.energy -= amount
    await session.commit()


async def remove_diamond(session, user_id: int, amount: int):
    user = await session.get(User, user_id)
    user.diamond -= amount
    await session.commit()


async def add_energy(session, user_id: int, amount: int):
    user = await session.get(User, user_id)
    user.energy += amount
    await session.commit()

async def add_diamond(session, user_id: int, amount: int):
    user = await session.get(User, user_id)
    user.diamond += amount
    await session.commit()


async def set_infinite_energy(session, user_id: int, value: bool):
    user = await session.get(User, user_id)
    user.infinite_energy = value
    await session.commit()


async def set_vip_expiration(session: AsyncSession, user_id: int, duration_days: int):

    expires_at = datetime.utcnow() + timedelta(days=duration_days)

    await session.execute(
        update(User)
        .where(User.user_id == user_id)
        .values(vip=expires_at)
    )
    await session.commit()


async def add_character_to_user(session: AsyncSession, user_id: int, character_id: int):
    result = await session.execute(select(User).where(User.user_id == user_id))
    user = result.scalar_one_or_none()

    if user is None:
        return False

    if character_id not in user.character_id:
        user.character_id.append(character_id)
        await session.commit()
        return True

    return False

async def get_language_code(session: AsyncSession, user_id:  int) -> str:
    query = select(User.language_code).filter_by(user_id=int(user_id))

    result = await session.execute(query)

    language_code = result.scalar_one_or_none()

    return language_code or ""


async def set_language_code(
        session: AsyncSession,
        user_id: int,
        language_code: str,
) -> None:
    stmt = update(User).where(User.user_id == int(user_id)).values(language_code=language_code)

    await session.execute(stmt)
    await session.commit()
