from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/{uid}")
async def root(uid: str):
    return {"message": uid}