# Generated by Django 3.0.8 on 2020-08-11 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20200811_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['category'],
            },
        ),
        migrations.AddField(
            model_name='newsstory',
            name='categories',
            field=models.ManyToManyField(to='news.StoryCategory'),
        ),
    ]
