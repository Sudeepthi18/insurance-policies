from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}


@app.get("/sample/{name}")
def greet(name: str):
    return {"message": f"Hello {name}! from Teja"}


@app.get("/sample/hello/{greet}")
def hello(greet: str):
    return {"msg" : f"this is the test {greet}"}

@app.get("/mahi")
def fu():
    return {"hreerfyeu"}