from django.db import models
from productsapp.models import TechnicalSolutions



# Create your models here.
class Project(models.Model):
    name = models.CharField(verbose_name='название', max_length=256, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    image = models.ImageField(upload_to='projects_images', blank=True)
    finishDate = models.DateTimeField()
    techDes = models.ForeignKey(TechnicalSolutions, on_delete=models.CASCADE)
    address = models.CharField(max_length=512, blank=True, null=True)
    executor = models.CharField(max_length=512, blank=True, null=True)
    orderer = models.CharField(max_length=512, blank=True, null=True)
    designer = models.CharField(max_length=512, blank=True, null=True)


