from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from daemon.database.models import Node


async def get_node(session: AsyncSession, node_id: int) -> Node:
    result = await session.execute(select(Node).where(Node.nodes_id == node_id))
    user = result.scalar_one_or_none()

    return user

async def update_node(session: AsyncSession, node_id: int, **kwargs: dict) -> bool:
    await session.execute(
        update(Node).where(Node.nodes_id == node_id).values(**kwargs)
    )
    await session.commit()