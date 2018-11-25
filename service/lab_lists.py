from repository.repository import Repository
from domain.components import *
from service.generate_random import GenerateRandom


class ListOfStudents(Repository):
    @staticmethod
    def default_list():
        """
        Generates a default list of Students
        :return: a list of Students
        """
        def_list = []
        id_list = []
        for i in range(100):
            id_ = GenerateRandom.str_int_generator()
            while id_ in id_list:
                id_ = GenerateRandom.str_int_generator()
            id_list.append(id_)
            def_list.append(Student(id_,
                                    GenerateRandom.string_generator(),
                                    GenerateRandom.str_int_generator()))
        return sorted(def_list)

    def update_name(self, id_, name):
        """
        Update the name of a student in the list of students
        :param id_: the student id
        :param name: the student's new name
        :return: None
        """
        for student in self._repo:
            if student.get_id() == id_:
                student.set_name(name)
                break

    def update_group(self, id_, group):
        """
        Updates group of the student in this list
        :param id_: string (can be casted to uint)
        :param group: string (can be casted to uint)
        :return: None
        """
        for student in self._repo:
            if student.get_id() == id_:
                student.set_group(group)
                break

class ListOfAssignments(Repository):
    @staticmethod
    def default_list():
        """
        Generates a default list of assignments
        :return: a list of Assignments
        """
        def_list = []
        id_list = []
        for i in range(100):
            id_ = GenerateRandom.str_int_generator()
            while id_ in id_list:
                id_ = GenerateRandom.str_int_generator()
            id_list.append(id_)
            def_list.append(Assignment(id_,
                                       GenerateRandom.string_generator(),
                                       GenerateRandom.date_generator()))
        return sorted(def_list)

    def update_deadline(self, id_, deadline):
        """
        Updates the deadline of this assignment
        :param id_: string
        :param deadline: string
        :return: None
        """
        for assignment in self._repo:
            if assignment.get_id() == id_:
                assignment.set_deadline(deadline)
                break

    def update_description(self, id_, description):
        """
        Updates the description of this assignment
        :param id_: string
        :param description: string
        :return: None
        """
        for assignment in self._repo:
            if assignment.get_id() == id_:
                assignment.set_description(description)
                break


class ListOfGrades(Repository):
    @staticmethod
    def default_list(list_of_assignments, list_of_students):
        def_list = []
        id_list = []
        for i in range(100):
            id_= GenerateRandom.grade_id_generator(list_of_assignments, list_of_students)
            while id_ in id_list:
                id_= GenerateRandom.grade_id_generator(list_of_assignments, list_of_students)
            def_list.append(Grade(id_[0], id_[1], GenerateRandom.grade_generator()))
            id_list.append(id_)
        return sorted(def_list)

    def add(self, obj):
        """
        Overrides the add method of the Repository
        Adds a grade to the list
        :param obj: Grade
        :return: None
        """
        for grade_obj in self._repo:
            if grade_obj.get_student_id() == obj.get_student_id() and\
               grade_obj.get_assignment_id() == obj.get_assignment_id():
                return
        self._repo.append(obj)

    def already_graded_student_for_assignment(self, assignment_id, student_id):
        """
        Checks if the student is already graded for an assignment
        :param assignment_id: string
        :param student_id: string
        :return: bool
        """
        for grade_obj in self._repo:
            if grade_obj.get_student_id() == student_id and\
               grade_obj.get_assignment_id() == assignment_id and\
               grade_obj.get_grade() is not None:
                return True
        return False

    def grade_student_for_assignment(self, assignment_id, student_id, grade):
        """
        Grades a student for assignment
        :param assignment_id: string
        :param student_id: string
        :param grade: string
        :return: None
        """
        for grade_obj in self._repo:
            if grade_obj.get_assignment_id() == assignment_id and\
               grade_obj.get_student_id() == student_id and grade_obj.get_grade() is None:
                grade_obj.set_grade(grade)

    def remove_student(self, student_id):
        """
        Removes the assignment that have student_id
        :param student_id: string
        :return: None
        """
        for grade_obj in self._repo[:]:
            if grade_obj.get_student_id() == student_id:
                self.remove(grade_obj)

    def remove_assignment(self, assignment_id):
        """
        Removes assignments that have assignment_id
        :param assignment_id: string
        :return: None
        """
        for assignment in self._repo[:]:
            if assignment.get_assignment_id() == assignment_id:
                self.remove(assignment)

    def get_student_grades(self, student_id):
        """
        Gets grades with student_id
        :param student_id: string
        :return: ListOfGrades
        """
        list_of_grades = ListOfGrades()
        for grade_obj in self._repo:
            if grade_obj.get_student_id() == student_id:
                list_of_grades.add(grade_obj)
        return list_of_grades
