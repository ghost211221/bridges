# Generated by Django 2.2.4 on 2019-09-29 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0018_auto_20190929_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='technicalsolutions',
            name='alt_desc',
            field=models.CharField(blank=True, max_length=128, verbose_name='alt фотографии'),
        ),
    ]
