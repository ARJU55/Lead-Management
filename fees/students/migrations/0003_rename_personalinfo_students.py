# Generated by Django 5.0 on 2024-01-18 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_personalinfo_delete_pesonalinfo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PersonalInfo',
            new_name='Students',
        ),
    ]
