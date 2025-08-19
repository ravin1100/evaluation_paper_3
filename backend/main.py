from fastapi import FastAPI, HTTPException
from routes.workout_route import router as workout_router
from database import create_tables


app = FastAPI(description="SmartFit: AI-Powered Fitness Coach")


@app.on_event("startup")
async def on_startup():
    await create_tables()


app.include_router(workout_router)


@app.post("/health")
def health_check():
    return {"success": True}
