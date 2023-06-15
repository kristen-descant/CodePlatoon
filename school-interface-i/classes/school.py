from classes.student import Student
from classes.staff import Staff

class School():

    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()
        self.number_of_students = len(self.students)
        self.number_of_staff = len(self.staff)








