# Generated by Django 3.0.5 on 2020-12-17 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201217_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='Boss',
            new_name='boss',
        ),
        migrations.AlterField(
            model_name='registration',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Title'),
        ),
    ]