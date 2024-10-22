

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

    def __repr__(self) -> str:
        return (f"User(\n"
                f"\tgender={self.gender!r}\n"
                f"\tneeds_hostel={self.needs_hostel!r}\n"
                f"\taverage_rate={self.average_rate}\n"
                f"\tpriority={self.priority!r}\n"
                f"\ttotal_exam_points={self.total_exam_points!r}\n"
                f"\ttotal_bonus_points={self.total_bonus_points!r}\n"
                f"\teducation={self.education!r}\n"
                f"\tform_of_education={self.form_of_education!r}\n"
                f"\ttype_of_reception={self.type_of_reception!r}\n"
                f"\tspeciality={self.speciality}\n"
                f")")
