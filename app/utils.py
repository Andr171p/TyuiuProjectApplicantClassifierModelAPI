from app.schemas.user_schema import UserSchema

from client.user import User


def create_user(user: UserSchema) -> User:
    user = User(
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
    return user

'''
user = User(
    gender="М",
    needs_hostel="да",
    average_rate=5.0,
    priority=1,
    total_exam_points=210,
    total_bonus_points=10,
    education="Среднее общее образование",
    form_of_education="Очная",
    type_of_reception="Общий конкурс",
    speciality="20.03.01 Техносферная безопасность"
)
from client.process import UserProcessing
from ml.model import BinaryClassifierModel
model = BinaryClassifierModel()
# user = create_user(user=user)
user_processing = UserProcessing(user=user)
processed_user = user_processing.process_user()
prediction = model.predict(x=processed_user)
print(prediction)'''