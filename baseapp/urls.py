from django.urls import path
from .views import show_grid
from .views import show_item

urlpatterns = [
    path('', show_grid, name='show_grid'),
    path('task/<int:id>', show_item, name='show_item'),
]
