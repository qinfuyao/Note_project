# Create your views here.

# notes/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Note


def note_list(request):
    """
    展示所有笔记的列表
    """
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_create(request):
    """
    创建一条新的笔记
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Note.objects.create(title=title, content=content)
        return redirect('note_list')  # 创建成功后，重定向到笔记列表页面

    # 如果是 GET 请求，则展示表单页面
    return render(request, 'notes/note_create.html')



@login_required
def note_list(request):
    notes = Note.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': notes})

@login_required
def note_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(title=title, content=content, author=request.user)
        return redirect('note_list')
    return render(request, 'notes/note_create.html')