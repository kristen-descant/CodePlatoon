from django.db import models
from django.core.exceptions import ValidationError
from .validators import validate_professor_name, validate_subject_format

# Create your models here.
class Class(models.Model):
    subject = models.CharField(max_length=255, null=False, unique=True, validators=[validate_subject_format])
    professor = models.CharField(max_length=255, null=False, default='Mr. Cahan', validators=[validate_professor_name])

    def clean(self):
        if self.students.count() < 1 or self.students.count() > 30:
            raise ValidationError("A class must have between 1 and 30 students")

    def __str__(self):
        return f"{self.subject} - {self.professor} - {self.students.count()}"
    
    def add_a_student(self, student_id):
        self.students.add(student_id)
        self.save()
    
    def drop_a_student(self, student_id):
        if student_id in self.students:
            self.drop(student_id)
            self.save()