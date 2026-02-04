from dotenv import load_dotenv
load_dotenv()   
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import employees, attendance

app = FastAPI(title="HRMS Lite")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
      
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
   
)

app.include_router(employees.router)
app.include_router(attendance.router)
