from django.urls import path
from . import views 

urlpatterns = [       
path('dashboard', views.dashboard, name= 'dashboard'),
path('courses/', views.courses, name= 'courses'),
path('excel-upload/', views.excel, name= 'excel'),
#path('profile/', views.profile, name= 'profile'), 
path('profile/<str:pk>/', views.profile, name='profile'),
path('announce/', views.announce, name= 'announce'),
path("upload/students/", views.upload_students),
path("upload/units/", views.upload_units),
path("upload/results/", views.upload_results),
path('add/', views.add_student, name='add'),
path('student_list', views.student_list, name='student_list'),
path('updatStudent/<str:pk>/', views.updateStudent, name='updateStudent'),
path('deleteStudent/<str:pk>/', views.deleteStudent, name='deleteStudent'),
]