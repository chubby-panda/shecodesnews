# Generated by Django 3.0.8 on 2020-08-12 09:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0020_auto_20200812_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='mod_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsstory',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 12, 9, 19, 56, 909865, tzinfo=utc)),
        ),
    ]
