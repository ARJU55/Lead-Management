# Generated by Django 5.0 on 2024-01-08 06:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=200)),
                ('branch_code', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('pincode', models.IntegerField()),
                ('mobile_number', models.CharField(max_length=15)),
                ('email_id', models.EmailField(max_length=254)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_app.district')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_app.state')),
            ],
        ),
    ]
