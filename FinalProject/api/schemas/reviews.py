from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .orders import Order


class ReviewBase(BaseModel):
    rating: int
    comment: Optional[str] = None


class ReviewCreate(ReviewBase):
    order_id: int


class ReviewUpdate(BaseModel):
    order_id: Optional[int] = None
    rating: Optional[int] = None
    comment: Optional[str] = None


class Review(ReviewBase):
    id: int
    order_id: int
    review_date: Optional[datetime] = None
    order: Order = None

    class ConfigDict:
        from_attributes = True