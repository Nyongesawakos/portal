from django.contrib import admin

# Register your models here.from django.contrib import admin
from .models import CourseUnit, Result, Student

admin.site.register(CourseUnit)
admin.site.register(Result)
admin.site.register(Student)