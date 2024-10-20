

class User:
    def __init__(
            self,
            gender: str,
            needs_hostel: str,
            average_rate: float,
            priority: int,
            total_exam_points: int,
            total_bonus_points: int,
            education: str,
            form_of_education: str,
            type_of_reception: str,
            speciality: str
    ) -> None:
        self.gender = gender
        self.needs_hostel = needs_hostel
        self.average_rate = average_rate
        self.priority = priority
        self.total_exam_points = total_exam_points
        self.total_bonus_points = total_bonus_points
        self.education = education
        self.form_of_education = form_of_education
        self.type_of_reception = type_of_reception
        self.speciality = speciality
