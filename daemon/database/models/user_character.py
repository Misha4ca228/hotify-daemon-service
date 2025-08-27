from sqlalchemy import Column, BigInteger, String

from daemon.database.models import Base


class UserCharacter(Base):
    __tablename__ = "user_characters"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    name = Column(String, nullable=False)
    prompt = Column(String, nullable=False)
    scene = Column(String, nullable=True)
    face_url = Column(String, nullable=True)

