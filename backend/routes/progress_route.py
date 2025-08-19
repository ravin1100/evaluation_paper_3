from fastapi import APIRouter, Depends

from database import get_db, AsyncSession

from sqlalchemy.ext.asyncio import AsyncSession

from model.workout import Workout
from schemas.workout_schema import WorkoutCreate, WorkoutUpdate


router = APIRouter(prefix="/progress", tags=["Progess"])


@router.post("/")
async def create_progress(
    workout: WorkoutCreate,
    db: AsyncSession = Depends(get_db),
):
    return {"msg": "Progress created"}


@router.get("/{id}")
async def get_progress(
    id: int,
    db: AsyncSession = Depends(get_db),
):
    return {"msg": "Progress fetched"}


@router.put("/{id}")
async def update_progress(
    id: int,
    workout: WorkoutUpdate,
    db: AsyncSession = Depends(get_db),
):
    return {"msg": "Progress updated"}


@router.delete("/{id}")
async def update_progress(
    id: int,
    db: AsyncSession = Depends(get_db),
):
    return {"msg": "Progress deleted"}
