# django-taskManager-midtermProject
Task Manager


# Features
- Add Task: Create new tasks with relevant details.
- Edit Task: Modify existing tasks, including updating their status.
- Delete Task: Remove tasks that are no longer needed.
- Task List: View all tasks in an organized manner.
- Task Status Management: Change the task status to "Pending", "Complete", or "Overdue".

# Setup Key
  Terminal:
    pipenv intall django
    pip install psycopg2 (since I'm using postgresql)
    django-admin startproject task_manager .
    python manage.py startapp tasks
  add app name on installed apps{} at settings.py
  add your database in databases{} at settings.py
  add urls.py file and template folder on app level
  add model on models.py
  Terminal:
    python manage.py makemigrations
    python manage.py migrate
# To run
  Terminal:
    python manage.py runserver
    press the development server url given (http://127.0.0.1:8000/)

# Functionality
- Users can add tasks with a title and description.
- Users can edit tasks, including changing their status.
- Users can delete tasks they no longer need.
- The task list displays all tasks with their current status.
- Task status can be updated to Pending, Complete, or Overdue based on progress.
- The status automatically define depends on the date added
