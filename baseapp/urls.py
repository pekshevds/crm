from django.urls import path
from .views import show_grid
from .views import show_task
from .views import new_task
from .views import create_task

from .views import set_b
from .views import set_c
from .views import set_d

from .views import get_employes_json

urlpatterns = [
    path('', show_grid, name='show_grid'),
    path('task/<int:id>', show_task, name='show_task'),
    path('new/', new_task, name='new_task'),
    path('create/', create_task, name='create_task'),
    path('set_b/<int:id>', set_b, name='set_b'),
    path('set_c/<int:id>', set_c, name='set_c'),
    path('set_d/<int:id>', set_d, name='set_d'),

    path('v1/get_employes/<int:id>', get_employes_json, name='get_employes'),    
]
