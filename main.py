from typing import Annotated

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from utils.database import Base, engine
from utils.dependencies import get_db

from models.production import ProductionRecord
from schemas.production import ProductionRecordResponse


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Production Records API",
    version="1.0.0",
)


@app.get(
    "/production-records",
    response_model=list[ProductionRecordResponse],
)
def get_production_records(
    db: Annotated[Session, Depends(get_db)],
):
    return db.query(ProductionRecord).all()
