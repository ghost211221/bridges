# Generated by Django 2.2 on 2019-11-04 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicesapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField(default=0, verbose_name='номер заказа пользователя')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='обновлен')),
                ('status', models.CharField(choices=[('PRD', 'обрабатывается'), ('RDY', 'обработан'), ('CNC', 'отменен')], default='PRD', max_length=3, verbose_name='статус')),
                ('is_active', models.BooleanField(default=True, verbose_name='активен')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productsapp.TechnicalSolutions', verbose_name='техническое решение')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicesapp.Service', verbose_name='услуга')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'ordering': ('-created',),
                'permissions': (('orders_view', 'Можно видеть все заказы'),),
            },
        ),
    ]
