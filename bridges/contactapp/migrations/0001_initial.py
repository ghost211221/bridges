# Generated by Django 2.2 on 2019-10-13 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Имя')),
                ('phone', models.CharField(max_length=24, verbose_name='номер телефона')),
                ('email', models.CharField(max_length=24, verbose_name='email')),
                ('subject', models.CharField(max_length=96, verbose_name='Тема сообщения')),
                ('message', models.CharField(max_length=768, verbose_name='Сообщение')),
                ('add_datetime', models.DateTimeField(auto_now_add=True, verbose_name='время')),
            ],
            options={
                'verbose_name': 'Форма обратной связи',
                'verbose_name_plural': 'Формы обратной связи',
            },
        ),
    ]
