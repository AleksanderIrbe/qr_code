# Generated by Django 2.2.2 on 2019-11-22 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_list', '0004_auto_20191122_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='qr_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='дата создания'),
        ),
    ]
