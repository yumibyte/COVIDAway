# Generated by Django 3.0.7 on 2020-09-06 05:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200906_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 9, 6, 5, 6, 51, 172280, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
