from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.attendance import Attendance
from app.schemas.attendance import AttendanceCreate

router = APIRouter(prefix="/attendance", tags=["Attendance"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def mark_attendance(data: AttendanceCreate, db: Session = Depends(get_db)):
    record = Attendance(**data.dict())
    db.add(record)
    db.commit()
    return record

@router.get("/{employee_id}")
def get_attendance(employee_id: int, db: Session = Depends(get_db)):
    return db.query(Attendance).filter(
        Attendance.employee_id == employee_id
    ).all()
