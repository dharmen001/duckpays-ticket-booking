from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    otp_verified = Column(Boolean, default=False)

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    ticket_type = Column(String)  # Flight or Bus
    amount = Column(Float)
    status = Column(String, default="Pending")  # Pending, Confirmed, Cancelled

