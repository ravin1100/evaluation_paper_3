from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base
from model.exercise import User


class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    plan_name = Column(String)
    date = Column(String)
    duration = Column(Float)

    # user = relationship("User", back_populates="")
    # user_id = Column(Integer, ForeignKey("users.id"))
    # user = relationship(User, primaryjoin=user_id == User.id)

    # Workouts: id, user_id, plan_name, date, exercises, duration
