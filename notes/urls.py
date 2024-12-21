# notes/urls.py
from django.urls import path, include

from . import views

urlpatterns = [
    # 访问 /notes/ 时触发 note_list
    path('', views.note_list, name='note_list'),
    # 访问 /notes/create/ 时触发 note_create
    path('create/', views.note_create, name='note_create'),
    path('tasks/', include('tasks.urls')),
]