from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
import random

router = APIRouter()

# In-memory OTP storage (Temporary for development)
otp_storage = {}

@router.post("/send-otp/")
def send_otp(phone_number: str, db: Session = Depends(get_db)):
    otp = random.randint(1000, 9999)
    otp_storage[phone_number] = otp
    return {"message": f"OTP sent to {phone_number}", "otp": otp}

@router.post("/verify-otp/")
def verify_otp(phone_number: str, otp: int, db: Session = Depends(get_db)):
    if otp_storage.get(phone_number) == otp:
        return {"message": "OTP Verified"}
    raise HTTPException(status_code=400, detail="Invalid OTP")

