from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, BigInteger
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Payment(Base):
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Card_number = Column(BigInteger)
    Transaction_status = Column(String(100))
    Payment_type = Column(String(100))
    User_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="CC_details")
