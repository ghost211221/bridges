from django.db import models

# Create your models here.
from authapp.models import Company, Users
from productsapp.models import TechnicalSolutions


class SubjectOfStudy(models.Model):
    """
    Предмет исследования, например "водонепроницаемость", "адгезия" и т.д.
    """
    name = models.CharField(verbose_name='предмет исследования', max_length=28, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исследование'
        verbose_name_plural = 'Исследования'


class Research(models.Model):
    """
    Модель научно-исследовательской работы по изучению каких-либо факторов или свойств
    """
    name = models.CharField(verbose_name='название исследования', max_length=128, unique=True)
    subject = models.ManyToManyField(SubjectOfStudy)
    researcher = models.ManyToManyField(Company)
    scientist = models.ManyToManyField(Users)
    techsol = models.ManyToManyField(TechnicalSolutions)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    comments = models.TextField(verbose_name='описание материала', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исследование'
        verbose_name_plural = 'Исследования'


class ResearchFile(models.Model):
    """
    Файлы или документы подгружаемые к модели Research
    """
    material = models.ForeignKey(Research, blank=True, null=True, default=None, on_delete=models.CASCADE)
    alt_desc = models.CharField(verbose_name='alt файла', max_length=128, blank=True)
    file = models.ImageField(verbose_name='файл', upload_to='research_files', blank=True)
    is_active = models.BooleanField(verbose_name='Показывать', default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.alt_desc

    class Meta:
        verbose_name = 'Документ исследования'
        verbose_name_plural = 'Документы исследования'
