from sqlalchemy import Column, Integer, String
from app.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    employee_id = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    department = Column(String, nullable=False)
