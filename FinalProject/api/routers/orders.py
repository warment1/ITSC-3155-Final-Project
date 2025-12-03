from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy import DATETIME
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas import orders as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)


@router.post("/", response_model=schema.Order)
def create(request: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Order])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)
@router.get("/{user_id}", response_model=list[schema.Order])
def read_all_from_user(user_id: str, db: Session = Depends(get_db)):
    return controller.read_all_from_user(db, user_id=user_id)
@router.get("/{order_date}", response_model=int)
def sales_per_diem(order_date: str, db: Session = Depends(get_db)):
    return controller.sales_per_diem(db, order_date=order_date)

@router.get("/{item_id}", response_model=schema.Order)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.Order)
def update(item_id: int, request: schema.OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
