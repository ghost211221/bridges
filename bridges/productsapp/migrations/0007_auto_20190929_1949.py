# Generated by Django 2.2.4 on 2019-09-29 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0006_auto_20190929_1937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='materialimage',
            options={'verbose_name': 'Фотография материаллов', 'verbose_name_plural': 'Фотографии материаллов'},
        ),
        migrations.RemoveField(
            model_name='material',
            name='image',
        ),
    ]
