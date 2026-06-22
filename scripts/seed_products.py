from random import choice, uniform
from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Product

CATEGORIES = [
    "Electronics",
    "Books",
    "Clothing",
    "Home",
    "Sports",
    "Beauty",
    "Toys",
    "Grocery",
]

TOTAL_PRODUCTS = 200_000
BATCH_SIZE = 5000


def seed():
    db: Session = SessionLocal()

    try:
        batch = []

        for i in range(1, TOTAL_PRODUCTS + 1):
            created = datetime.utcnow() - timedelta(days=i % 365)

            batch.append(
                Product(
                    name=f"Product {i}",
                    category=choice(CATEGORIES),
                    price=round(uniform(10, 5000), 2),
                    created_at=created,
                    updated_at=created,
                )
            )

            if len(batch) == BATCH_SIZE:
                db.bulk_save_objects(batch)
                db.commit()
                print(f"Inserted {i} products")
                batch.clear()

        if batch:
            db.bulk_save_objects(batch)
            db.commit()

        print("✅ Finished inserting 200,000 products!")

    finally:
        db.close()


if __name__ == "__main__":
    seed()