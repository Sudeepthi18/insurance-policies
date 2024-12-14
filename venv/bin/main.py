from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}


@app.get("/sample/{name}")
def greet(name: str):
    return {"message": f"Hello {name}! from Teja"}