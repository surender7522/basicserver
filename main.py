import json
import os

import requests
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()
url = os.getenv("url", "")


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
    r = requests.post(
        "http://{0}/identity/v3/auth/tokens".format(url), data=json.dumps(js)
    )
    print(r.status_code)
    print(r.headers)
    print(type(r.headers))
    return r.headers.get("X-Subject-Token", "")


def write_notification(uid: str):
    token = authorize()
    x = {
        "events": [
            {
                "name": "network-changed",
                "server_uuid": uid,
                "tag": uid,
                "status": "completed",
            }
        ]
    }
    headers = {"X-Auth-Token": token}
    r = requests.post(
        "http://{0}/compute/v2.1/os-server-external-events".format(url),
        data=json.dumps(x),
        headers=headers,
    )
    # r = requests.get("http://{0}/compute/v2.1/servers".format(url), headers=headers)
    print(r.status_code)
    print(r.json())


@app.get("/{uid}")
async def root(uid: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, uid=uid)
    return {"message": "token", "uid": uid}


@app.post("/{uid}")
async def root(uid: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, uid=uid)

    return {"message": "token", "uid": uid}
