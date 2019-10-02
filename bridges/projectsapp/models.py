from django.db import models
from productsapp.models import TechnicalSolutions


# Create your models here.
class Project(models.Model):
    name = models.CharField(verbose_name='название', max_length=256, unique=True)
    slug = models.SlugField(verbose_name='слаг', max_length=128, unique=True)
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

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class ProjectImage(models.Model):
    material = models.ForeignKey(Project, blank=True, null=True, default=None, on_delete=models.CASCADE)
    alt_desc = models.CharField(verbose_name='alt фотографии', max_length=128, blank=True)
    image = models.ImageField(verbose_name='Фотография', upload_to='products_images', blank=True)
    is_active = models.BooleanField(verbose_name='Показывать', default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.alt_desc

    class Meta:
        verbose_name = 'Фотография проекта'
        verbose_name_plural = 'Фотографии проектов'
