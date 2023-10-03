from sqlalchemy import Column, String, Text
from app.database.base import Base

class Webpage(Base):
    __tablename__ = 'webpages'
    address = Column(String(255), primary_key=True)
    header = Column(Text, nullable=True)
    body = Column(Text, nullable=True)
    footer = Column(Text, nullable=True)