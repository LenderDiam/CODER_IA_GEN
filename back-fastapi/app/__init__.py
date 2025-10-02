from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.count_table import Base, CountTable
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/postgres")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

with SessionLocal() as session:
    session.query(CountTable).delete()
    session.add(CountTable(count_number=0))
    session.commit()