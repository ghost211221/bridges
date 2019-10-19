# Generated by Django 2.2.4 on 2019-10-19 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcompany',
            name='company',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='authapp.Company', verbose_name='Выберите компанию'),
        ),
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
            name='project',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='managers', to='projectsapp.Project', verbose_name='проект'),
        ),
        migrations.AlterField(
            model_name='projectmanagers',
            name='role',
            field=models.CharField(blank=True, choices=[('проектировщик', 'проектировщик'), ('подрядчик', 'подрядчик'), ('заказчик', 'заказчик'), ('инспектор', 'инспектор'), ('технический надзор', 'технический надзор'), ('авторский надзор', 'авторский надзор'), ('агент', 'агент'), ('партнер', 'партнер'), ('владелец', 'владелец'), ('коммерсант', 'коммерсант'), ('ассистент', 'ассистент')], max_length=24, verbose_name='роль в проекте'),
        ),
    ]