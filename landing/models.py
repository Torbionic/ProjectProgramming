from django.db import models
from django.utils import timezone


class CEO(models.Model):
    name = models.CharField('Имя', max_length=100, default = "")
    corparation = models.CharField('Организация', max_length=100, default = "")
    annotation = models.TextField('Аннотация', default = "")
    moneys = models.TextField('Маржа', default = "")
    date_create = models.DateTimeField(default=timezone.now)

