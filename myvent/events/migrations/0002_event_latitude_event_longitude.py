# Generated by Django 5.1.2 on 2024-11-01 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='event',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
    ]