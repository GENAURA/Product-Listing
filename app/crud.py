from sqlalchemy import and_, or_, desc
from app.models import Product


def get_products(db, category=None, cursor_updated_at=None, cursor_id=None, limit=20):
    query = db.query(Product)

    if category:
        query = query.filter(Product.category == category)

    if cursor_updated_at and cursor_id:
        query = query.filter(
            or_(
                Product.updated_at < cursor_updated_at,
                and_(
                    Product.updated_at == cursor_updated_at,
                    Product.id < cursor_id,
                ),
            )
        )

    products = (
        query.order_by(
            desc(Product.updated_at),
            desc(Product.id),
        )
        .limit(limit)
        .all()
    )

    return products