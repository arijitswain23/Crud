# Generated by Django 4.2.6 on 2023-12-15 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='hire_date',
        ),
    ]
