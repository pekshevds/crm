from django.db import models

# Create your models here.

DEFAULT_SEX = 'M'
SEX = (
	(DEFAULT_SEX, 'Мужской'),	
	('F', 'Женский'),
	)

class Person(models.Model):

	""" Физические лица """
	first_name = models.CharField(max_length=255, verbose_name="Имя")
	middle_name = models.CharField(max_length=255, verbose_name="Отчество", null=True, blank=True)
	last_name = models.CharField(max_length=1024, verbose_name="Фамилия", null=True, blank=True)
	birthdate = models.DateField(verbose_name="Дата рождения", null=True, blank=True)
	sex = models.CharField(max_length=1, verbose_name="Пол", 
										choices=SEX, default=DEFAULT_SEX, null=True, blank=True)

	email = models.EmailField(max_length=254, verbose_name="Адрес e-mail", null=True, blank=True)

	address1 = models.CharField(max_length=1024, verbose_name="Адрес по прописке", null=True, blank=True)
	address2 = models.CharField(max_length=1024, verbose_name="Адрес проживания", null=True, blank=True)

	phone1 = models.CharField(max_length=25, verbose_name="Телефон", null=True, blank=True)
	phone2 = models.CharField(max_length=25, verbose_name="Телефон", null=True, blank=True)

	description = models.TextField(verbose_name="Краткая характеристика", null=True, blank=True)


	def __str__(self):
		return f'{self.first_name} {self.last_name}'


class Customer(models.Model):
	
	""" Заказчики """
	name = models.CharField(max_length=255, verbose_name="Наименование")
	full_name = models.CharField(max_length=1024, verbose_name="Полное наименование", null=True, blank=True)
	
	inn = models.CharField(max_length=12, verbose_name="ИНН", null=True, blank=True)
	kpp = models.CharField(max_length=9, verbose_name="КПП", null=True, blank=True)

	email = models.EmailField(max_length=254, verbose_name="Адрес e-mail", null=True, blank=True)

	address1 = models.CharField(max_length=1024, verbose_name="Адрес юридический", null=True, blank=True)
	address2 = models.CharField(max_length=1024, verbose_name="Адрес фактический", null=True, blank=True)

	phone1 = models.CharField(max_length=25, verbose_name="Телефон", null=True, blank=True)
	phone2 = models.CharField(max_length=25, verbose_name="Телефон", null=True, blank=True)

	description = models.TextField(verbose_name="Краткая характеристика", null=True, blank=True)

	person = models.ForeignKey(Person, verbose_name="Физическое лицо", on_delete=models.PROTECT, null=True, blank=True)

	def __str__(self):
		return f'{self.name}'


class Position(models.Model):
	
	""" Должности """	
	name = models.CharField(max_length=1024, verbose_name="Наименование")	

	def __str__(self):
		return f'{self.name}'


class Employee(models.Model):

	""" Сотрудники заказчиков """
	customer = models.ForeignKey(Customer, verbose_name="Заказчик", on_delete=models.PROTECT)

	name = models.CharField(max_length=1024, verbose_name="Наименование")
	position = models.ForeignKey(Position, verbose_name="Должность", on_delete=models.PROTECT, null=True, blank=True)
		
	email = models.EmailField(max_length=254, verbose_name="Адрес e-mail", null=True, blank=True)

	address1 = models.CharField(max_length=1024, verbose_name="Адрес юридический", null=True, blank=True)
	address2 = models.CharField(max_length=1024, verbose_name="Адрес фактический", null=True, blank=True)

	phone1 = models.CharField(max_length=25, verbose_name="Телефон", null=True, blank=True)
	phone2 = models.CharField(max_length=25, verbose_name="Телефон", null=True, blank=True)

	person = models.ForeignKey(Person, verbose_name="Физическое лицо", on_delete=models.PROTECT, null=True, blank=True)

	def __str__(self):
		return f'{self.name}'