# Generated by Django 2.2 on 2019-10-16 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technicalsolutions',
            name='material_content',
            field=models.ManyToManyField(blank=True, related_name='materials', to='productsapp.Material'),
        ),
    ]