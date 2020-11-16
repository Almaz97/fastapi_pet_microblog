from core.database import Base
from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
# from user.models import User


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(350))
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("user.User")
