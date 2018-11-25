from ui.ui import MenuUI
from service.controller import *
from service.check_input import InputChecker
from service.edit_action import EditAction

class AppStart:
    @staticmethod
    def app_start():
        list_of_students = ListOfStudents(ListOfStudents.default_list())
        list_of_assignments = ListOfAssignments(ListOfAssignments.default_list())
        list_of_grades = ListOfGrades(ListOfGrades.default_list(list_of_assignments, list_of_students))
        edit_action = EditAction()

        input_checker = InputChecker(list_of_students, list_of_assignments, list_of_grades)

        student_controller = StudentController(list_of_students, input_checker, edit_action)
        assignment_controller = AssignmentController(list_of_assignments, input_checker, edit_action)
        grade_controller = GradeController(list_of_grades, input_checker, edit_action)
        edit_action_controller = EditActionController(edit_action)

        menu_ui = MenuUI(student_controller, assignment_controller, grade_controller, edit_action_controller)
        menu_ui.main()

AppStart.app_start()


