from sqlalchemy import Column, String, Text, JSON
from app.database.base import Base

class Webpage(Base):
    __tablename__ = 'webpages'
    address = Column(String(255), primary_key=True)
    head = Column(Text, nullable=True)
    body = Column(JSON, nullable=True)
    foot = Column(Text, nullable=True)