import unittest
from service.lab_lists import *
from copy import deepcopy

class TestListOfStudents(unittest.TestCase):
    _stud_list = ListOfStudents([Student(1, "A", 1),
                                 Student(2, "B", 2),
                                 Student(3, "C", 3),
                                 Student(6, "Derp", 2)])

    _assignment_list = ListOfAssignments([Assignment(1, "A", "1/1/2018"),
                                          Assignment(2, "B", "2/2/2022"),
                                          Assignment(3, "C", "3/3/2019"),
                                          Assignment(7, "Derp", "2/2/2022")])

    def test_update_name(self):
        stud_list = deepcopy(self._stud_list)
        stud_list.update_name(1, "a")
        self.assertEqual(stud_list.get_by_id(1).get_name(), "a")
        stud_list.update_name(6, "derp")
        self.assertEqual(stud_list.get_by_id(6).get_name(), "derp")
        self.assertEqual(stud_list, ListOfStudents([Student(1, "a", 1),
                                                    Student(2, "B", 2),
                                                    Student(3, "C", 3),
                                                    Student(6, "derp", 2)]))

    def test_update_group(self):
        stud_list = deepcopy(self._stud_list)
        stud_list.update_group(1, 10)
        self.assertEqual(stud_list.get_by_id(1).get_group(), 10)
        stud_list.update_group(6, 20)
        self.assertEqual(stud_list.get_by_id(6).get_group(), 20)
        self.assertEqual(stud_list, ListOfStudents([Student(1, "A", 10),
                                                    Student(2, "B", 2),
                                                    Student(3, "C", 3),
                                                    Student(6, "Derp", 20)]))


class TestListOfAssignments(unittest.TestCase):
    _stud_list = ListOfStudents([Student(1, "A", 1),
                                 Student(2, "B", 2),
                                 Student(3, "C", 3),
                                 Student(6, "Derp", 2)])

    _assignment_list = ListOfAssignments([Assignment(1, "A", "1/1/2018"),
                                          Assignment(2, "B", "2/2/2022"),
                                          Assignment(3, "C", "3/3/2019"),
                                          Assignment(7, "Derp", "2/2/2022")])

    def test_update_deadline(self):
        assignment_list = deepcopy(self._assignment_list)
        assignment_list.update_deadline(1, "2/2/2018")
        self.assertEqual(str(assignment_list.get_by_id(1).get_deadline()), "2018-02-02 00:00:00")
        assignment_list.update_deadline(7, "2/3/2018")
        self.assertEqual(str(assignment_list.get_by_id(7).get_deadline()), "2018-03-02 00:00:00")
        self.assertEqual(assignment_list, ListOfAssignments([Assignment(1, "A", "2/2/2018"),
                                                             Assignment(2, "B", "2/2/2022"),
                                                             Assignment(3, "C", "3/3/2019"),
                                                             Assignment(7, "Derp", "2/3/2018")]))

    def test_update_description(self):
        assignment_list = deepcopy(self._assignment_list)
        assignment_list.update_description(1, "Kms")
        self.assertEqual(assignment_list.get_by_id(1).get_description(), "Kms")
        assignment_list.update_description(7, "Kms")
        self.assertEqual(assignment_list.get_by_id(7).get_description(), "Kms")
        self.assertEqual(assignment_list, ListOfAssignments([Assignment(1, "Kms", "1/1/2018"),
                                                             Assignment(2, "B", "2/2/2022"),
                                                             Assignment(3, "C", "3/3/2019"),
                                                             Assignment(7, "Kms", "2/2/2022")]))

