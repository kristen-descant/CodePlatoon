from classes.person import Person
import csv


class Student(Person):
    all_students_list = []

    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, role, password)
        self.school_id = school_id
        
    @classmethod
    def all_students(cls):
        
        with open('/home/kristen_descant/codePlatoon/week2day4/school-interface-i-kristen-descant/data/students.csv', 'r', newline='') as infile:
            reader = csv.DictReader(infile)

            next(reader)

            for row in reader:
                cls.all_students_list.append(Student(**row))

        return cls.all_students_list

print(Student.all_students())

