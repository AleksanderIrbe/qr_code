# Generated by Django 2.2.2 on 2019-11-23 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_list', '0006_auto_20191122_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='слаг'),
        ),
    ]
