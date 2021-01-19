from django.urls import path
from .views import show_grid
from .views import show_task
from .views import new_task
from .views import create_task

urlpatterns = [
    path('', show_grid, name='show_grid'),
    path('task/<int:id>', show_task, name='show_task'),
    path('new/', new_task, name='new_task'),
    path('create/', create_task, name='create_task'),
]
