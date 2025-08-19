from fastapi import APIRouter, Depends

from database import get_db, AsyncSession

from sqlalchemy.ext.asyncio import AsyncSession

from model.workout import Workout
from schemas.workout_schema import WorkoutCreate, WorkoutUpdate


router = APIRouter(prefix="/nutrition", tags=["Nutrition"])


@router.post("/")
async def create_nutrition(
    workout: WorkoutCreate,
    db: AsyncSession = Depends(get_db),
):
    return {"msg": "Nutrition created"}


@router.get("/{id}")
async def get_nutrition(
    id: int,
    db: AsyncSession = Depends(get_db),
):
    return {"msg": "Nutrition fetched"}


@router.put("/{id}")
async def update_nutrition(
    id: int,
    workout: WorkoutUpdate,
    db: AsyncSession = Depends(get_db),
):
    return {"msg": "Nutrition updated"}


@router.delete("/{id}")
async def update_nutrition(
    id: int,
    db: AsyncSession = Depends(get_db),
):
    return {"msg": "Nutrition deleted"}
