from typing import TYPE_CHECKING
from uuid import uuid4
import daemon.core.config as cfg
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, AsyncEngine, create_async_engine
from asyncpg import Connection

from sqlalchemy.engine.url import URL



class CConnection(Connection):
    def _get_unique_id(self, prefix: str) -> str:
        return f"__asyncpg_{prefix}_{uuid4()}__"


def get_engine(url: URL | str = cfg.DATABASE_URL) -> AsyncEngine:
    return create_async_engine(
        url=url,
        echo=False,
        pool_size=20,
        max_overflow=10,
        pool_recycle=3600,
        pool_pre_ping=True,
        connect_args={
            "connection_class": CConnection,
            "server_settings": {
                "application_name": "cloud-daemon-automatic",
            },
        },
    )


def get_sessionmaker(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


db_url = cfg.DATABASE_URL
engine = get_engine(url=db_url)
sessionmaker = get_sessionmaker(engine)