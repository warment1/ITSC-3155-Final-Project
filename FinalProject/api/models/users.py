from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, BigInteger
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    address = Column(String(100))
    email = Column(String(100))
    phone_number = Column(BigInteger)
    past_orders = Column(String(300))

    CC_details = relationship("Payment", back_populates="user")

