from datetime import datetime

from fastapi import FastAPI, Depends, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import distinct
from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
from app.models import Product
from app.crud import get_products

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="CodeVector Product Browser",
    version="1.0.0",
    description="FastAPI + Supabase Product Browser",
)

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Home API
@app.get("/")
def root():
    return {"message": "🚀 CodeVector Backend is Running!"}


# UI Page
@app.get("/ui", response_class=HTMLResponse)
def ui(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


# Health Check
@app.get("/health")
def health():
    return {"status": "healthy"}


# Categories API
@app.get("/categories")
def get_categories(db: Session = Depends(get_db)):
    rows = (
        db.query(distinct(Product.category))
        .order_by(Product.category)
        .all()
    )

    return {
        "categories": [row[0] for row in rows]
    }


# Products API
@app.get("/products")
def list_products(
    category: str | None = None,
    cursor_updated_at: datetime | None = None,
    cursor_id: int | None = None,
    limit: int = Query(default=20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    products = get_products(
        db=db,
        category=category,
        cursor_updated_at=cursor_updated_at,
        cursor_id=cursor_id,
        limit=limit,
    )

    next_cursor = None

    if products:
        last = products[-1]
        next_cursor = {
            "cursor_updated_at": last.updated_at.isoformat(),
            "cursor_id": last.id,
        }

    return {
        "success": True,
        "count": len(products),
        "items": products,
        "next_cursor": next_cursor,
    }