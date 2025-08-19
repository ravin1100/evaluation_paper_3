from fastapi import FastAPI, HTTPException
from routes.workout_route import router as workout_router
from routes.exercise_route import router as exercise_router
from routes.nutrition_route import router as nutrition_router
from routes.progress_route import router as progress_router
from routes.exercise_route import router as exercise_router
from database import create_tables


app = FastAPI(description="SmartFit: AI-Powered Fitness Coach")


@app.on_event("startup")
async def on_startup():
    await create_tables()


app.include_router(workout_router)
app.include_router(exercise_router)
app.include_router(nutrition_router)
app.include_router(progress_router)
app.include_router(exercise_router)


@app.post("/health")
def health_check():
    return {"success": True}
