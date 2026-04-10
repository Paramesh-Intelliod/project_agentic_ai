from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib

app = FastAPI()

class LoginRequest(BaseModel):
    username: str
    password: str

users = {
    "admin": hashlib.sha256("password123".encode()).hexdigest()
}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.post("/login")
def login(data: LoginRequest):
    if data.username in users and users[data.username] == hash_password(data.password):
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
