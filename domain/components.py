from datetime import datetime
from copy import deepcopy

class Student:
    def __init__(self, id_, name, group):
        self._id_ = id_
        self._name = name
        self._group = group

    def get_id(self):
        return self._id_

    def set_id(self, student_id):
        self._id_ = student_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_group(self):
        return self._group

    def set_group(self, group):
        self._group = group

    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        return self._id_ == other.get_id()

    def __str__(self):
        student_to_string = "id = {}\nname = {}\ngroup = {}\n".format(self._id_, self._name, self._group)
        return student_to_string

    def __lt__(self, other):
        if type(self) != type(other):
            raise TypeError
        return int(self._id_) < int(other.get_id())

class Assignment:
    def __init__(self, id_, description, deadline):
        self._id_ = id_
        self._description = description
        self._deadline = deadline
        self._average_grade = 0

    def get_id(self):
        return self._id_

    def set_id(self, id_):
        self._id_ = id_

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_deadline(self):
        deadline = deepcopy(str(self._deadline))  # make this secure no mather what
        deadline = datetime.strptime(deadline, "%d/%m/%Y")
        return deadline  # return it in datetime form

    def set_deadline(self, deadline):
        self._deadline = deadline

    def get_average_grade(self):
        return self._average_grade

    def set_average_grade(self, average_grade):
        self._average_grade = average_grade

    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        return self._id_ == other.get_id()

    def __str__(self):
        return "id = {}\ndescription = {}\ndeadline = {}\n".format(self._id_, self._description, self._deadline)

    def __lt__(self, other):
        if type(self) != type(other):
            raise TypeError
        return int(self._id_) < int(other.get_id())

class GradeError(Exception):
    pass

class Grade:
    def __init__(self, assignment_id, student_id, grade=None):
        self._assignment_id = assignment_id
        self._student_id = student_id
        self._grade = grade
        self._id_ = (assignment_id, student_id)

    def get_assignment_id(self):
        return self._assignment_id

    def get_student_id(self):
        return self._student_id

    def get_grade(self):
        if self._grade is None:
            return
        return int(self._grade)

    def set_grade(self, grade):
        if self._grade is not None and grade is not None:
            raise GradeError
        self._grade = grade

    def get_id(self):
        return self._id_

    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        return self.get_id() == other.get_id()

    def __str__(self):
        return "assignment_id = {}\nstudent_id = {}\ngrade = {}\n".format(
            self._assignment_id, self._student_id, self._grade)

    def __lt__(self, other):
        return self._id_ < other.get_id()
