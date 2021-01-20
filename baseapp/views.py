from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from django.http import JsonResponse

from .models import Customer
from .models import Employee
from .models import Task

from .core import get_a
from .core import get_b
from .core import get_c
from .core import create_new_task
from .core import get_employes

from datetime import datetime

import json
# Create your views here.
def show_grid(request):

	context = {
		'a': get_a(),
		'b': get_b(),
		'c': get_c(),
	}
	return render(request, 'baseapp/grid.html', context)


def show_task(request, id):

	context = {
		'task': Task.objects.get(id=id)
	}
	return render(request, 'baseapp/task.html', context)


def new_task(request):
	context = {
		'customers': Customer.objects.all(),
		'employes': Employee.objects.all(),
	}
	return render(request, 'baseapp/new_task.html', context)


def create_task(request):
	
	customer_id = int(request.POST.get('customer', '0'))
	from_customer_id = int(request.POST.get('from_customer', '0'))
	
	performer_id = int(request.POST.get('performer', '0'))
	from_performer_id = int(request.POST.get('from_performer', '0'))
		
	dead_line = datetime.strptime(request.POST.get('dead_line', ''), '%Y-%m-%d')

	description = request.POST.get('description', '')


	customer = Customer.objects.filter(id=customer_id).first()
	from_customer = Employee.objects.filter(id=from_customer_id).first()

	performer = Customer.objects.filter(id=performer_id).first()
	from_performer = Employee.objects.filter(id=from_performer_id).first()

	if create_new_task(customer=customer, 
		from_customer=from_performer, 
		performer=performer, 
		from_performer=from_performer, 
		dead_line=dead_line, 
		description=description):

		return redirect('show_grid')
	return redirect(request.META['HTTP_REFERER'])


def set_b(request, id):

	task = Task.objects.get(id=id)
	task.task_status = 'B'
	task.save()
	return redirect('show_grid')


def set_c(request, id):

	task = Task.objects.get(id=id)
	task.task_status = 'C'
	task.save()
	return redirect('show_grid')


def set_d(request, id):

	task = Task.objects.get(id=id)
	task.task_status = 'D'
	task.save()
	return redirect('show_grid')


def get_employes_json(request, id):
	customer = Customer.objects.filter(id=id).first()
	employes = get_employes(customer).values()

	data = list(employes)
	return JsonResponse(data, safe=False)