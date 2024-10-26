from pydantic import BaseModel, field_validator

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


class UserValidate(UserSchema):
    @field_validator('gender')
    def validate_gender(self, v):
        if v not in ['М', 'Ж']:
            raise ValueError('Gender must be either "М" or "Ж"')
        return v

    @field_validator('exam_points')
    def validate_exam_points(self, v):
        if v < 0 or v > 300:
            raise ValueError('Exam points must be between 0 and 300')
        return v