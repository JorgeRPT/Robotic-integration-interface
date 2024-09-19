from fastapi import FastAPI

from server.routes.object import router as ObjectRouter

app = FastAPI()

app.include_router(ObjectRouter, tags=["Object"], prefix="/object")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
