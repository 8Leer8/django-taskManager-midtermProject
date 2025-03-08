from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # URL for list of tasks
    path('create/', views.task_create, name='task_create'), # URL for create
    path('update/<int:task_id>/', views.task_update, name='task_update'),  # URL for update
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'), # URL for delete
]
