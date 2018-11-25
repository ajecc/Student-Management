import time
from domain.components import *

class InputError(Exception):
    pass

class InputChecker:
    def __init__(self, list_of_students, list_of_assignments, list_of_grades):
        self._list_of_students = list_of_students
        self._list_of_assignments = list_of_assignments
        self._list_of_grades = list_of_grades

    def _to_int(self, foo):
        try:
            foo = int(foo)
        except ValueError:
            return False
        return foo

    def _is_unsigned_int(self, foo):
        try:
            foo = int(foo)
            return foo > 0
        except ValueError:
            return False

    def _check_not_empty(self, to_check):
        return to_check != "" and to_check is not None

    def check_student_id_not_in(self, student_id):
        if not self._check_not_empty(student_id):
            return False
        return not self._list_of_students.in_list(student_id)

    def check_student_id_in(self, student_id):
        if not self._check_not_empty(student_id):
            return False
        return self._list_of_students.in_list(student_id)

    def check_assignment_id_not_in(self, assignment_id):
        if not self._check_not_empty(assignment_id):
            return False
        return not self._list_of_assignments.in_list(assignment_id)

    def check_assignment_id_in(self, assignment_id):
        if not self._check_not_empty(assignment_id):
            return False
        return self._list_of_assignments.in_list(assignment_id)

    def check_grade_id_not_in(self, grade_id):
        return not self._list_of_grades.in_list(grade_id)

    def check_name(self, name):
        if not self._check_not_empty(name):
            return False
        return True

    def check_group(self, group):
        if not self._check_not_empty(group):
            return False
        return self._is_unsigned_int(group)

    def check_deadline(self, deadline):
        """
        :param deadline: a string r
        :return: True if deadline is a string of form DD/MM/YYYY representing a date
        """
        if not self._check_not_empty(deadline):
            return False
        if deadline == "" or deadline is None:
            return False

        try:
            time.strptime(deadline, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def check_description(self, description):
        return self._check_not_empty(description)

    def check_number(self, number):
        if not self._check_not_empty(number):
            return False
        return self._is_unsigned_int(number)

    def check_assignment_id_in_student_ungraded(self, student_id_in,
                                                assignment_id_in_student_ungraded):
        id_ = (assignment_id_in_student_ungraded, student_id_in)
        if not self._list_of_grades.in_list(id_):
            return False
        grade = self._list_of_grades.get_by_id(id_)
        return grade.get_grade() is None

    def check_grade(self, grade):
        return self._is_unsigned_int(grade) and 1 <= int(grade) <= 10

    def check_add_student(self, student_id_not_in, name, group):
        good = True
        good = good and self.check_student_id_not_in(student_id_not_in)
        good = good and self.check_name(name)
        good = good and self.check_group(group)
        return good

    def check_add_assignment(self, assignment_id_not_in, description, deadline):
        good = True
        good = good and self.check_assignment_id_not_in(assignment_id_not_in)
        good = good and self.check_description(description)
        good = good and self.check_deadline(deadline)
        return good

    def check_remove_student(self, student_id_in):
        return self.check_student_id_in(student_id_in)

    def check_remove_assignment(self, assignment_id_in):
        return self.check_assignment_id_in(assignment_id_in)

    def check_update_student_name(self, student_id_in, name):
        good = True
        good = good and self.check_student_id_in(student_id_in)
        good = good and self.check_name(name)
        return good

    def check_update_student_group(self, student_id_in, group):
        good = True
        good = good and self.check_student_id_in(student_id_in)
        good = good and self.check_group(group)
        return good

    def check_update_assignment_description(self, assignment_id_in, description):
        good = True
        good = good and self.check_assignment_id_in(assignment_id_in)
        good = good and self.check_description(description)
        return good

    def check_update_assignment_deadline(self, assignment_id_in, deadline):
        good = True
        good = good and self.check_assignment_id_in(assignment_id_in)
        good = good and self.check_deadline(deadline)
        return good

    def check_assign_students_assignment(self, assignment_id_in, number, student_id_list):
        good = True
        good = good and self.check_assignment_id_in(assignment_id_in)
        good = good and self.check_number(number)
        for student_id_in in student_id_list:
            good = good and self.check_student_id_in(student_id_in)
            good = good and self.check_grade_id_not_in((assignment_id_in, student_id_in))
        return good

    def check_grade_student_assignment(self, student_id_in, assignment_id_in_student_ungraded, grade):
        good = True
        good = good and self.check_student_id_in(student_id_in)
        good = good and self.check_assignment_id_in_student_ungraded(student_id_in, assignment_id_in_student_ungraded)
        good = good and self.check_grade(grade)
        return good

    def check_students_received_assignment_alphabetic_order(self, assignment_id_in):
        return self.check_assignment_id_in(assignment_id_in)

    def check_students_received_assignment_grade_order(self, assignment_id_in):
        return self.check_assignment_id_in(assignment_id_in)


