# Generated by Django 5.0 on 2024-01-22 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_students_college_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='college_Name',
            field=models.CharField(default='Default_college_Name', max_length=100),
        ),
    ]