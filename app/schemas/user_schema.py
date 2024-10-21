from pydantic import BaseModel

from typing import List


class UserSchema(BaseModel):
    gender: str
    needs_hostel: str
    average_rate: float
    priority: int
    total_exam_points: int
    total_bonus_points: int
    education: str
    form_of_education: str
    type_of_reception: str
    speciality: str


class UsersSchema(BaseModel):
    users: List[UserSchema]
