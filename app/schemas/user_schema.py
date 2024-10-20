from pydantic import (
    BaseModel,
    field_validator
)


class UserSchema(BaseModel):
    gender: str
    needs_hostel: bool
    average_rate = float
    priority = int
    total_exam_points = int
    total_bonus_points = int
    education = str
    form_of_education = str
    type_of_reception = str
    speciality = str
