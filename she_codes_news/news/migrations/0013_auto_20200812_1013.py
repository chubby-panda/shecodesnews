# Generated by Django 3.0.8 on 2020-08-12 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20200812_1008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category'], 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='newsstory',
            options={'verbose_name_plural': 'news stories'},
        ),
    ]
