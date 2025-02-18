from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Booking
from app.database import get_db

router = APIRouter()

@router.post("/book-ticket/")
def book_ticket(user_id: int, ticket_type: str, amount: float, db: Session = Depends(get_db)):
    booking = Booking(user_id=user_id, ticket_type=ticket_type, amount=amount)
    db.add(booking)
    db.commit()
    return {"message": "Booking Confirmed", "booking_id": booking.id}

