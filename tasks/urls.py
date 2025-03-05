from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_task_form/', views.add_task_form, name='add_task_form'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('update_task/<int:task_id>/', views.update_task, name='update_task'),
    path('task_confirm_delete/<int:task_id>/', views.task_confirm_delete, name='task_confirm_delete'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
]