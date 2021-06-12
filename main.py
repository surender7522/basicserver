from fastapi import FastAPI
import requests
import json
app = FastAPI()


def authorize():
    js = {
        "auth": {
            "identity": {
                "methods": ["password"],
                "password": {
                    "user": {
                        "name": "admin",
                        "domain": {"id": "default"},
                        "password": "secret",
                    }
                },
            }
        }
    }
    r=requests.post("http:///identity/v3/auth/tokens", json=json.dumps(js))
    print(r.status_code)
    print(r.headers)
    print(type(r.headers))


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/{uid}")
async def root(uid: str):
    return {"message": uid}
authorize()