# Generated by Django 2.2.4 on 2019-09-29 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0003_auto_20190929_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialimage',
            name='image',
            field=models.ImageField(blank=True, upload_to='products_images', verbose_name='Фотография'),
        ),
    ]
