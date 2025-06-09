from pydantic import BaseModel

class ProductSchema(BaseModel):
    code: str
    name: str
    price: float

    class Config:
        orm_mode = True
