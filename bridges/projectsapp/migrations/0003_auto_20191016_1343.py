# Generated by Django 2.2 on 2019-10-16 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectsapp', '0002_auto_20191015_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcompany',
            name='role',
            field=models.CharField(blank=True, choices=[('проектировщик', 'проектировщик'), ('подрядчик', 'подрядчик'), ('заказчик', 'заказчик'), ('инспектор', 'инспектор'), ('технический заказчик', 'технический заказчик'), ('авторский надзор', 'авторский надзор'), ('агент', 'агент'), ('партнер', 'партнер')], max_length=24, verbose_name='роль в проекте'),
        ),
        migrations.AlterField(
            model_name='projecthastechnicalsolutions',
            name='techsol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='productsapp.TechnicalSolutions', verbose_name='Техническое решение'),
        ),
        migrations.AlterField(
            model_name='projectmanagers',
            name='role',
            field=models.CharField(blank=True, choices=[('проектировщик', 'проектировщик'), ('подрядчик', 'подрядчик'), ('заказчик', 'заказчик'), ('инспектор', 'инспектор'), ('технический надзор', 'технический надзор'), ('авторский надзор', 'авторский надзор'), ('агент', 'агент'), ('партнер', 'партнер'), ('владелец', 'владелец'), ('коммерсант', 'коммерсант'), ('ассистент', 'ассистент')], max_length=24, verbose_name='роль в проекте'),
        ),
    ]