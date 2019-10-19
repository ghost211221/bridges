# Generated by Django 2.2 on 2019-10-14 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='название')),
                ('slug', models.SlugField(max_length=128, unique=True, verbose_name='слаг')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('image', models.ImageField(blank=True, upload_to='аватарка')),
                ('status', models.CharField(blank=True, choices=[('разработка', 'разработка'), ('экспертиза', 'экспертиза'), ('аукцион', 'аукцион'), ('строительство', 'строительство'), ('сдача', 'сдача'), ('выплата', 'выплата'), ('завершен', 'завершен')], max_length=24, verbose_name='статус')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='обновлен')),
                ('city', models.CharField(blank=True, max_length=512, null=True, verbose_name='город')),
                ('address', models.CharField(blank=True, max_length=512, null=True, verbose_name='адрес')),
                ('coordinate', models.CharField(blank=True, max_length=34, null=True, verbose_name='координаты')),
                ('map_mark', models.SlugField(blank=True, max_length=128, verbose_name='id метки на карте')),
                ('text_for_map', models.TextField(blank=True, max_length=240, null=True, verbose_name='текст для метки')),
                ('is_active', models.BooleanField(default=False, verbose_name='активен')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ('-updated',),
            },
        ),
        migrations.CreateModel(
            name='ProjectManagers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, choices=[('проектировщик', 'проектировщик'), ('подрядчик', 'подрядчик'), ('заказчик', 'заказчик'), ('инспектор', 'инспектор'), ('агент', 'агент'), ('партнер', 'партнер'), ('владелец', 'владелец'), ('коммерсант', 'коммерсант'), ('ассистент', 'ассистент')], max_length=24, verbose_name='роль в проекте')),
                ('description', models.TextField(blank=True, verbose_name='комментарий')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('manager', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Участники')),
                ('project', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='managers', to='projectsapp.Project')),
            ],
            options={
                'verbose_name': 'Участник проекта',
                'verbose_name_plural': 'Участники проекта',
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_desc', models.CharField(blank=True, max_length=128, verbose_name='alt фотографии')),
                ('image', models.ImageField(blank=True, upload_to='products_images', verbose_name='Фотография')),
                ('is_active', models.BooleanField(default=True, verbose_name='Показывать')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='projectsapp.Project')),
            ],
            options={
                'verbose_name': 'Фотография проекта',
                'verbose_name_plural': 'Фотографии проектов',
            },
        ),
        migrations.CreateModel(
            name='ProjectHasTechnicalSolutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='название конструкции или участка')),
                ('value', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='Объем работ')),
                ('is_active', models.BooleanField(default=True, verbose_name='Показывать')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='projectsapp.Project', verbose_name='Строительный проект')),
                ('techsol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productsapp.TechnicalSolutions', verbose_name='Техническое решение')),
            ],
            options={
                'verbose_name': 'Тех решение проекта',
                'verbose_name_plural': 'Тех решения проекта',
            },
        ),
        migrations.CreateModel(
            name='ProjectCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, choices=[('проектировщик', 'проектировщик'), ('подрядчик', 'подрядчик'), ('заказчик', 'заказчик'), ('инспектор', 'инспектор'), ('агент', 'агент'), ('партнер', 'партнер')], max_length=24, verbose_name='роль в проекте')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='authapp.Company', verbose_name='Компании на проекте')),
                ('project', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='projectsapp.Project')),
            ],
            options={
                'verbose_name': 'Компания - участник проекта',
                'verbose_name_plural': 'Компания - участник проекта',
            },
        ),
    ]
