from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    position = models.CharField(max_length=200, verbose_name='Должность')
    hired_at = models.DateField()
    salary = models.PositiveIntegerField()
    chief = models.PositiveIntegerField(blank=True, verbose_name='ID начальника')
