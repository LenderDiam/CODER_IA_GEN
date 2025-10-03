from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from app.models.count_table import Base, CountTable

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/postgres")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def init_database():
    Base.metadata.create_all(bind=engine)
    
    with SessionLocal() as session:
        count_row = session.query(CountTable).first()
        if count_row is None:
            session.add(CountTable(count_number=0))
            session.commit()

init_database()

@app.get("/count")
def get_count():
    with SessionLocal() as session:
        count_row = session.query(CountTable).first()
        if count_row is None:
            session.add(CountTable(count_number=0))
            session.commit()
            return {"count": 0}
        return {"count": count_row.count_number}

@app.post("/count/increment")
def increment_count():
    with SessionLocal() as session:
        count_row = session.query(CountTable).first()
        if count_row is None:
            raise HTTPException(status_code=404, detail="Count not found")
        count_row.count_number += 1
        session.commit()
        return {"count": count_row.count_number}

@app.post("/count/reset")
def reset_count():
    with SessionLocal() as session:
        count_row = session.query(CountTable).first()
        if count_row is None:
            raise HTTPException(status_code=404, detail="Count not found")
        count_row.count_number = 0
        session.commit()
        return {"count": count_row.count_number}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)