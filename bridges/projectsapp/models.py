from django.db import models
from productsapp.models import TechnicalSolutions


# Create your models here.
class Project(models.Model):
    name = models.CharField(verbose_name='название', max_length=256, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    image = models.ImageField(upload_to='projects_images', blank=True)
    finishDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    city = models.CharField(verbose_name='город', max_length=512, blank=True, null=True)
    address = models.CharField(verbose_name='адрес', max_length=512, blank=True, null=True)
    latitude = models.FloatField(verbose_name='широта', null=True)
    longitude = models.FloatField(verbose_name='долгота', null=True)
    contractor = models.CharField(verbose_name='подрядчик', max_length=512, blank=True, null=True)
    customer = models.CharField(verbose_name='заказчик', max_length=512, blank=True, null=True)
    designer = models.CharField(verbose_name='проектировщик', max_length=512, blank=True, null=True)
    technical_solutions = models.ManyToManyField(TechnicalSolutions)

    def __str__(self):
        return f"{self.name} ({self.city})"
