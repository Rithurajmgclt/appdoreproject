# Generated by Django 3.0.5 on 2020-12-17 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20201217_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Title'),
        ),
    ]
