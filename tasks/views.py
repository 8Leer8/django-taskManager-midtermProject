from django.shortcuts import render, redirect
from .models import Task
from datetime import date

#function for list of tasks
def task_list(request):
    query = request.GET.get('q', '').strip()
    tasks = Task.objects.all()
    if query:
        tasks = tasks.filter(title__icontains=query)
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'query': query})

#function for create
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        due_date_str = request.POST.get('due_date', '').strip()

        if title and due_date_str:
            try:
                due_date = date.fromisoformat(due_date_str)
                status = 'Overdue' if due_date < date.today() else 'Pending'
                Task.objects.create(title=title, description=description, due_date=due_date, status=status)
                return redirect('task_list')
            except ValueError:
                error_message = "Invalid date format. Please use YYYY-MM-DD."
        else:
            error_message = "Title and Due Date are required."
        
        return render(request, 'tasks/task_form.html', {'error_message': error_message})
    
    return render(request, 'tasks/task_form.html')

#function for update
def task_update(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        due_date_str = request.POST.get('due_date', '').strip()
        is_completed = request.POST.get('status') == 'on'

        if title and due_date_str:
            try:
                due_date = date.fromisoformat(due_date_str)
                status = "Completed" if is_completed else ("Overdue" if due_date < date.today() else "Pending")

                task.title = title
                task.description = description
                task.due_date = due_date
                task.status = status
                task.save()

                return redirect('task_list')
            except ValueError:
                error_message = "Invalid date format. Please use YYYY-MM-DD."
        else:
            error_message = "Title and Due Date are required."

        return render(request, 'tasks/task_form.html', {'task': task, 'error_message': error_message})

    return render(request, 'tasks/task_form.html', {'task': task})

#function for delete
def task_delete(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return redirect('task_list')

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
