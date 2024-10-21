from pydantic import field_validator

from app.schemas.user_schema import UserSchema
from app.validates.valid_values import (
    VALID_GENDERS,
    VALID_NEEDS_HOSTELS,
    VALID_ENTRANCE_EXAM_FORM,
    VALID_EDUCATIONS
)


class UserValidate(UserSchema):
    @field_validator("gender")
    def validate_gender(self, value):
        if value not in VALID_GENDERS:
            raise ValueError(f"Gender must be {VALID_GENDERS}")
        return value

    @field_validator("needs_hostel")
    def validate_needs_hostel(self, value):
        if value not in VALID_NEEDS_HOSTELS:
            raise ValueError(f"Needs hostel must be in {VALID_NEEDS_HOSTELS}")
        return value

    @field_validator("average_rate")
    def validate_average_rate(self, value):
        if not (1 <= value <= 5):
            raise ValueError(f"Average rate must be in range(1, 5)")
        return value

    @field_validator("priority")
    def validate_priority(self, value):
        if value not in range(2, 6):
            raise ValueError("Priority must be in range(1, 5)")
        return value

    @field_validator("total_exam_points")
    def validate_total_exam_points(self, value):
        if value not in range(0, 310):
            raise ValueError("Total exam points must be in range(0, 300)")
        return value

    @field_validator("total_bonus_points")
    def validate_total_bonus_points(self, value):
        if value not in range(0, 11):
            raise ValueError("Total bonus points must be in range(0, 10)")
        return value

    @field_validator('education')
    def validate_education(self, value):
        if value not in VALID_EDUCATIONS:
            raise ValueError(f"Education must be in {VALID_EDUCATIONS}")
        return value