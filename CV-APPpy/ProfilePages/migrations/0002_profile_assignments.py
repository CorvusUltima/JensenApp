# Generated by Django 2.2.24 on 2021-12-23 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
        ('ProfilePages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='assignments',
            field=models.ManyToManyField(blank=True, to='assignment.Assignment'),
        ),
    ]