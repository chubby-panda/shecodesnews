# Generated by Django 3.0.8 on 2020-08-12 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_auto_20200812_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]