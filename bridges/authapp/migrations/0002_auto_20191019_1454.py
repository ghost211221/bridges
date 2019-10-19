# Generated by Django 2.2.4 on 2019-10-19 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyusers',
            name='works',
            field=models.BooleanField(default=True, null=True, verbose_name='Работает в компании'),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(blank=True, choices=[(None, 'не указан'), ('male', 'муж'), ('female', 'жен')], max_length=6, null=True, verbose_name='Пол'),
        ),
    ]