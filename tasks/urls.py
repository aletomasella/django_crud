from django.urls import path
from .views import list_task, create_task, delete_task

urlpatterns = [
    path('', list_task, name='list_task'),
    path('new/', create_task, name='create_task'),
    path('delete/<int:id>/', delete_task, name='delete_task'),
]