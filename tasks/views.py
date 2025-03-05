from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Task
from datetime import date

def index(request):
    que = request.GET.get('q', '').strip()
    tasks = Task.objects.filter(title__istartswith=que) if que else Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks, 'query': que})

def add_task_form(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        due_date_str = request.POST.get('due_date', '').strip()
        if not title or not due_date_str:
            return HttpResponseBadRequest("Missing required fields.")
        try:
            due_date = date.fromisoformat(due_date_str)
        except ValueError:
            return HttpResponseBadRequest("Invalid date format.")
        status = 'Overdue' if due_date < date.today() else 'Pending'
        Task.objects.create(title=title, description=description, due_date=due_date, status=status)
        return redirect('index')
    return render(request, 'add_task_form.html')

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'edit_task_form.html', {'task': task})

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    title = request.POST.get('title', '').strip()
    description = request.POST.get('description', '').strip()
    due_date_str = request.POST.get('due_date', '').strip()
    status = request.POST.get('status', '').strip()
    if not title or not status:
        return HttpResponseBadRequest("missing required fields.")
    if due_date_str:
        try:
            due_date = date.fromisoformat(due_date_str)
            task.due_date = due_date
        except ValueError:
            return HttpResponseBadRequest("invalid date format.")
    task.title = title
    task.description = description
    task.status = status
    task.save()
    return redirect('index')

def task_confirm_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'task_confirm_delete.html', {'task': task})

    return render(request, 'task_confirm_delete.html', {'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        return redirect('index')
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)
