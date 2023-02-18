from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship

import database


class Customer(database.Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=False)
    full_name = Column(String, unique=False, index=False)



class Item(database.Base):
    __tablename__ = "items"

    item_id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, index=True)

class Details(database.Base):
    __tablename__ = "details"

    detail_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    item_id = Column(Integer, ForeignKey("items.item_id"))
    purchase_date = Column(Date, unique=False, index=False)
    price = Column(Float, unique=False, index=False)
    
    items = relationship("Item")
    customers = relationship("Customer")
