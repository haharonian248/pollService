from fastapi import FastAPI
from controller.poll_controller import router as poll_router
from repository.database import database

app = FastAPI()
app.include_router(poll_router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()