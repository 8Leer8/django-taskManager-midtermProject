# django-taskManager-midtermProject
Task Manager


# Features
- Add Task: Create new tasks with relevant details.
- Edit Task: Modify existing tasks, including updating their status.
- Delete Task: Remove tasks that are no longer needed.
- Task List: View all tasks in an organized manner.
- Task Status Management: The status are automatically set depends on the date but u can edit it if it is complete or not.

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
- Users can edit tasks, including changing the status to complete.
- Users can delete tasks they no longer need.
- The task list displays all tasks with their current status.
- Task status can be updated to Complete by checking the checkbox.
- The status automatically define depends on the date added
