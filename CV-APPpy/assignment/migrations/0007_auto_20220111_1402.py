# Generated by Django 3.2.9 on 2022-01-11 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0006_auto_20211229_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assignment.assignment'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='applicant',
            field=models.ManyToManyField(blank=True, null=True, to='assignment.Applicant'),
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='tags',
        ),
        migrations.AddField(
            model_name='assignment',
            name='tags',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
