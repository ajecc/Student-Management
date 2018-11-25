import unittest
from repository.repository import Repository
from domain.components import *
from copy import deepcopy

class TestRepository(unittest.TestCase):
    _stud_list = Repository([Student(1, "A", 1),
                                 Student(2, "B", 2),
                                 Student(3, "C", 3),
                                 Student(6, "Derp", 2)])

    _assignment_list = Repository([Assignment(1, "A", "1/1/2018"),
                                          Assignment(2, "B", "2/2/2022"),
                                          Assignment(3, "C", "3/3/2019"),
                                          Assignment(7, "Derp", "2/2/2022")])

    def test_add(self):
        stud_list = deepcopy(self._stud_list)
        assignment_list = deepcopy(self._assignment_list)

        stud_list.add(Student(7, "Seven", 7))
        self.assertEqual(stud_list, Repository([Student(1, "A", 1),
                                                    Student(2, "B", 2),
                                                    Student(3, "C", 3),
                                                    Student(6, "Derp", 2),
                                                    Student(7, "Seven", 7)]))
        assignment_list.add(Assignment(8, "Eight", "8/8/8888"))
        self.assertEqual(assignment_list, Repository([Assignment(1, "A", "1/1/2018"),
                                                             Assignment(2, "B", "2/2/2022"),
                                                             Assignment(3, "C", "3/3/2019"),
                                                             Assignment(7, "Derp", "2/2/2022"),
                                                             Assignment(8, "Eight", "8/8/8888")]))

    def test_remove(self):
        stud_list = deepcopy(self._stud_list)
        assignment_list = deepcopy(self._assignment_list)

        stud_list.remove(Student(6, "Derp", 2))
        self.assertEqual(stud_list, Repository([Student(1, "A", 1),
                                                    Student(2, "B", 2),
                                                    Student(3, "C", 3)]))
        assignment_list.remove(Assignment(7, "Derp", "2/2/2022"))
        self.assertEqual(assignment_list, Repository([Assignment(1, "A", "1/1/2018"),
                                                             Assignment(2, "B", "2/2/2022"),
                                                             Assignment(3, "C", "3/3/2019")]))

    def test_in_list(self):
        self.assertTrue(self._stud_list.in_list(1))
        self.assertTrue(self._stud_list.in_list(6))
        self.assertFalse(self._stud_list.in_list(100))
        self.assertTrue(self._assignment_list.in_list(1))
        self.assertTrue(self._assignment_list.in_list(7))
        self.assertFalse(self._assignment_list.in_list(100))

    def test_get_by_id(self):
        self.assertEqual(self._stud_list.get_by_id(1), Student(1, "A", 1))
        self.assertEqual(self._stud_list.get_by_id(6), Student(6, "Derp", 2))
        self.assertEqual(self._stud_list.get_by_id(100), None)
        self.assertEqual(self._assignment_list.get_by_id(1), Assignment(1, "A", "1/1/2018"))
        self.assertEqual(self._assignment_list.get_by_id(7), Assignment(7, "Derp", "2/2/2022"))
        self.assertEqual(self._assignment_list.get_by_id(100), None)


