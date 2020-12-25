# Generated by Django 3.0.5 on 2020-12-17 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201217_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='registration',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.title'),
        ),
    ]
