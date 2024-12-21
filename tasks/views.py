# Create your views here.
# tasks/views.py

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TaskForm
from .models import Task


@login_required
def task_list(request):
    """
    展示当前用户负责的所有任务。
    """
    tasks = Task.objects.filter(assignees=request.user).order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    """
    创建新任务。
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.assignees.add(request.user)  # 将当前用户加入负责人
            messages.success(request, '任务已成功创建。')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_create.html', {'form': form})

@login_required
def task_update(request, pk):
    """
    更新现有任务。
    """
    task = get_object_or_404(Task, pk=pk, assignees=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, '任务已成功更新。')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_update.html', {'form': form, 'task': task})

@login_required
def task_delete(request, pk):
    """
    删除任务。
    """
    task = get_object_or_404(Task, pk=pk, assignees=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, '任务已成功删除。')
        return redirect('task_list')
    return render(request, 'tasks/task_delete_confirm.html', {'task': task})