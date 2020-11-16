from sqlalchemy import Column, String, Integer, DateTime, Boolean
from core.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(50), unique=True)
    email = Column(String(255), unique=True)
    password = Column(String(50), unique=True)
    date = Column(DateTime)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
