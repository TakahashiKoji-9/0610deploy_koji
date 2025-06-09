from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# -----------------------------
# 商品マスタテーブル
# -----------------------------

class ProductMaster(Base):
    __tablename__ = "product_master"

    prd_id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, index=True, nullable=False)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)

    # 取引明細とのリレーション（逆参照）
    details = relationship("TransactionDetail", back_populates="product")


# -----------------------------
# 取引テーブル
# -----------------------------

class Transaction(Base):
    __tablename__ = "transaction"

    trd_id = Column(Integer, primary_key=True, index=True)
    emp_cd = Column(String(20), nullable=False)
    store_cd = Column(String(20), nullable=False)
    pos_no = Column(String(20), nullable=False)
    total_amt = Column(Integer, nullable=False)

    # 取引明細とのリレーション
    details = relationship("TransactionDetail", back_populates="transaction")


# -----------------------------
# 取引明細テーブル
# -----------------------------

class TransactionDetail(Base):
    __tablename__ = "transaction_detail"

    trd_id = Column(Integer, ForeignKey("transaction.trd_id"), primary_key=True)
    dtl_id = Column(Integer, primary_key=True)
    prd_id = Column(Integer, ForeignKey("product_master.prd_id"))

    prd_code = Column(String(20), nullable=False)
    prd_name = Column(String(100), nullable=False)
    prd_price = Column(Integer, nullable=False)

    # リレーション設定
    transaction = relationship("Transaction", back_populates="details")
    product = relationship("ProductMaster", back_populates="details")
