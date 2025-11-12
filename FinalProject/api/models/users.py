from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    Address = Column(String(100))
    email = Column(String(100))
    phone_number = Column(Integer)
    pastOrders = Column(String(300))

    CC_details = relationship("CardDetail", back_populates="user")
