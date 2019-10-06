# Generated by Django 2.2 on 2019-10-04 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchapp', '0004_auto_20191004_1301'),
    ]

    operations = [
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
                'verbose_name': 'Документ исследования',
                'verbose_name_plural': 'Документы исследования',
            },
        ),
        migrations.RemoveField(
            model_name='researchfile',
            name='research',
        ),
        migrations.DeleteModel(
            name='Research',
        ),
        migrations.DeleteModel(
            name='ResearchFile',
        ),
    ]
