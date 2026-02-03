from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate

router = APIRouter(prefix="/employees", tags=["Employees"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_employee(data: EmployeeCreate, db: Session = Depends(get_db)):
    if db.query(Employee).filter(Employee.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")
    emp = Employee(**data.dict())
    db.add(emp)
    db.commit()
    return emp

@router.get("/")
def list_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

@router.delete("/{id}")
def delete_employee(id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).get(id)
    if not emp:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(emp)
    db.commit()
    return {"message": "Deleted"}
