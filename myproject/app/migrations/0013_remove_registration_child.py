# Generated by Django 3.0.5 on 2020-12-21 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_registration_child'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='child',
        ),
    ]
