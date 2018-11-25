import unittest
from service.check_input import InputChecker
from service.lab_lists import *

class TestInputChecker(unittest.TestCase):
    _list_of_students = ListOfStudents([Student(1, "A", 1),
                                        Student(2, "B", 2),
                                        Student(3, "C", 3),
                                        Student(6, "Derp", 2)])

    _list_of_assignments = ListOfAssignments([Assignment(1, "A", "1/1/2018"),
                                              Assignment(2, "B", "2/2/2022"),
                                              Assignment(3, "C", "3/3/2019"),
                                              Assignment(7, "Derp", "2/2/2022")])

    _input_checker = InputChecker(_list_of_students, _list_of_assignments, [])

    def test_is_unsigned_int(self):
        self.assertTrue(self._input_checker._is_unsigned_int(10))
        self.assertTrue(self._input_checker._is_unsigned_int(777))
        self.assertTrue(self._input_checker._is_unsigned_int("100"))
        self.assertTrue(self._input_checker._is_unsigned_int(1110))
        self.assertFalse(self._input_checker._is_unsigned_int(-1110))
        self.assertFalse(self._input_checker._is_unsigned_int(0))
        self.assertFalse(self._input_checker._is_unsigned_int("0"))
        self.assertFalse(self._input_checker._is_unsigned_int("-1110"))
        self.assertFalse(self._input_checker._is_unsigned_int("KMS"))

    def test_check_student_id_not_in(self):
        self.assertTrue(self._input_checker.check_student_id_not_in(4))
        self.assertTrue(self._input_checker.check_student_id_not_in(9))
        self.assertTrue(self._input_checker.check_student_id_not_in(777))
        self.assertFalse(self._input_checker.check_student_id_not_in(1))
        self.assertFalse(self._input_checker.check_student_id_not_in(6))

    def test_check_student_id_in(self):
        self.assertFalse(self._input_checker.check_student_id_in(4))
        self.assertFalse(self._input_checker.check_student_id_in(9))
        self.assertFalse(self._input_checker.check_student_id_in(777))
        self.assertTrue(self._input_checker.check_student_id_in(1))
        self.assertTrue(self._input_checker.check_student_id_in(6))

    def test_check_assignment_id_not_in(self):
        self.assertTrue(self._input_checker.check_assignment_id_not_in(4))
        self.assertTrue(self._input_checker.check_assignment_id_not_in(9))
        self.assertTrue(self._input_checker.check_assignment_id_not_in(777))
        self.assertFalse(self._input_checker.check_assignment_id_not_in(1))
        self.assertFalse(self._input_checker.check_assignment_id_not_in(7))

    def test_check_assignment_id_in(self):
        self.assertFalse(self._input_checker.check_assignment_id_in(4))
        self.assertFalse(self._input_checker.check_assignment_id_in(9))
        self.assertFalse(self._input_checker.check_assignment_id_in(777))
        self.assertTrue(self._input_checker.check_assignment_id_in(1))
        self.assertTrue(self._input_checker.check_assignment_id_in(7))

    def test_check_group(self):
        self.assertTrue(self._input_checker.check_group("911"))
        self.assertTrue(self._input_checker.check_group(911))
        self.assertTrue(self._input_checker.check_group(1))
        self.assertFalse(self._input_checker.check_group("-1"))
        self.assertFalse(self._input_checker.check_group(-1))
        self.assertFalse(self._input_checker.check_group("KMS"))

