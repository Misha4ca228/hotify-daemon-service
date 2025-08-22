from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from daemon.database.models import Dialog

async def get_dialog_by_user_id(session: AsyncSession, user_id: int) -> Dialog | None:
    result = await session.execute(
        select(Dialog).where(Dialog.user_id == user_id)
    )
    return result.scalar_one_or_none()


async def dialog_exists(session: AsyncSession, user_id: int) -> bool:
    result = await session.execute(
        select(Dialog.user_id).where(Dialog.user_id == user_id)
    )
    return result.scalar_one_or_none() is not None


async def get_dialog_json(session: AsyncSession, user_id: int) -> list[dict] | None:
    result = await session.execute(
        select(Dialog.dialog).where(Dialog.user_id == user_id)
    )
    return result.scalar_one_or_none()


async def append_to_dialog_json(session: AsyncSession, user_id: int, role: str, content: str):
    result = await session.execute(
        select(Dialog).where(Dialog.user_id == user_id)
    )
    dialog_entry = result.scalar_one_or_none()

    if dialog_entry is None:
        return

    dialog_entry.dialog.append({
        "role": role,
        "content": content
    })

    session.add(dialog_entry)
    await session.commit()



async def create_dialog(session: AsyncSession, user_id: int, character_id: int, dialog_data: list = None):
    if dialog_data is None:
        dialog_data = []

    result = await session.execute(
        select(Dialog).where(Dialog.user_id == user_id, Dialog.character_id == character_id)
    )
    existing_dialog = result.scalar_one_or_none()

    if existing_dialog is None:
        new_dialog = Dialog(
            user_id=user_id,
            character_id=character_id,
            dialog=dialog_data
        )
        session.add(new_dialog)
        await session.commit()
        return new_dialog
    else:
        return existing_dialog


async def delete_dialog(session: AsyncSession, user_id: int) -> bool:

    stmt = delete(Dialog).where(Dialog.user_id == user_id)
    result = await session.execute(stmt)
    await session.commit()

    return result.rowcount > 0