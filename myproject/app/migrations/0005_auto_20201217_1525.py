# Generated by Django 3.0.5 on 2020-12-17 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201217_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='Boss',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Title'),
        ),
    ]
