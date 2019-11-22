# Generated by Django 2.2.2 on 2019-11-22 18:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('qr_list', '0002_list_qr_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='qr_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now, verbose_name='дата создания'),
            preserve_default=False,
        ),
    ]
