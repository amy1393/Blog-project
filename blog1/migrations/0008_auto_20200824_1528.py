# Generated by Django 3.1 on 2020-08-24 09:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0007_auto_20200821_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='commented_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
