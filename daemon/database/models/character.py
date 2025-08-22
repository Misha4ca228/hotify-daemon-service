from sqlalchemy import Column, Integer, String, Text
from daemon.database.models.base import Base
from enum import Enum

class CharacterType(Enum):
    FREE = "FREE"
    PAID = "PAID"



class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    name = Column(String, nullable=False)
    prompt = Column(Text, nullable=False)
    photo_link = Column(String, nullable=False)
