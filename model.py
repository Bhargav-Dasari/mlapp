from sqlalchemy import Column, Integer, String
from database import Base


class row(Base):
    __tablename__ = 'image_urls'
    id = Column(Integer, primary_key=True, autoincrement = True)
    url = Column(String(250), nullable = False, unique=True)
    prediction = Column(Integer)