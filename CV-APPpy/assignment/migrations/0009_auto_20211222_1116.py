# Generated by Django 3.2.9 on 2021-12-22 10:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0008_auto_20211210_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='slug',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
