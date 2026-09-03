from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from utils.database import Base


class ProductionRecord(Base):
    __tablename__ = "production_records"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    serial_number: Mapped[str] = mapped_column(
        String,
        nullable=False,
        index=True,
    )

    model_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    model_id: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    created_by: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    created_on: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_by: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    updated_on: Mapped[datetime | None] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=True,
    )
