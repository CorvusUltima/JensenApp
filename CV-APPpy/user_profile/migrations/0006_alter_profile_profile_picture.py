# Generated by Django 3.2.9 on 2021-12-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='user-default.png', null=True, upload_to=''),
        ),
    ]
