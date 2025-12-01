from __future__ import annotations
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail




class UserBase(BaseModel):
    customer_name: str
    address: Optional[str] = None
    past_orders: str
    email: Optional[str] = None
    phone_number : Optional[int] = None


class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    customer_name: Optional[str] = None
    address: Optional[str] = None
    past_orders: Optional[str] = None
    email: Optional[str] = None
    phone_number : Optional[int] = None
class User(UserBase):
    id: int
    order_details: Optional[list[OrderDetail]] = None

    class ConfigDict:
        from_attributes = True


User.model_rebuild()
