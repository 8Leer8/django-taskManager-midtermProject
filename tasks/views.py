from django.shortcuts import render, redirect
from .models import Task
from datetime import date

def index(request):
    que = request.GET.get('q', '').strip()
    tasks = Task.objects.filter(title__istartswith=que) if que else Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks, 'query': que})

def add_task_form(request):
    error_message = None
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        due_date_str = request.POST.get('due_date', '').strip()

        if not title or not due_date_str:
            error_message = "Title and Due Date are required."

        else:
            try:
                due_date = date.fromisoformat(due_date_str)
                status = 'Overdue' if due_date < date.today() else 'Pending'
                Task.objects.create(title=title, description=description, due_date=due_date, status=status)
                return redirect('index')
            except ValueError:
                error_message = "Invalid date format. Please use YYYY-MM-DD."

    return render(request, 'add_task_form.html', {'error_message': error_message})

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'edit_task_form.html', {'task': task})

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    error_message = None

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        due_date_str = request.POST.get('due_date', '').strip()
        status = request.POST.get('status', '').strip()

        if not title or not status:
            error_message = "Title and Status are required."

        else:
            if due_date_str:
                try:
                    task.due_date = date.fromisoformat(due_date_str)
                except ValueError:
                    error_message = "Invalid date format. Please use YYYY-MM-DD."

            task.title = title
            task.description = description
            task.status = status

            if not error_message: 
                task.save()
                return redirect('index')

    return render(request, 'edit_task_form.html', {'task': task, 'error_message': error_message})

def task_confirm_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'task_confirm_delete.html', {'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return redirect('index')
