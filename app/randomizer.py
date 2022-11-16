from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class Login(BaseModel):
    username: str
    password: str

app = FastAPI()
origins = [""]
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=[""], allow_headers=["*"])

@app.get("/")
def root():
    return {"message": "endpoint 1"}

@app.get("/")
def endpoint1():
    return {"message": "endpoint 2"}

@app.post("/test")
def postLogin(credentials: Login):
    return credentials