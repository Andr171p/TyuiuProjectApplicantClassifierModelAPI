from app.schemas.user_schema import UserSchema

from app.user import User

from process_user_service.input_data import InputData


async def process_user(user: UserSchema) -> ...:
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
    input_data = InputData(user=_user)
    input_data.add_data()
    data = input_data.input_data()