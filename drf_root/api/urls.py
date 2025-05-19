from django.urls import path, include
from . import views

urlpatterns = [
  path("students/", views.student_list, name="student_list"),
  path("students/create/", views.student_create, name="student_create"),
  path("teachers/", views.teacher_list, name="teacher_list"),
  path("teachers/create", views.teacher_create, name="teacher_create"),
]
