# Generated by Django 3.2.9 on 2021-12-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfilePages', '0003_alter_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(max_length=100),
        ),
    ]