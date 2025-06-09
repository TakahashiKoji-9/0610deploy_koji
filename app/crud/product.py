from sqlalchemy.orm import Session
from app.models.product import Product

def get_product_by_code(db: Session, code: str):
    return db.query(Product).filter(Product.code == code).first()
