from django.db import models
from django.contrib.auth.models import AbstractUser


class customUser(AbstractUser):
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.username + " " +self.last_name

# Create your models here.
class teacherModel(models.Model):
    firstname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.firstname
    

class studentModel(models.Model):
    firstname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.firstname
    
class staffModel(models.Model):
    firstname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.firstname
    

class doctorModel(models.Model):
    firstname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.firstname
    
class nurseModel(models.Model):
    firstname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.firstname
    

class employeeModel(models.Model):
    firstname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.firstname