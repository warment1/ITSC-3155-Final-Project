from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class OrderBase(BaseModel):
    customer_id: int
    description: Optional[str] = None
    order_date: Optional[datetime] = None
    togo: Optional[str] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    description: Optional[str] = None


class Order(OrderBase):
    id: int

    class ConfigDict:
        from_attributes = True
