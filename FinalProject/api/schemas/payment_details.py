from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .users import User


class PaymentDetailBase(BaseModel):
    Card_number: int
    Transaction_status: str
    Payment_type: str



class PaymentDetailCreate(PaymentDetailBase):
    User_id: int
    Order_id: int
class PaymentDetailUpdate(BaseModel):
    User_id: Optional[int] = None
    Card_number: Optional[int] = None
    Transaction_status: Optional[str] = None
    Payment_type: Optional[str] = None
    order_id: Optional[int] = None


class PaymentDetail(PaymentDetailBase):
    User_id: int
    user: Optional[User] = None

    class ConfigDict:
        from_attributes = True


PaymentDetail.model_rebuild()
