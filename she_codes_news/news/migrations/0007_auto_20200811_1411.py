# Generated by Django 3.0.8 on 2020-08-11 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_newsstory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
