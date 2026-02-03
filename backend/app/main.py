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
        "https://your-frontend.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_host = ["*"],
)

app.include_router(employees.router)
app.include_router(attendance.router)
