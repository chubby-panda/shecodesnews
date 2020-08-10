# Generated by Django 3.0.8 on 2020-08-10 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_customuser_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(default="This user hasn't written a bio yet!", max_length=1000),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_img',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
    ]
