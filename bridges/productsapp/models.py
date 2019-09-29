from django.db import models


class MaterialCategory(models.Model):
    name = models.CharField(verbose_name='категория материалов', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name


class MeasureTypes(models.Model):
    name = models.CharField(verbose_name='единица измерения', max_length=28, unique=True)
    shortcut = models.CharField(verbose_name='ед.изм.', max_length=10, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.shortcut


# class Characteristic(models.Model):
#     name = models.CharField(verbose_name='название характеристики', max_length=28, unique=True)
#     measure = models.ForeignKey(MeasureTypes, on_delete=models.CASCADE)
#     description = models.TextField(verbose_name='описание', blank=True)
#
#     def __str__(self):
#         return f"{self.name} {self.measure}"


class Material(models.Model):
    name = models.CharField(verbose_name='название материала', max_length=128)
    category = models.ForeignKey(MaterialCategory, on_delete=models.CASCADE)
    measure = models.ForeignKey(MeasureTypes, on_delete=models.CASCADE)
    # characteristics = models.ManyToManyField(Characteristic)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание материала', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание материала', blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class TechnicalSolutions(models.Model):
    name = models.CharField(verbose_name='название материала', max_length=128)
    material_content = models.ManyToManyField(Material)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание материала', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание материала', blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.name
