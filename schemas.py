#file with Pydantic models
from typing import List, Union

from pydantic import BaseModel

class ItemBase(BaseModel):
    item_name: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    item_id: int

    class Config:
        orm_mode = True


class CustomerBase(BaseModel):
    full_name: str


class CustomerCreate(CustomerBase):
    pass #password: str


class Customer(CustomerBase):
    customer_id: int
    full_name: str

    class Config:
        orm_mode = True


class DetailsBase(BaseModel):
    customer_id: int
    item_id: int
    purchase_date: str
    price: float


class DetailsCreate(DetailsBase):
    pass


class Details(DetailsBase):
    detail_id: int

    class Config:
        orm_mode = True