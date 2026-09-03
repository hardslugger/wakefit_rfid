from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database import Base


class ProductionRecord(Base):
    __tablename__ = "production_records"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, nullable=False)
    serial_number = Column(String, nullable=False, index=True)
    model_name = Column(String, nullable=False)
    model_id = Column(String, nullable=False)   # VARCHAR
    created_by = Column(String, nullable=False)
    created_on = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_by = Column(String, nullable=True)
    updated_on = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )