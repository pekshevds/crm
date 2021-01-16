from django.contrib import admin

from .models import Person
from .models import Customer
from .models import Employee
from .models import Position

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
	list_display = (		
		'first_name',
		'middle_name',
		'last_name',
		'birthdate',
		'sex',
	)
		
	list_filter = ( 'sex', )


class EmployeeInline(admin.TabularInline):
    model = Employee    
    extra = 0


class CustomerAdmin(admin.ModelAdmin):
	list_display = (		
		'name',
		'inn',
		'kpp',		
	)
		
	search_fields = ('name', 'inn',)
	list_filter = ( 'kpp', )
	inlines = [EmployeeInline, ]
	

admin.site.register(Person, PersonAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Position)

