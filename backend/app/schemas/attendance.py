from pydantic import BaseModel
from datetime import date

class AttendanceCreate(BaseModel):
    employee_id: int
    date: date
    status: str
