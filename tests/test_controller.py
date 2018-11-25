import unittest
from service.check_input import *
from service.edit_action import EditAction
from service.controller import *

class TestStudentController(unittest.TestCase):
    def setUp(self):
        self.list_of_students = ListOfStudents([Student(1, "A", 1),
                                                Student(2, "B", 2),
                                                Student(3, "C", 3),
                                                Student(6, "Derp", 2)])

        self.list_of_assignments = ListOfAssignments([Assignment(1, "A", "1/1/2018"),
                                                  Assignment(2, "B", "2/2/2022"),
                                                  Assignment(3, "C", "3/3/2019"),
                                                  Assignment(7, "Derp", "2/2/2022")])

        self.list_of_grades = ListOfGrades([Grade(1, 1), Grade(2, 3, 10),
                                        Grade(7, 2, 2)])

        self.input_checker = InputChecker(self.list_of_students, self.list_of_assignments,
                                          self.list_of_grades)

        self.edit_action = EditAction()

        self.student_controller = StudentController(self.list_of_students, self.input_checker,
                                                    self.edit_action)

    def test_list_students_with_grades(self):
        self.assertEqual(self.student_controller.list_students_with_grades(self.list_of_grades),
                         "id = 1\nname = A\ngroup = 1\nan assignment = 1, ungraded\n\n" +
                         "id = 2\nname = B\ngroup = 2\nan assignment = 7, grade = 2\n\n" +
                         "id = 3\nname = C\ngroup = 3\nan assignment = 2, grade = 10\n\n" +
                         "id = 6\nname = Derp\ngroup = 2\n\n")

    def test_add_student(self):
        self.assertRaises(InputError, self.student_controller.add_student, 1, "depr", 911)
        self.student_controller.add_student(100, "Test", 911)
        self.assertEqual(self.student_controller.get_list_of_students(),
                         ListOfStudents([Student(1, "A", 1),
                                         Student(2, "B", 2),
                                         Student(3, "C", 3),
                                         Student(6, "Derp", 2),
                                         Student(100, "Test", 911)]))

    def test_remove_student(self):
        self.assertRaises(InputError, self.student_controller.remove_student, 100, self.list_of_grades)
        self.student_controller.remove_student(1, self.list_of_grades)
        self.assertEqual(self.student_controller.get_list_of_students(),
                         ListOfStudents([Student(2, "B", 2),
                                         Student(3, "C", 3),
                                         Student(6, "Derp", 2)]))
        self.assertEqual(self.list_of_grades,
                         ListOfGrades([Grade(2, 3, 10), Grade(7, 2, 2)]))

    def test_update_student_name(self):
        self.assertRaises(InputError, self.student_controller.update_student_name, 100, "derp")
        self.student_controller.update_student_name(1, "911")
        self.assertEqual(self.student_controller.get_list_of_students(),
                         ListOfStudents([Student(1, "derp", 1),
                                        Student(2, "B", 2),
                                        Student(3, "C", 3),
                                        Student(6, "Derp", 2)]))

    def test_update_student_group(self):
        self.assertRaises(InputError, self.student_controller.update_student_group, 100, "911")
        self.student_controller.update_student_group(1, 911)
        self.assertEqual(self.student_controller.get_list_of_students(),
                         ListOfStudents([Student(1, "A", 911),
                                         Student(2, "B", 2),
                                         Student(3, "C", 3),
                                         Student(6, "Derp", 2)]))

class TestAssignmentController(unittest.TestCase):
    def setUp(self):
        self.list_of_students = ListOfStudents([Student(1, "A", 1),
                                                Student(2, "B", 2),
                                                Student(3, "C", 3),
                                                Student(6, "Derp", 2)])

        self.list_of_assignments = ListOfAssignments([Assignment(1, "A", "1/1/2018"),
                                                      Assignment(2, "B", "2/2/2022"),
                                                      Assignment(3, "C", "3/3/2019"),
                                                      Assignment(7, "Derp", "2/2/2022")])

        self.list_of_grades = ListOfGrades([Grade(1, 1), Grade(2, 3, 10),
                                            Grade(7, 2, 2)])

        self.input_checker = InputChecker(self.list_of_students, self.list_of_assignments,
                                          self.list_of_grades)

        self.edit_action = EditAction()

        self.assignment_controller = AssignmentController(self.list_of_assignments,
                                                          self.input_checker, self.edit_action)

    def test_list_assignments(self):
        self.assertEqual(self.assignment_controller.list_assignments(),
                         "id = 1\ndescription = A\ndeadline = 1/1/2018\n\n" +
                         "id = 2\ndescription = B\ndeadline = 2/2/2022\n\n" +
                         "id = 3\ndescription = C\ndeadline = 3/3/2019\n\n" +
                         "id = 7\ndescription = Derp\ndeadline = 2/2/2022\n\n")

    def test_add_assignment(self):
        self.assertRaises(InputError, self.assignment_controller.add_assignment, 1, "waa", "9/11/2018")
        self.assertRaises(InputError, self.assignment_controller.add_assignment, 9, "waa", "323/11/2018")
        self.assignment_controller.add_assignment(100, "Test", "9/11/2018")
        self.assertEqual(self.assignment_controller.get_list_of_assignments(),
                         ListOfAssignments([Assignment(1, "A", "1/1/2018"),
                                            Assignment(2, "B", "2/2/2022"),
                                            Assignment(3, "C", "3/3/2019"),
                                            Assignment(7, "Derp", "2/2/2022"),
                                            Assignment(100, "Test", "9/11/2018")]))

    def test_remove_assignment(self):
        self.assertRaises(InputError, self.assignment_controller.remove_assignment, 100, self.list_of_grades)
        self.assignment_controller.remove_assignment(7, self.list_of_grades)
        self.assertEqual(self.assignment_controller.get_list_of_assignments(),
                         ListOfAssignments([Assignment(1, "A", "1/1/2018"),
                                            Assignment(2, "B", "2/2/2022"),
                                            Assignment(3, "C", "3/3/2019")]))
        self.assertEqual(self.list_of_grades, ListOfGrades([Grade(1, 1), Grade(2, 3, 10)]))

    def test_update_assignment_description(self):
        self.assertRaises(InputError, self.assignment_controller.update_assignment_description,
                          100, "desc")
        self.assignment_controller.update_assignment_description(1, "test")
        self.assertEqual(self.assignment_controller.get_list_of_assignments(),
                        ListOfAssignments([Assignment(1, "test", "1/1/2018"),
                                            Assignment(2, "B", "2/2/2022"),
                                            Assignment(3, "C", "3/3/2019"),
                                            Assignment(7, "Derp", "2/2/2022")]))

    def test_update_assignment_deadline(self):
        self.assertRaises(InputError, self.assignment_controller.update_assignment_deadline,
                          100, "9/11/2018")
        self.assertRaises(InputError, self.assignment_controller.update_assignment_deadline,
                          1, "9/13/2018")
        self.assignment_controller.update_assignment_deadline(1, "9/1/2018")
        self.assertEqual(self.assignment_controller.get_list_of_assignments(),
                         ListOfAssignments([Assignment(1, "test", "9/1/2018"),
                                            Assignment(2, "B", "2/2/2022"),
                                            Assignment(3, "C", "3/3/2019"),
                                            Assignment(7, "Derp", "2/2/2022")]))

class TestGradeController(unittest.TestCase):
    def setUp(self):
        self.list_of_students = ListOfStudents([Student(1, "A", 1),
                                                Student(2, "B", 2),
                                                Student(3, "C", 3),
                                                Student(6, "Derp", 2)])

        self.list_of_assignments = ListOfAssignments([Assignment(1, "A", "1/1/2018"),
                                                      Assignment(2, "B", "2/2/2022"),
                                                      Assignment(3, "C", "3/3/2019"),
                                                      Assignment(7, "Derp", "2/2/2022")])

        self.list_of_grades = ListOfGrades([Grade(1, 1), Grade(2, 3, 10),
                                            Grade(7, 2, 2)])

        self.input_checker = InputChecker(self.list_of_students, self.list_of_assignments,
                                          self.list_of_grades)

        self.edit_action = EditAction()

        self.grade_controller = GradeController(self.list_of_grades, self.input_checker, self.edit_action)

    def test_list_grades(self):
        self.assertEqual(self.grade_controller.list_grades(),
                         "assignment_id = 1\nstudent_id = 1\ngrade = None\n\n" +
                         "assignment_id = 2\nstudent_id = 3\ngrade = 10\n\n" +
                         "assignment_id = 7\nstudent_id = 2\ngrade = 2\n\n" )

    def test_assign_students_assignment(self):
        self.assertRaises(InputError, self.grade_controller.assign_students_assignment,
                          100, 1, [1, 2, 3])
        self.assertRaises(InputError, self.grade_controller.assign_students_assignment,
                          1, 2, [2, 10])
        self.assertRaises(InputError, self.grade_controller.assign_students_assignment,
                          1, 2, [1, 2])
        self.grade_controller.assign_students_assignment(1, 2, [2, 3])
        self.assertEqual(self.grade_controller.get_list_of_grades(),
                         ListOfGrades([Grade(1, 1), Grade(2, 3, 10),
                                       Grade(7, 2, 2), Grade(1, 2), Grade(1, 3)]))

    def test_grade_student_assignment(self):
        self.assertRaises(InputError, self.grade_controller.grade_student_assignment,
                          100, 1, 10)
        self.assertRaises(InputError, self.grade_controller.grade_student_assignment,
                          1, 2, 10)
        self.assertRaises(InputError, self.grade_controller.grade_student_assignment,
                          2, 3, 8)
        self.assertRaises(InputError, self.grade_controller.grade_student_assignment,
                          1, 1, 11)
        self.grade_controller.grade_student_assignment(1, 1, 5)
        self.assertEqual(self.grade_controller.get_list_of_grades(),
                         ListOfGrades([Grade(1, 1, 5), Grade(2, 3, 10), Grade(7, 2, 2)]))

class TestEditActionController(unittest.TestCase):
    def setUp(self):
        self.list_of_students = ListOfStudents([Student(1, "A", 1),
                                                Student(2, "B", 2),
                                                Student(3, "C", 3),
                                                Student(6, "Derp", 2)])

        self.list_of_assignments = ListOfAssignments([Assignment(1, "A", "1/1/2018"),
                                                      Assignment(2, "B", "2/2/2022"),
                                                      Assignment(3, "C", "3/3/2019"),
                                                      Assignment(7, "Derp", "2/2/2022")])

        self.list_of_grades = ListOfGrades([Grade(1, 1), Grade(2, 3, 10),
                                            Grade(7, 2, 2)])

        self.input_checker = InputChecker(self.list_of_students, self.list_of_assignments,
                                          self.list_of_grades)

        self.edit_action = EditAction()

        self.edit_action_controller = EditActionController(self.edit_action)
        self.grade_controller = GradeController(self.list_of_grades, self.input_checker, self.edit_action)
        self.student_controller = StudentController(self.list_of_students, self.input_checker,
                                                    self.edit_action)
        self.assignment_controller = AssignmentController(self.list_of_assignments,
                                                          self.input_checker, self.edit_action)

    def test_undo(self):
        self.assertRaises(InputError, self.edit_action_controller.undo)
        self.student_controller.add_student(100, "Test", 911)
        self.edit_action_controller.undo()
        self.assertEqual(self.student_controller.get_list_of_students(),
                         ListOfStudents([Student(1, "A", 1),
                                                Student(2, "B", 2),
                                                Student(3, "C", 3),
                                                Student(6, "Derp", 2)]))

    def test_redo(self):
        self.assertRaises(InputError, self.edit_action_controller.redo)
        self.student_controller.add_student(100, "Test", 911)
        self.edit_action_controller.undo()
        self.edit_action_controller.redo()
        self.assertEqual(self.student_controller.get_list_of_students(),
                         ListOfStudents([Student(1, "A", 1),
                                         Student(2, "B", 2),
                                         Student(3, "C", 3),
                                         Student(6, "Derp", 2),
                                         Student(100, "Test", 911)]))


