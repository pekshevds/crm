from django.shortcuts import render
from .models import Task
# Create your views here.
def show_grid(request):

	context = {
		'a': get_a(),
		'b': get_b(),
		'c': get_c(),
	}
	return render(request, 'baseapp/grid.html', context)

def show_item(request, id):

	context = {
		'task': Task.objects.get(id=id)
	}
	return render(request, 'baseapp/item.html', context)


def get_a():
	return Task.objects.filter(task_status='A')

def get_b():
	return Task.objects.filter(task_status='B')

def get_c():
	return Task.objects.filter(task_status='C')