from app.user import User
from app.schemas.user_schema import UserSchema
from app.validates.user_validate import UserValidate

from service.input import InputData
from service.preprocessing.encode import EncodeInputData
from service.preprocessing.standard import StandardInputData

from ml.model import BinaryClassifierModel

import numpy as np

from typing import Any


async def validate_user(user: UserSchema) -> UserSchema:
    validated_user = UserValidate()


async def add_user(user: UserSchema) -> User:
    _user = User(
        gender=user.gender,
        needs_hostel=user.needs_hostel,
        average_rate=user.average_rate,
        priority=user.priority,
        total_exam_points=user.total_exam_points,
        total_bonus_points=user.total_bonus_points,
        education=user.education,
        form_of_education=user.form_of_education,
        type_of_reception=user.type_of_reception,
        speciality=user.speciality
    )
    return _user


async def preprocessing_user(user: User) -> np.array:
    input_user_data = InputData(user=user).data()
    encode_input_data = EncodeInputData(data=input_user_data)
    encoded_user_data = encode_input_data.binary_encoding()
    standard_input_data = StandardInputData(data=encoded_user_data)
    normalize_user_data = standard_input_data.normalize()
    return normalize_user_data