from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from utils.dependencies import get_db
from models.production import ProductionRecord
from schemas.production import ProductionRecordResponse


router = APIRouter(
    prefix="/production-records",
    tags=["Production Records"],
)


@router.get(
    "/",
    response_model=list[ProductionRecordResponse],
)
def get_production_records(
    db: Annotated[Session, Depends(get_db)],
):
    return db.query(ProductionRecord).all()
