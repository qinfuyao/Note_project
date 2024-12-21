# tasks/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # /tasks/
    path('create/', views.task_create, name='task_create'),  # /tasks/create/
    path('<int:pk>/update/', views.task_update, name='task_update'),  # /tasks/<pk>/update/
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),  # /tasks/<pk>/delete/
]