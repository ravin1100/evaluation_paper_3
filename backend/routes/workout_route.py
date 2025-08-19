from fastapi import APIRouter, Depends

from database import get_db, AsyncSession

from sqlalchemy.ext.asyncio import AsyncSession

from model.workout import Workout
from schemas.workout_schema import WorkoutCreate, WorkoutUpdate


router = APIRouter(prefix="/workouts", tags=["Workout"])


@router.post("/")
async def create_workout(
    workout: WorkoutCreate,
    db: AsyncSession = Depends(get_db),
):
    # wo = Workout(workout.model_dump())
    # await db.commit(wo)
    # wo_sync = await db.refresh()
    # return {**wo}
    return {"msg": "Workout created"}


@router.get("/{id}")
async def get_workout(
    id: int,
    db: AsyncSession = Depends(get_db),
):
    return {"msg": "Workout fetched"}


@router.put("/{id}")
async def update_workout(
    id: int,
    workout: WorkoutUpdate,
    db: AsyncSession = Depends(get_db),
):
    return {"msg": "Workout updated"}


@router.delete("/{id}")
async def update_workout(
    id: int,
    db: AsyncSession = Depends(get_db),
):
    return {"msg": "Workout deleted"}
