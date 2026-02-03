HRMS Lite is a lightweight Human Resource Management System built using FastAPI for the backend and React for the frontend.
This project is designed for learning, demos, and small-scale applications, covering core HR functionalities such as employee management and attendance tracking.

 Features

Employee Management (Create, View, Update, Delete)

Attendance Management

RESTful APIs using FastAPI

Database integration with SQLAlchemy

Alembic for database migrations

Ready for cloud deployment (Render)

Clean and modular project structure

🛠 Tech Stack
Backend

Python

FastAPI

SQLAlchemy

Alembic

PostgreSQL 

Gunicorn

Frontend

React

Axios

Modern CSS

📂 Project Structure
hrms-lite/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models/
│   │   ├── routers/
│   │   └── schemas/
│   │
│   ├── alembic/
│   ├── alembic.ini
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│   ├── src/
│   └── package.json
│
└── README.md
