from pydantic import BaseModel
from datetime import datetime


class ProductionRecordResponse(BaseModel):
    id: int
    timestamp: datetime
    serial_number: str
    model_name: str
    model_id: str
    created_by: str
    created_on: datetime
    updated_by: str | None
    updated_on: datetime | None

    class Config:
        from_attributes = True