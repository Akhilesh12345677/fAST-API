from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import sqlite3

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def show_students(request: Request):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    conn.close()

    return templates.TemplateResponse("students.html", {
        "request": request,
        "students": data
    })