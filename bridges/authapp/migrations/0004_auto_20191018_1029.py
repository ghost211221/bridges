# Generated by Django 2.2 on 2019-10-18 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_companyusers_works'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyusers',
            name='works',
            field=models.BooleanField(default=True, null=True, verbose_name='Работает в компании'),
        ),
    ]
