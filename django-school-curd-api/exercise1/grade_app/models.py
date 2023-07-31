from django.db import models
from student_app.models import Student
from class_app.models import Class
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

# Create your models here.

class Grade(models.Model):
    grade = models.DecimalField(null=False, default=100, max_digits=5,
        decimal_places=2,validators=[MinValueValidator(1.), MaxValueValidator(100.)])
    a_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

