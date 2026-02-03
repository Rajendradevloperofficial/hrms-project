from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database import Base

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    date = Column(Date)
    status = Column(String)
