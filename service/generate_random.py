import string
import random
import time
import datetime

class GenerateRandom:
    @staticmethod
    def int_generator(lb=1, ub=300):
        return random.randint(lb, ub)

    @staticmethod
    def str_int_generator(lb=1, ub=300):
        return str(random.randint(lb, ub))

    @staticmethod
    def date_generator(lb=str(datetime.date.today() - datetime.timedelta(days=10)),
                       ub=None):
        if ub is None:
            ub = str(datetime.date.today() + datetime.timedelta(days=GenerateRandom.int_generator()))

        format_ = '%Y-%m-%d'
        startime = time.mktime(time.strptime(lb, format_))
        endtime = time.mktime(time.strptime(ub, format_))
        time_ = startime + random.random() * (endtime - startime)

        temp_date = str(time.strftime(format_, time.localtime(time_)))
        temp_date = temp_date.split('-')
        return temp_date[2] + '/' + temp_date[1] + '/' + temp_date[0]

    @staticmethod
    def grade_generator():
        grade_options = [None, random.randint(1, 10)]
        return grade_options[random.randint(0, 1)]

    @staticmethod
    def string_generator(size=None, chars=string.ascii_uppercase + string.digits):
        if size is None:
            size = GenerateRandom.int_generator(3, 10)
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def grade_id_generator(list_of_assignments, list_of_students):
        random_assignment = random.choice(list_of_assignments.get_repo())
        random_student = random.choice(list_of_students.get_repo())
        return (random_assignment.get_id(), random_student.get_id())
