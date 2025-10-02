from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CountTable(Base):
    __tablename__ = 'count_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    count_number = Column(Integer, nullable=False)