# Generated by Django 3.1 on 2020-08-21 11:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0002_auto_20200821_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 8, 21, 11, 59, 3, 587659, tzinfo=utc)),
        ),
    ]