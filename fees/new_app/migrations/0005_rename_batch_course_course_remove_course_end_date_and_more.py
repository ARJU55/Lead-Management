# Generated by Django 5.0 on 2024-01-11 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0004_course_followupstatu_qualification_syllabus_branches_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Batch',
            new_name='Course',
        ),
        migrations.RemoveField(
            model_name='course',
            name='End_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='Start_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='Trainer_name',
        ),
    ]