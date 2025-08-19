from fastapi import APIRouter, Depends

from database import get_db, AsyncSession

from sqlalchemy.ext.asyncio import AsyncSession

from model.workout import Workout
from schemas.workout_schema import WorkoutCreate, WorkoutUpdate


router = APIRouter(prefix="/exercise", tags=["Exercise"])


@router.post("/")
async def create_exercise(
    workout: WorkoutCreate,
    db: AsyncSession = Depends(get_db),
):
    return {"msg": "Exercise created"}


@router.get("/{id}")
async def get_exercise(
    id: int,
    db: AsyncSession = Depends(get_db),
):
    return {"msg": "Exercise fetched"}


@router.put("/{id}")
async def update_exercise(
    id: int,
    workout: WorkoutUpdate,
    db: AsyncSession = Depends(get_db),
):
    return {"msg": "Exercise updated"}


@router.delete("/{id}")
async def update_exercise(
    id: int,
    db: AsyncSession = Depends(get_db),
):
    return {"msg": "Exercise deleted"}
