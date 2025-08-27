from sqlalchemy import Column, Integer, JSON, BigInteger, String
from sqlalchemy.ext.mutable import MutableList

from daemon.database.models.base import Base

class Dialog(Base):
    __tablename__ = 'dialogs'

    user_id = Column(BigInteger, primary_key=True)
    character_id = Column(String, nullable=False)
    dialog = Column(MutableList.as_mutable(JSON), nullable=False, default=list)

