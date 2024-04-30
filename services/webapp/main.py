from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from client import client


class Detect(BaseModel):
    source: str
    action: str | None = None


app = FastAPI()


@app.post("/detection/")
async def detection(detect: Detect):
    client.run(detect.source, detect.action)


@app.get("/quickstart/")
async def create_item():
    for i in client.run('/service/files/face-3.jpg', "insert"):
        pass

    return StreamingResponse(client.run('/service/files/task-video.mp4', "search"), media_type="text/html")
