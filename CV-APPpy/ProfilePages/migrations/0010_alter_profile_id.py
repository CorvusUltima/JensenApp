# Generated by Django 3.2.9 on 2021-12-22 09:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ProfilePages', '0009_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]