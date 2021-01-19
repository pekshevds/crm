from .models import Customer
from .models import Employee
from .models import Task

def get_a():
	return Task.objects.filter(task_status='A').order_by('dead_line')

def get_b():
	return Task.objects.filter(task_status='B').order_by('dead_line')

def get_c():
	return Task.objects.filter(task_status='C').order_by('dead_line')

def create_new_task(customer, from_customer, performer, from_performer, dead_line, description):
	try:
		new_task = Task.objects.create(customer=customer, 
										from_customer=from_customer, 
										performer=performer, 
										from_performer=from_performer,
										dead_line=dead_line, 
										description=description)
	except:
		return False
	return True