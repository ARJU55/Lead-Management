# Generated by Django 5.0 on 2024-01-17 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0008_batches_formatted_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batches',
            name='formatted_name',
        ),
    ]
