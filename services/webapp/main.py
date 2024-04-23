from fastapi import FastAPI
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
    client.run('/service/files/face-3.jpg', "insert")
    client.run('/service/files/task-video.mp4', "search")