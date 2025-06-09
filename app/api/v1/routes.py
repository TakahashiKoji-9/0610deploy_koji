from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.product import ProductSchema
from app.crud.product import get_product_by_code
from backend.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/products/{code}", response_model=ProductSchema)
def read_product(code: str, db: Session = Depends(get_db)):
    db_product = get_product_by_code(db, code)
    if not db_product:
        raise HTTPException(status_code=404, detail="商品が見つかりません")
    return db_product
