# Generated by Django 3.2.9 on 2021-12-22 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0009_auto_20211222_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='applicant',
            field=models.ManyToManyField(blank=True, to='assignment.Applicant'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='tags',
            field=models.ManyToManyField(blank=True, to='assignment.Tag'),
        ),
    ]
