from classes.person import Person
import csv

class Staff(Person):
    all_staff_list = []

    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id

    @classmethod
    def all_staff(cls):
        
        with open('/home/kristen_descant/codePlatoon/week2day4/school-interface-i-kristen-descant/data/staff.csv', 'r', newline='') as infile:
            reader = csv.DictReader(infile)

            next(reader)

            for row in reader:
                cls.all_staff_list.append(Staff(**row))

        return cls.all_staff_list
    
print(Staff.all_staff())