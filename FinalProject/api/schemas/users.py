from __future__ import annotations
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail




class UserBase(BaseModel):
    customer_name: str
    Address: Optional[str] = None
    pastOrders: str
    email: Optional[str] = None
    phone_number : Optional[int] = None


class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    customer_name: Optional[str] = None
    Address: Optional[str] = None
    pastOrders: Optional[str] = None
    email: Optional[str] = None
    phone_number : Optional[int] = None
class User(UserBase):
    id: int
    order_details: Optional[list[OrderDetail]] = None

    class ConfigDict:
        from_attributes = True


User.model_rebuild()
