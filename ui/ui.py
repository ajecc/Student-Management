from domain.components import *

class ReadInput:
    def _read_student_id_not_in(self):
        student_id_not_in = input("student_id = ")
        return student_id_not_in

    def _read_student_id_in(self):
        student_id_in = input("student_id = ")
        return student_id_in

    def _read_assignment_id_not_in(self):
        assignment_id_not_in = input("assignment_id = ")
        return assignment_id_not_in

    def _read_assignment_id_in(self):
        assignment_id_in = input("assignment_id = ")
        return assignment_id_in

    def _read_name(self):
        name = input("name = ")
        return name

    def _read_group(self):
        group = input("group = ")
        return group

    def _read_description(self):
        description = input("description = ")
        return description

    def _read_deadline(self):
        deadline = input("deadline = ")
        return deadline

    def _read_number(self):
        number = input("number = ")
        return number

    def _read_assignment_id_in_student_ungraded(self):
        assignment_id_in_student_ungraded = input("assignment_id_in_student_ungraded = ")
        return assignment_id_in_student_ungraded

    def _read_grade(self):
        grade = input("grade = ")
        return grade

class ProcessInput(ReadInput):
    def __init__(self, student_controller, assignment_controller, grade_controller, edit_action_controller):
        self._student_controller = student_controller
        self._assignment_controller = assignment_controller
        self._grade_controller = grade_controller
        self._edit_action_controller = edit_action_controller

    def _list_students_with_grades(self):
        print(self._student_controller.list_students_with_grades(self._grade_controller.get_list_of_grades()))

    def _list_assignments(self):
        print(self._assignment_controller.list_assignments())

    def _list_grades(self):
        print(self._grade_controller.list_grades())

    def _add_student(self):
        student_id_not_in = self._read_student_id_not_in()
        name = self._read_name()
        group = self._read_group()
        self._student_controller.add_student(student_id_not_in, name, group)

    def _add_assignment(self):
        assignment_id_not_in = self._read_assignment_id_not_in()
        description = self._read_description()
        deadline = self._read_deadline()
        self._assignment_controller.add_assignment(assignment_id_not_in, description, deadline)

    def _remove_student(self):
        student_id_in = self._read_student_id_in()
        self._student_controller.remove_student(student_id_in, self._grade_controller.get_list_of_grades())

    def _remove_assignment(self):
        assignment_id_in = self._read_assignment_id_in()
        self._assignment_controller.remove_assignment(assignment_id_in, self._grade_controller.get_list_of_grades())

    def _update_student_name(self):
        student_id_in = self._read_student_id_in()
        name = self._read_name()
        self._student_controller.update_student_name(student_id_in, name)

    def _update_student_group(self):
        student_id_in = self._read_student_id_in()
        group = self._read_group()
        self._student_controller.update_student_group(student_id_in, group)

    def _update_assignment_description(self):
        assignment_id_in = self._read_assignment_id_in()
        description = self._read_description()
        self._assignment_controller.update_assignment_description(assignment_id_in, description)

    def _update_assignment_deadline(self):
        assignment_id_in = self._read_assignment_id_in()
        deadline = self._read_deadline()
        self._assignment_controller.update_assignment_deadline(assignment_id_in, deadline)

    def _assign_students_assignment(self):
        assignment_id_in = self._read_assignment_id_in()
        number = self._read_number()
        student_id_list = []
        for i in range(int(number)):
            student_id_in = self._read_student_id_in()
            student_id_list.append(student_id_in)
        self._grade_controller.assign_students_assignment(assignment_id_in, number, student_id_list)

    def _grade_student_assignment(self):
        student_id_in = self._read_student_id_in()
        assignment_id_in_student_ungraded = self._read_assignment_id_in_student_ungraded()
        grade = self._read_grade()
        self._grade_controller.grade_student_assignment(student_id_in, assignment_id_in_student_ungraded, grade)

    def _students_received_assignment_alphabetic_order(self):
        assignment_id_in = self._read_assignment_id_in()
        print(self._student_controller.students_received_assignment_alphabetic_order(assignment_id_in,
                                                          self._grade_controller.get_list_of_grades()))

    def _students_received_assignment_grade_order(self):
        assignment_id_in = self._read_assignment_id_in()
        print(self._student_controller.students_received_assignment_grade_order(assignment_id_in,
                                                            self._grade_controller.get_list_of_grades()))

    def _students_late_handing_assignment(self):
        print(self._student_controller.students_late_handing_assignment(
            self._assignment_controller.get_list_of_assignments(), self._grade_controller.get_list_of_grades()))

    def _students_with_best_school_situation(self):
        print(self._student_controller.students_with_best_school_situation(self._grade_controller.get_list_of_grades()))

    def _assignments_given_grade_order(self):
        print(self._assignment_controller.assignments_given_grade_order(self._grade_controller.get_list_of_grades()))

    def _undo(self):
        self._edit_action_controller.undo()

    def _redo(self):
        self._edit_action_controller.redo()

class MenuUI(ProcessInput):
    def __init__(self, student_controller, assignment_controller, grade_controller, edit_action_controller):
        super().__init__(student_controller, assignment_controller, grade_controller, edit_action_controller)
        self._menu_commands = {
            "1": self._list_students_with_grades,
            "2": self._list_assignments,
            "3": self._list_grades,
            "4": self._add_student,
            "5": self._add_assignment,
            "6": self._remove_student,
            "7": self._remove_assignment,
            "8": self._update_student_name,
            "9": self._update_student_group,
            "10": self._update_assignment_description,
            "11": self._update_assignment_deadline,
            "12": self._assign_students_assignment,
            "13": self._grade_student_assignment,
            "14": self._students_received_assignment_alphabetic_order,
            "15": self._students_received_assignment_grade_order,
            "16": self._students_late_handing_assignment,
            "17": self._students_with_best_school_situation,
            "18": self._assignments_given_grade_order,
            "19": self._undo,
            "20": self._redo,
            "exit": self._exit,
            "man": self._list_commands,
        }

    def _list_commands(self):
        # quick list of commands output -> messy but enough for this project
        list_of_commands = []
        for command in self._menu_commands.keys():
            list_of_commands.append([command, self._menu_commands[command].__name__])
        def cmp(command):
            if len(command[0]) == 1:
                return "0" + command[0]
            return command[0]
        list_of_commands = sorted(list_of_commands, key=lambda command: cmp(command))
        for i in list_of_commands:
            print(i[0] + ": " + i[1][1::])

    def _exit(self):
        exit(0)

    def main(self):
        while True:
            input_ = input("Enter your command :D\n")
            if input_ not in self._menu_commands.keys():
                print("Oops, your command is not good, try again ;)")
                continue
            try:
                self._menu_commands[input_]()
            except:
                print("Error :(")

