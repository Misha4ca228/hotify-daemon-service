from sqlalchemy import Column, Integer, DateTime, Boolean, String, BigInteger, Float
from sqlalchemy.ext.mutable import MutableList

from sqlalchemy.types import JSON
from daemon.database.models.base import Base


class Node(Base):
    __tablename__ = 'nodes'

    nodes_id = Column(BigInteger, primary_key=True)
    nodes_name = Column(String, nullable=False)
    status = Column(Boolean, nullable=False)
    worker_url = Column(String, nullable=False)
    profit = Column(Float, nullable=False, default=0.0)