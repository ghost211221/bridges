# Generated by Django 2.2.5 on 2019-10-09 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20191008_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='authapp.CategoryCompany', verbose_name='Категория компании*'),
        ),
    ]
