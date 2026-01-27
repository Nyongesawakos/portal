from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    reg_no = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    grade= models.CharField(max_length=100, blank=True)
    fee_paid = models.CharField(max_length=100, blank=True)
    arrears = models.CharField(max_length=100, blank=True)
    assessment_no=models.CharField(max_length=100, blank=True)
    UPI=models.CharField(max_length=100, blank=True)
    emergency_contact = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.reg_no
class CourseUnit(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=100)
    credit_units = models.IntegerField()

    def __str__(self):
        return self.code
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    unit = models.ForeignKey(CourseUnit, on_delete=models.CASCADE)
    marks = models.IntegerField()
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student} - {self.unit}"
