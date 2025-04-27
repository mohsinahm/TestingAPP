from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")

def read_root():
    return "This is Test for ForwardETL"