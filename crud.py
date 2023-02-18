from sqlalchemy.orm import Session

import models, schemas


def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()


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


def create_customer_item(db: Session, item: schemas.ItemCreate, customer_id: int):
    db_item = models.Item(**item.dict(), customer_id=customer_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_details(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Details).order_by("purchase_date").offset(skip).limit(limit).all()