from typing import List, Union

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
import database

from datetime import datetime


database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

#---------------------------------------------------------------
@app.get("/")
def read_root():
    return {"Hello": "World"}
#------------------------------------------------------------------
# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/customers/", response_model=schemas.Customer)
def create_customer(user: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_user = crud.get_full_name(db, user.full_name)
    if db_user:
        raise HTTPException(status_code=400, detail="Customer name already registered")
    return crud.create_customers(db=db, customer=user)


@app.get("/customers/", response_model=List[schemas.Customer])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_customers(db, skip=skip, limit=limit)
    return users


@app.get("/customers/{customer_id}", response_model=schemas.Customer)
def read_user(customer_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_customer(db, customer_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_user


@app.put("/customers/{customer_id}")
async def update_customer(customer_id: int, item: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_user = crud.get_customer(db, customer_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db_user = crud.update_customer(db, customer_id, item)
    return db_user


@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    return crud.delete_customer(db, customer_id)



@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)

@app.get("/details/", response_model=List[schemas.Details])
def read_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    details = crud.get_details(db, skip=skip, limit=limit)
    return details

def details_orm_to_schema(details: models.Details) -> schemas.Details:
    return schemas.Details(
        detail_id=details.detail_id,
        customer_id=details.customer_id,
        item_id=details.item_id,
        purchase_date=str(details.purchase_date),
        price=details.price
    )

@app.post("/details/", response_model=schemas.Details)
def create_item(detail: schemas.DetailsCreate, db: Session = Depends(get_db)):
    return details_orm_to_schema(crud.create_detail(db, detail))
