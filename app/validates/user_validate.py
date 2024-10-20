from pydantic import field_validator

from app.schemas.user_schema import UserSchema
from app.validates.valid_values import (
    VALID_GENDERS,
    VALID_NEEDS_HOSTELS,
    VALID_ENTRANCE_EXAM_FORM,
    VALID_EDUCATIONS
)


class UserValidate(UserSchema):
    @field_validator('gender')
    def validate_gender(self, value) -> str:
        if value not in VALID_GENDERS:
            raise ValueError(f"Gender must be {VALID_GENDERS}")
        return value

    @field_validator('needs_hostel')
    def validate_needs_hostel(self, value) -> str:
        if value not in VALID_NEEDS_HOSTELS:
            raise ValueError(f"Needs hostel must be in {VALID_NEEDS_HOSTELS}")
        return value

    @field_validator('entrance_exam_form')
    def validate_entrance_exam_form(self, value) -> str:
        if value not in VALID_ENTRANCE_EXAM_FORM:
            raise ValueError(f"Entrance exam form must be in {VALID_ENTRANCE_EXAM_FORM}")
        return value

    @field_validator('education')
    def validate_education(self, value) -> str:
        if value not in VALID_EDUCATIONS:
            raise ValueError(f"Education must be in {VALID_EDUCATIONS}")
        return value