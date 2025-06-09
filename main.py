from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from backend import models, schemas, crud
from backend.database import engine, get_db, SessionLocal, Base
from backend.routers import items  # 今は未使用

# テーブル作成
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS設定（Next.jsからのアクセスを許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 商品一覧取得
@app.get("/items", response_model=list[schemas.Product])
def get_items(db: Session = Depends(get_db)):
    return db.query(models.ProductMaster).all()

# 商品コードで1件取得
@app.get("/items/{code}", response_model=schemas.Product)
def get_item_by_code(code: str, db: Session = Depends(get_db)):
    product = crud.get_product_by_code(db, code)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# 購入処理
@app.post("/purchase")
def create_purchase(tr: schemas.TransactionCreate, db: Session = Depends(get_db)):
    try:
        result = crud.create_transaction(db, tr)
        return {"message": "Purchase saved", "trd_id": result.trd_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during purchase: {str(e)}")

