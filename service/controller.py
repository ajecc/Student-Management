from service.check_input import InputError
from service.misc import FunctionCascade
from service.lab_lists import *
from datetime import date, datetime


class StudentController:
    def __init__(self, list_of_students, input_checker, edit_action):
        self._list_of_students = list_of_students
        self._input_checker = input_checker
        self._edit_action = edit_action

    def get_list_of_students(self):
        return self._list_of_students

    def list_students_with_grades(self, list_of_grades, list_of_students=None):
        """
        Lists students and their assignments with corresponding grades
        :param list_of_grades: ListOfGrades
        :param list_of_students: ListOfStudents with default value self._list_of_students
        :return: string
        """
        if list_of_students is None:
            list_of_students = self._list_of_students

        list_of_students_to_string = ""
        for student in list_of_students.get_repo():
            list_of_students_to_string += str(student)
            list_of_grades_student = list_of_grades.get_student_grades(student.get_id())
            for grade in list_of_grades_student.get_repo():
                list_of_students_to_string += "an assignment = " + str(grade.get_assignment_id()) + ", "
                if grade.get_grade() is None:
                    list_of_students_to_string += "ungraded\n"
                else:
                    list_of_students_to_string += "grade = " + str(grade.get_grade()) + "\n"
            list_of_students_to_string += "\n"
        return list_of_students_to_string

    def add_student(self, student_id_not_in, name, group):
        """
        Adds student to list
        Also adds the function and its inverse to the undo/redo lists
        Throws an error if the user entered incorrect data
        :param student_id_not_in: string
        :param name: string
        :param group: string
        :return: None, just calls add in a ListOfStudents
        """
        if not self._input_checker.check_add_student(student_id_not_in, name, group):
            raise InputError
        self._edit_action.update_history(self._add_student_cascade(student_id_not_in, name, group),
                                         self._inverse_add_student_cascade(student_id_not_in))
        self._list_of_students.add(Student(student_id_not_in, name, group))

    def _add_student_cascade(self, student_id_not_in, name, group):
        function_cascade = FunctionCascade()
        function_cascade.add_function(self._list_of_students.add, [Student(student_id_not_in, name, group)])
        return function_cascade

    def _inverse_add_student_cascade(self, student_id_not_in):
        function_cascade = FunctionCascade()
        function_cascade.add_function(self._list_of_students.remove_by_id, [student_id_not_in])
        return function_cascade

    def remove_student(self, student_id_in, list_of_grades):
        """
        Removes student from list
        Also adds the function and its inverse to the undo/redo lists
        Throws an error if the user entered incorrect data
        :param student_id_in: string
        :param list_of_grades: ListOfGrades
        :return: None, removes a student from a ListOfStudents
        """
        if not self._input_checker.check_remove_student(student_id_in):
            raise InputError
        self._edit_action.update_history(self._remove_student_cascade(student_id_in, list_of_grades),
                                         self._inverse_remove_student_cascade(student_id_in, list_of_grades))
        self._list_of_students.remove_by_id(student_id_in)
        #  also remove the grades
        list_of_grades.remove_student(student_id_in)

    def _remove_student_cascade(self, student_id_in, list_of_grades):
        function_cascade = FunctionCascade()
        function_cascade.add_function(self._list_of_students.remove_by_id, [student_id_in])
        function_cascade.add_function(list_of_grades.remove_student, [student_id_in])
        return function_cascade

    def _inverse_remove_student_cascade(self, student_id_in, list_of_grades):
        function_cascade = FunctionCascade()
        student = self._list_of_students.get_by_id(student_id_in)
        function_cascade.add_function(self._list_of_students.add, [student])
        for grade in list_of_grades.get_repo():
            if grade.get_student_id() == student_id_in:
                function_cascade.add_function(list_of_grades.add, [grade])
        return function_cascade

    def update_student_name(self, student_id_in, name):
        """
        Updates name of a student
        Also adds the function and its inverse to the undo/redo lists
        Throws an error if the user entered incorrect data
        :param student_id_in: string
        :param name: string
        :return: None, just updates the name of a student from a ListOfStudents
        """
        if not self._input_checker.check_update_student_name(student_id_in, name):
            raise InputError
        self._edit_action.update_history(self._update_student_name_cascade(student_id_in, name),
                                         self._inverse_update_student_name_cascade(student_id_in))
        student = self._list_of_students.get_by_id(student_id_in)
        student.set_name(name)

    def _update_student_name_cascade(self, student_id_in, name):
        function_cascade = FunctionCascade()
        student = self._list_of_students.get_by_id(student_id_in)
        function_cascade.add_function(student.set_name, [name])
        return function_cascade

    def _inverse_update_student_name_cascade(self, student_id_in):
        function_cascade = FunctionCascade()
        student = self._list_of_students.get_by_id(student_id_in)
        function_cascade.add_function(student.set_name, [student.get_name()])
        return function_cascade

    def update_student_group(self, student_id_in, group):
        """
        Updates group of a student
        Also adds the function and its inverse to the undo/redo lists
        Throws an error if the user entered incorrect data
        :param student_id_in: string
        :param group: string
        :return: None, just updates the group of a student from a ListOfStudents
        """
        if not self._input_checker.check_update_student_group(student_id_in, group):
            raise InputError
        self._edit_action.update_history(self._update_student_group_cascade(student_id_in, group),
                                         self._inverse_update_student_group(student_id_in))
        student = self._list_of_students.get_by_id(student_id_in)
        student.set_group(group)

    def _update_student_group_cascade(self, student_id_in, group):
        function_cascade = FunctionCascade()
        student = self._list_of_students.get_by_id(student_id_in)
        function_cascade.add_function(student.set_group, [group])
        return function_cascade

    def _inverse_update_student_group(self, student_id_in):
        function_cascade = FunctionCascade()
        student = self._list_of_students.get_by_id(student_id_in)
        function_cascade.add_function(student.set_name, [student.get_name()])
        return function_cascade

    def students_received_assignment_alphabetic_order(self, assignment_id, list_of_grades):
        """
        Returns the ListOfStudents that received the assignment with assignment_id as
        its id and orders it in alphabetic order
        Throws an error if the user entered incorrect data
        :param assignment_id: string (that can be casted to uint)
        :return: ListOfStudents
        """
        if not self._input_checker.check_students_received_assignment_alphabetic_order(assignment_id):
            raise InputError
        ordered_student_list = ListOfStudents()
        for grade in list_of_grades.get_repo():
            if grade.get_assignment_id() == assignment_id:
                ordered_student_list.add(self._list_of_students.get_by_id(grade.get_student_id()))
        repo = ordered_student_list.get_repo()
        repo = sorted(repo, key=lambda student: student.get_name())
        ordered_student_list.set_repo(repo)
        return self.list_students_with_grades(list_of_grades, ordered_student_list)

    def students_received_assignment_grade_order(self, assignment_id, list_of_grades):
        """
        Returns the ListOfStudents that received the assignment with assignment_id as
        its id and orders it in grade order
        Throws an error if the user entered incorrect data
        :param assignment_id: string (that can be casted to uint)
        :return: ListOfStudents as string
        """
        if not self._input_checker.check_students_received_assignment_grade_order(assignment_id):
            raise InputError
        student_id_and_grade_list = []
        for grade in list_of_grades.get_repo():
            if grade.get_assignment_id() == assignment_id:
                student_id_and_grade_list.append([grade.get_student_id(), grade.get_grade()])

        def cmp(student_id_and_grade):
            grade = student_id_and_grade[1]
            if grade is None:
                return 0
            return int(grade)
        student_id_and_grade_list = sorted(student_id_and_grade_list,
                                           key=lambda student_id_and_grade: cmp(student_id_and_grade))

        ordered_student_list = ListOfStudents()
        for student_id_and_grade in student_id_and_grade_list:
            ordered_student_list.add(self._list_of_students.get_by_id(student_id_and_grade[0]))
        return self.list_students_with_grades(list_of_grades, ordered_student_list)

    def students_late_handing_assignment(self, list_of_assignments, list_of_grades):
        """
        Returns the ListOfStudents late in handing their assignments
        By late we mean that the deadline of the assignment is past the current date
        :return: ListOfStudents as string
        """
        student_list = ListOfStudents()
        current_date = date.today()
        current_date = datetime(year=current_date.year, month=current_date.month,
                                day=current_date.day,)
        for grade in list_of_grades.get_repo():
            assignment_id = grade.get_assignment_id()
            assignment = list_of_assignments.get_by_id(assignment_id)
            if assignment.get_deadline() < current_date:
                student_id = grade.get_student_id()
                student = self._list_of_students.get_by_id(student_id)
                student_list.add(student)
        return self.list_students_with_grades(list_of_grades, student_list)

    def students_with_best_school_situation(self, list_of_grades):
        """
        Returns the ListOfStudents ordered by the average grade of their
        assignments, in descending order
        :return: ListOfStudents as string
        """
        student_id_and_grades = {}
        for grade in list_of_grades.get_repo():
            if grade.get_grade() is None:
                continue
            if grade.get_student_id() not in student_id_and_grades.keys():
                student_id_and_grades.update({grade.get_student_id(): [grade.get_grade(), 1]})
            else:
                student_id_and_grades[grade.get_student_id()][0] += grade.get_grade()
                student_id_and_grades[grade.get_student_id()][1] += 1
        student_id_and_grades_list = []
        for student_id_and_grades_key in student_id_and_grades.keys():
            student_id_and_grades_list.append([student_id_and_grades_key,
                                          student_id_and_grades[student_id_and_grades_key][0] /
                                          student_id_and_grades[student_id_and_grades_key][1]])
        student_id_and_grades_list = sorted(student_id_and_grades_list, key=lambda student_id_and_grade:
                                            -student_id_and_grade[1])
        ordered_student_list = ListOfStudents()
        for student_id_and_grades in student_id_and_grades_list:
            ordered_student_list.add(self._list_of_students.get_by_id(student_id_and_grades[0]))
        return self.list_students_with_grades(list_of_grades, ordered_student_list)

class AssignmentController:
    def __init__(self, list_of_assignments, input_checker, edit_action):
        self._list_of_assignments = list_of_assignments
        self._input_checker = input_checker
        self._edit_action = edit_action

    def get_list_of_assignments(self):
        return self._list_of_assignments

    def list_assignments(self, list_of_assignments=None):
        """
        Lists assignments
        :param list_of_assignments: ListOfAssignments, with default value self._list_of_assignments
        :return: string
        """
        if list_of_assignments is None:
            list_of_assignments = self._list_of_assignments
        return str(list_of_assignments)

    def add_assignment(self, assignment_id_not_in, description, deadline):
        """
        Adds an assignment to the list of assignments
        Also adds the function and its inverse to the undo/redo lists
        Throws an error if the user entered incorrect data
        :param assignment_id_not_in: string
        :param description: string
        :param deadline: string
        :return: None, just adds an assignment
        """
        if not self._input_checker.check_add_assignment(assignment_id_not_in, description, deadline):
            raise InputError
        self._edit_action.update_history(self._add_assignment_cascade(assignment_id_not_in, description, deadline),
                                         self._inverse_add_assignment_cascade(assignment_id_not_in))
        self._list_of_assignments.add(Assignment(assignment_id_not_in, description, deadline))

    def _add_assignment_cascade(self, assignment_id_not_in, description, deadline):
        function_cascade = FunctionCascade()
        function_cascade.add_function(self._list_of_assignments.add, [Assignment(assignment_id_not_in, description,
                                                                                 deadline)])
        return function_cascade

    def _inverse_add_assignment_cascade(self, assignment_id_not_in):
        function_cascade = FunctionCascade()
        function_cascade.add_function(self._list_of_assignments.remove_by_id, [assignment_id_not_in])
        return function_cascade

    def remove_assignment(self, assignment_id_in, list_of_grades):
        """
        Removes an assignment from the list of assignments
        Also adds the function and its inverse to the undo/redo lists
        Throws an error if the user entered incorrect data
        :param assignment_id_in: string
        :param list_of_grades: ListOfGrades
        :return: None, just removes an assignment
        """
        if not self._input_checker.check_remove_assignment(assignment_id_in):
            raise InputError
        self._edit_action.update_history(self._remove_assignment_cascade(assignment_id_in, list_of_grades),
                                         self._inverse_remove_assignment_cascade(assignment_id_in, list_of_grades))
        self._list_of_assignments.remove_by_id(assignment_id_in)
        # also removes grades associated with this
        list_of_grades.remove_assignment(assignment_id_in)

    def _remove_assignment_cascade(self, assignment_id_in, list_of_grades):
        function_cascade = FunctionCascade()
        function_cascade.add_function(self._list_of_assignments.remove_by_id, [assignment_id_in])
        function_cascade.add_function(list_of_grades, [assignment_id_in])
        return function_cascade

    def _inverse_remove_assignment_cascade(self, assignment_id_in, list_of_grades):
        function_cascade = FunctionCascade()
        assignment = self._list_of_assignments.get_by_id(assignment_id_in)
        function_cascade.add_function(self._list_of_assignments.add, [assignment])
        for grade in list_of_grades.get_repo():
            if grade.get_assignment_id() == assignment_id_in:
                function_cascade.add_function(list_of_grades.add, [grade])
        return function_cascade

    def update_assignment_description(self, assignment_id_in, description):
        """
        Updates the description of an assignment
        Also adds the function and its inverse to the undo/redo lists
        Throws an error if the user entered incorrect data
        :param assignment_id_in:  string
        :param description: string
        :return: None, just updates the description of an assignment
        """
        if not self._input_checker.check_update_assignment_description(assignment_id_in, description):
            raise InputError
        self._edit_action.update_history(self._update_assignment_description_cascade(assignment_id_in, description),
                                         self._inverse_update_assignment_description_cascade(assignment_id_in))
        assignment = self._list_of_assignments.get_by_id(assignment_id_in)
        assignment.set_description(description)

    def _update_assignment_description_cascade(self, assignment_id_in, description):
        function_cascade = FunctionCascade()
        assignment = self._list_of_assignments.get_by_id(assignment_id_in)
        function_cascade.add_function(assignment.set_description, [description])
        return function_cascade

    def _inverse_update_assignment_description_cascade(self, assignment_id_in):
        function_cascade = FunctionCascade()
        assignment = self._list_of_assignments.get_by_id(assignment_id_in)
        function_cascade.add_function(assignment.set_description, [assignment.get_description()])
        return function_cascade

    def update_assignment_deadline(self, assignment_id_in, deadline):
        """
        Updates the deadline of an assignment
        Also adds the function and its inverse to the undo/redo lists
        Throws an error if the user entered incorrect data
        :param assignment_id_in: string
        :param deadline: string
        :return: None, just updates the deadline of an assignment
        """
        if not self._input_checker.check_update_assignment_deadline(assignment_id_in, deadline):
            raise InputError
        self._edit_action.update_history(self._update_assignment_deadline_cascade(assignment_id_in, deadline),
                                         self._inverse_update_assignment_deadline_cascade(assignment_id_in))
        assignment = self._list_of_assignments.get_by_id(assignment_id_in)
        assignment.set_deadline(deadline)

    def _update_assignment_deadline_cascade(self, assignment_id_in, deadline):
        function_cascade = FunctionCascade()
        assignment = self._list_of_assignments.get_by_id(assignment_id_in)
        function_cascade.add_function(assignment.set_deadline, deadline)
        return function_cascade

    def _inverse_update_assignment_deadline_cascade(self, assignment_id_in):
        function_cascade = FunctionCascade()
        assignment = self._list_of_assignments.get_by_id(assignment_id_in)
        function_cascade.add_function(assignment.set_deadline, assignment.get_deadline())
        return function_cascade

    def assignments_given_grade_order(self, list_of_grades):
        """
        Returns a ListOfAssignments ordered by the average grade
        of students that were graded for it
        :return: ListOfAssignments as string
        """
        assignment_id_and_grades = {}
        for grade in list_of_grades.get_repo():
            if grade.get_grade() is None:
                continue
            if grade.get_assignment_id() not in assignment_id_and_grades.keys():
                assignment_id_and_grades.update({grade.get_assignment_id():
                                                 [grade.get_grade(), 1]})
            else:
                assignment_id_and_grades[grade.get_assignment_id()][0] += grade.get_grade()
                assignment_id_and_grades[grade.get_assignment_id()][1] += 1
        assignment_id_and_grades_list = []
        for assignment_id_and_grades_key in assignment_id_and_grades.keys():
            assignment_id_and_grades_list.append([assignment_id_and_grades_key,
                                                  assignment_id_and_grades[assignment_id_and_grades_key][0] /
                                                  assignment_id_and_grades[assignment_id_and_grades_key][1]])
        assignment_id_and_grades_list = sorted(assignment_id_and_grades_list, key=lambda assignment_id_and_grade:
                                                -assignment_id_and_grade[1])
        ordered_assignment_list = ListOfAssignments()
        for assignment_id_and_grade in assignment_id_and_grades_list:
            ordered_assignment_list.add(self._list_of_assignments.get_by_id(assignment_id_and_grade[0]))
        return self.list_assignments(ordered_assignment_list)


class GradeController:
    def __init__(self, list_of_grades, input_checker, edit_action):
        self._list_of_grades = list_of_grades
        self._input_checker = input_checker
        self._edit_action = edit_action

    def get_list_of_grades(self):
        return self._list_of_grades

    def list_grades(self):
        """
        Lists the grades
        :return: string
        """
        return str(self._list_of_grades)

    def assign_students_assignment(self, assignment_id_in, number, student_id_list):
        """
        Assigns a number of students an assignment
        Also adds the function and its inverse to the undo/redo lists
        Throws an error if the user entered incorrect data
        :param assignment_id_in: string
        :param number: string
        :param student_id_list: string
        :return: None, just assigns a number of students an assignment
        """
        if not self._input_checker.check_assign_students_assignment(assignment_id_in, number, student_id_list):
            raise InputError
        self._edit_action.update_history(self._assign_student_assignment_cascade(assignment_id_in, student_id_list),
                                         self._inverse_assign_student_assignment_cascade(assignment_id_in, student_id_list))
        for student_id in student_id_list:
            self._list_of_grades.add(Grade(assignment_id_in, student_id))

    def _assign_student_assignment_cascade(self, assignment_id_in, student_id_list):
        function_cascade = FunctionCascade()
        for student_id in student_id_list:
            function_cascade.add_function(self._list_of_grades.add, [Grade(assignment_id_in, student_id)])
        return function_cascade

    def _inverse_assign_student_assignment_cascade(self, assignment_id_in, student_id_list):
        function_cascade = FunctionCascade()
        for student_id in student_id_list:
            function_cascade.add_function(self._list_of_grades.remove_by_id, [(assignment_id_in, student_id)])
        return function_cascade

    def grade_student_assignment(self, student_id_in, assignment_id_in_student_ungraded, grade):
        """
        Grades the assignment of a student
        Also adds the function and its inverse to the undo/redo lists
        Throws an error if the user entered incorrect data
        :param student_id_in: string
        :param assignment_id_in_student_ungraded: string
        :param grade: string
        :return: None, just grades the assignment of a student
        """
        if not self._input_checker.check_grade_student_assignment(student_id_in,
                                                                  assignment_id_in_student_ungraded, grade):
            raise InputError
        self._edit_action.update_history(self._grade_student_assignment_cascade(student_id_in,
                                                                                assignment_id_in_student_ungraded,
                                                                                grade),
                                         self._inverse_grade_student_assignment_cascade(student_id_in,
                                                                                        assignment_id_in_student_ungraded))
        grade_obj = self._list_of_grades.get_by_id((assignment_id_in_student_ungraded, student_id_in))
        grade_obj.set_grade(grade)

    def _grade_student_assignment_cascade(self, student_id_in, assignment_id_in_student_ungraded, grade):
        function_cascade = FunctionCascade()
        grade_obj = self._list_of_grades.get_by_id((assignment_id_in_student_ungraded, student_id_in))
        function_cascade.add_function(grade_obj.set_grade, [grade])
        return function_cascade

    def _inverse_grade_student_assignment_cascade(self, student_id_in, assignment_id_in_student_ungraded):
        function_cascade = FunctionCascade()
        grade_obj = self._list_of_grades.get_by_id((assignment_id_in_student_ungraded, student_id_in))
        function_cascade.add_function(grade_obj.set_grade, [None])
        return function_cascade


class EditActionController:
    def __init__(self, edit_action):
        self._edit_action = edit_action

    def undo(self):
        self._edit_action.undo()

    def redo(self):
        self._edit_action.redo()

