from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ece-students/', views.students_list, name='students_list'),
    path('ece-students/<str:roll_no>/<str:dob>/<str:mother_name>', views.student_detail, name='student_detail'),
    path('<str:id>/registration/', views.registration, name="registration"),
    path('thank_you', views.thank_you, name='thank_you'),
    path('data_exist', views.data_exist, name='data_exist'),
    path('ece-students/login/<str:roll_no>', views.login, name='login')
]

