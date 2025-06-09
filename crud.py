from sqlalchemy.orm import Session
from . import models, schemas

from sqlalchemy import func

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.ProductMaster(
        code=item.code,
        name=item.name,
        price=item.price
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {
        "message": "Item created successfully",
        "item": db_item
    }

def get_product_by_code(db: Session, code: str):
    return db.query(models.ProductMaster).filter(func.trim(models.ProductMaster.code) == code.strip()).first()


def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    tr = models.Transaction(
        emp_cd=transaction.emp_cd,
        store_cd=transaction.store_cd,
        pos_no=transaction.pos_no,
        total_amt=transaction.total_amt
    )
    db.add(tr)
    db.flush()  # TRD_ID を確定

    for i, d in enumerate(transaction.details):
        detail = models.TransactionDetail(
            trd_id=tr.trd_id,
            dtl_id=i + 1,
            prd_id=d.prd_id,
            prd_code=d.prd_code,
            prd_name=d.prd_name,
            prd_price=d.prd_price
        )
        db.add(detail)

    db.commit()
    db.refresh(tr)
    return tr
