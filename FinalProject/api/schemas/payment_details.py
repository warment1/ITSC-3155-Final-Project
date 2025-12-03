from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .users import User


class PaymentBase(BaseModel):
    Card_number: int
    Transaction_status: str
    Payment_type: str


class PaymentCreate(PaymentBase):
    User_id: int

class PaymentUpdate(BaseModel):
    User_id: Optional[int] = None
    Card_number: Optional[int] = None
    Transaction_status: Optional[str] = None
    Payment_type: Optional[str] = None


class Payment(PaymentBase):
    User_id: int
    user: Optional[User] = None

    class ConfigDict:
        from_attributes = True


Payment.model_rebuild()
