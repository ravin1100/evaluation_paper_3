from typing import Optional
from pydantic import BaseModel


class WorkoutCreate(BaseModel):
    user_id: int
    plan_name: str
    date: str
    duration_in_min: float


# Workouts: id, user_id, plan_name, date, exercises, duration
class WorkoutUpdate(BaseModel):
    user_id: Optional[int] = None
    plan_name: Optional[str] = None
    date: Optional[str] = None
    duration_in_min: Optional[float] = None


class WorkoutResponse(BaseModel):
    user_id: int
    plan_name: str
    date: str
    duration_in_min: float
