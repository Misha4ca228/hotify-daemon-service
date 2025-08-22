from sqlalchemy import Column, Integer, DateTime, Boolean, String, BigInteger
from sqlalchemy.ext.mutable import MutableList

from sqlalchemy.types import JSON
from daemon.database.models.base import Base


class User(Base):
    __tablename__ = 'users'

    user_id = Column(BigInteger, primary_key=True)
    referral_id = Column(BigInteger, nullable=True, default=None)
    energy = Column(Integer, nullable=False, default=100)
    infinite_energy = Column(Boolean, nullable=False, default=False)
    diamond = Column(Integer, nullable=False, default=0)
    character_id = Column(MutableList.as_mutable(JSON), nullable=False, default=list)
    vip = Column(DateTime, nullable=True)
    language_code = Column(String, nullable=False)
