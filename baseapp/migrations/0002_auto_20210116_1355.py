# Generated by Django 3.1.4 on 2021-01-16 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthdate',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Мужской'), ('F', 'Женский')], default='M', max_length=1, null=True, verbose_name='Пол'),
        ),
    ]