# Generated by Django 3.2.9 on 2022-01-20 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainPages', '0003_alter_room_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='topic',
            new_name='name',
        ),
    ]
