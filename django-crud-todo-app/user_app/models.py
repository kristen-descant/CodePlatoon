from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(verbose_name='email address', unique=True)
    password = models.CharField(max_length=128)  
    age = models.PositiveIntegerField(validators=[MaxValueValidator(110)])
    display_name = models.CharField(default="New user", max_length=25)
    address = models.TextField(null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= []