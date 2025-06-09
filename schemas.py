from pydantic import BaseModel
from typing import List

# --------------------------
# 商品情報（Product）
# --------------------------

class Product(BaseModel):
    prd_id: int
    code: str
    name: str
    price: int

    class Config:
        from_attributes = True


# --------------------------
# 商品作成用（未使用なら削除可）
# --------------------------

class ItemCreate(BaseModel):
    code: str
    name: str
    price: int


# --------------------------
# トランザクション明細
# --------------------------

class TransactionDetailCreate(BaseModel):
    prd_id: int
    prd_code: str
    prd_name: str
    prd_price: int


# --------------------------
# トランザクション全体
# --------------------------

class TransactionCreate(BaseModel):
    emp_cd: str
    store_cd: str
    pos_no: str
    total_amt: int
    details: List[TransactionDetailCreate]


# --------------------------
# レスポンス例（必要に応じて使用）
# --------------------------

class ItemResponse(BaseModel):
    message: str
    item: Product

    class Config:
        from_attributes = True
