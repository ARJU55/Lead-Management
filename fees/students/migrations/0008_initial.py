# Generated by Django 5.0 on 2024-01-22 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0007_delete_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('trans', 'Transgender'), ('others', 'Others')], default='null', max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('alternative_email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('alternative_address', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('mobile', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=100)),
                ('pincodes', models.CharField(max_length=7)),
                ('whatsapp', models.CharField(max_length=20, null=True)),
                ('college_name', models.CharField(default='Default College Name', max_length=100)),
                ('year_of_pass', models.IntegerField()),
                ('roll_no', models.CharField(max_length=15)),
                ('registration_number', models.CharField(max_length=15)),
            ],
        ),
    ]