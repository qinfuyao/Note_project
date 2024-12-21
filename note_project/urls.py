# note_project/urls.py
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.urls import path, include


def home_view(request):
    return HttpResponse("<h1>Welcome to my Note project!</h1>")

urlpatterns = [
    path('', home_view, name='home'),  # 访问 / 时的主页
    path('login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('notes/', include('notes.urls')),  # 把 /notes/ 下的路由交给 notes/urls.py
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),  # 包含 tasks 应用的 URL
]