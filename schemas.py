#file with Pydantic models
from typing import List, Union

from pydantic import BaseModel

class ItemBase(BaseModel):
    item_name: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
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
    title: str
    description: Union[str, None] = None


class DetailsCreate(DetailsBase):
    pass


class Details(DetailsBase):
    id: int
    detail_id: int

    class Config:
        orm_mode = True