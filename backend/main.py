from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import Annotated
from datetime import datetime

from database import engine, Base, get_db
from models import ProductionRecord
from schemas import ProductionRecordResponse


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get(
    "/production-records",
    response_model=list[ProductionRecordResponse]
)
def get_production_records(
    db: Annotated[Session, Depends(get_db)]
):
    records = db.query(ProductionRecord).all()

    return records

@app.post("/seed")
def seed_database(
    db: Annotated[Session, Depends(get_db)]
):
    records = [
        ProductionRecord(
            timestamp=datetime(2026, 9, 3, 10, 30, 0),
            serial_number="SN10001",
            model_name="Model-X100",
            model_id="MDL-001",
            created_by="admin",
            updated_by="admin"
        ),

        ProductionRecord(
            timestamp=datetime(2026, 9, 3, 11, 15, 0),
            serial_number="SN10002",
            model_name="Model-X200",
            model_id="MDL-002",
            created_by="admin",
            updated_by="admin"
        ),

        ProductionRecord(
            timestamp=datetime(2026, 9, 3, 12, 45, 0),
            serial_number="SN10003",
            model_name="Model-X100",
            model_id="MDL-001",
            created_by="john",
            updated_by="john"
        )
    ]

    db.add_all(records)
    db.commit()

    return {
        "message": "Dummy records created"
    }