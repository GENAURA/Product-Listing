from sqlalchemy import Column, BigInteger, String, Float, DateTime, Index
from datetime import datetime, UTC

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    category = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)

    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC), nullable=False)

    __table_args__ = (
        Index("idx_updated_id", "updated_at", "id"),
        Index("idx_category_updated_id", "category", "updated_at", "id"),
    )