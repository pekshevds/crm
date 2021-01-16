# Generated by Django 3.1.4 on 2021-01-16 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0005_auto_20210116_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('full_name', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Полное наименование')),
                ('inn', models.CharField(max_length=12, null=True, verbose_name='ИНН')),
                ('kpp', models.CharField(max_length=9, null=True, verbose_name='КПП')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Адрес e-mail')),
                ('address1', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Адрес юридический')),
                ('address2', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Адрес фактический')),
                ('phone1', models.CharField(blank=True, max_length=25, null=True, verbose_name='Телефон')),
                ('phone2', models.CharField(blank=True, max_length=25, null=True, verbose_name='Телефон')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Краткая характеристика')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='baseapp.person', verbose_name='Физическое лицо')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, verbose_name='Наименование')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Адрес e-mail')),
                ('address1', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Адрес юридический')),
                ('address2', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Адрес фактический')),
                ('phone1', models.CharField(blank=True, max_length=25, null=True, verbose_name='Телефон')),
                ('phone2', models.CharField(blank=True, max_length=25, null=True, verbose_name='Телефон')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='baseapp.customer', verbose_name='Заказчик')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='baseapp.person', verbose_name='Физическое лицо')),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='baseapp.position', verbose_name='Должность')),
            ],
        ),
    ]