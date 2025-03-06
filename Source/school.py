
class TooManyStudentsError(Exception):
    pass

class School:
    def __init__(self, students, teacher, course_name):
        self.students = students
        self.teacher = teacher
        self.course_name = course_name

    def add_student(self, student):
        if len(self.students) < 10:
            self.students.append(student)
        else:
            raise TooManyStudentsError

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def change_teacher(self, new_teacher):
        self.teacher = new_teacher

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    pass

class Student(Person):
    pass


