# Generated by Django 3.0.8 on 2020-08-12 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20200812_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image',
            field=models.ImageField(default='default-story.jpeg', upload_to='images'),
        ),
    ]
