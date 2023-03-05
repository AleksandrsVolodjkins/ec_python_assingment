from sqlalchemy.orm import Session

import models, schemas

from datetime import datetime


def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.customer_id == customer_id).first()


def get_full_name(db: Session, full_name: str):
    return db.query(models.Customer).filter(models.Customer.full_name == full_name).first()


def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).order_by("full_name").offset(skip).limit(limit).all()


def create_customers(db: Session, customer: schemas.CustomerCreate):
    db_user = models.Customer(full_name=customer.full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).order_by("item_id").offset(skip).limit(limit).all()


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(item_name=item.item_name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_customer(db: Session, customer_id: int,  customer: schemas.CustomerCreate):
    db_update = db.query(models.Customer).filter(models.Customer.customer_id == customer_id).first()
    db_update.full_name = customer.full_name
    db.commit()
    db.refresh(db_update)
    return db_update


def delete_customer(db: Session, customer_id: int):
    db_customer = db.query(models.Customer).filter(models.Customer.customer_id == customer_id).first()
    if db_customer:
        db.delete(db_customer)
        db.commit()
        return {"message": f"Customer with ID {customer_id} deleted successfully."}
    else:
        return {"error": f"Customer with ID {customer_id} not found."}


def get_details(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Details).order_by("purchase_date").offset(skip).limit(limit).all()

def create_detail(db: Session, detail: schemas.DetailsCreate):
    db_item = models.Details(customer_id=detail.customer_id, item_id=detail.item_id, price=detail.price, purchase_date=detail.purchase_date)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item