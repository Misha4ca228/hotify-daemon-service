from sqlalchemy import Column, String, Text, BigInteger, JSON
from daemon.database.models.base import Base
from enum import Enum

class TasksStatus(Enum):
    WAIT_IMAGE = "WAIT_IMAGE"
    WAIT_SEND = "WAIT_SEND"
    DONE = "DONE"



class Task(Base):
    __tablename__ = 'tasks'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    status = Column(String, nullable=False, default=TasksStatus.WAIT_SEND.value)
    user_id = Column(BigInteger, nullable=False)
    text_response = Column(String, nullable=False, default="")
    image = Column(Text, nullable=True, default=None)
    image_args = Column(JSON, nullable=True, default=None)



