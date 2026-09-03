from datetime import datetime, timezone

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from utils.database import Base


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class ProductionRecord(Base):
    __tablename__ = "production_records"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
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
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )

    updated_by: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    updated_on: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        onupdate=utc_now,
        nullable=True,
    )
