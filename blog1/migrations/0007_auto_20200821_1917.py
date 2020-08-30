# Generated by Django 3.1 on 2020-08-21 13:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0006_auto_20200821_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 21, 13, 47, 11, 940882, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 21, 13, 47, 11, 939886, tzinfo=utc)),
        ),
    ]