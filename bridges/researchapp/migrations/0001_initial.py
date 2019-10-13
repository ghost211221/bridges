# Generated by Django 2.2 on 2019-10-13 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authapp', '0001_initial'),
        ('productsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='название категории')),
                ('comment', models.TextField(blank=True, verbose_name='комментарии')),
            ],
            options={
                'verbose_name': 'Категория документа',
                'verbose_name_plural': 'Категории документов',
            },
        ),
        migrations.CreateModel(
            name='FileStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_desc', models.CharField(blank=True, max_length=128, verbose_name='название файла')),
                ('file', models.FileField(blank=True, upload_to='research_files', verbose_name='файл')),
                ('is_active', models.BooleanField(default=True, verbose_name='Показывать')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Хранилище файлов',
                'verbose_name_plural': 'Хранилище файлов',
            },
        ),
        migrations.CreateModel(
            name='SubjectOfStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='предмет исследования')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Предмет исследование',
                'verbose_name_plural': 'Предметы исследований',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='название документа')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='автор документа')),
                ('company', models.ManyToManyField(blank=True, to='authapp.Company', verbose_name='компания выпустившая документ')),
                ('file', models.ManyToManyField(blank=True, to='researchapp.FileStorage')),
                ('subject', models.ManyToManyField(blank=True, to='researchapp.SubjectOfStudy', verbose_name='предмет исседования')),
                ('techsol', models.ManyToManyField(to='productsapp.TechnicalSolutions', verbose_name='техническое решение')),
                ('type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='researchapp.DocumentCategory', verbose_name='категория документа')),
            ],
            options={
                'verbose_name': 'Документ и исследование',
                'verbose_name_plural': 'Документы и исследования',
            },
        ),
    ]
