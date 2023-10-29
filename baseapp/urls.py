from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('login/', views.login_user, name ='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    #path('create_task/', views.create_task, name='create_task'),
    path('assign_task/', views.assign_task, name='assign_task'),
    path('task_list/', views.task_detail, name='task_list'),
]

