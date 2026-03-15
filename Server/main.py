from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import database

app = FastAPI(title="Authorization Server")

class LoginRequest(BaseModel):
    username: str
    password: str

# http://127.0.0.1:8000
@app.get("/")
async def read_root():
    return {"message": "Authorization Server Running"}


@app.post("/login")
async def login(request: LoginRequest):
    if request.username in database.users and database.users[request.username] == request.password:
        return {"message": "Login successful", "user": request.username}

    raise HTTPException(status_code=401, detail="Invalid username or password")