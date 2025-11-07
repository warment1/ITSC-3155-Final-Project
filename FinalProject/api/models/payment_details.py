from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Card_number = Column(Integer)
    Transaction_status = Column(String(100))
    Payment_type = Column(String(100))
    User_id = Column(Integer, ForeignKey("users.id"))
