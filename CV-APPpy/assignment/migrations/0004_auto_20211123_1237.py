# Generated by Django 2.2.24 on 2021-11-23 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0003_auto_20211123_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='applicant',
            field=models.ManyToManyField(blank=True, null=True, to='assignment.Applicant'),
        ),
    ]
