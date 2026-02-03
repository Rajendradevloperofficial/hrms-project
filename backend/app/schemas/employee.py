from pydantic import BaseModel, EmailStr

class EmployeeCreate(BaseModel):
    employee_id: str
    full_name: str
    email: EmailStr
    department: str
