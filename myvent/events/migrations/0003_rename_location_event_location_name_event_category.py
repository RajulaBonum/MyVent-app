# Generated by Django 5.1.2 on 2024-11-01 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_latitude_event_longitude'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='location',
            new_name='location_name',
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('conference', 'Conference'), ('workshop', 'Workshop'), ('meetup', 'Meetup'), ('webinar', 'Webinar')], default='conference', max_length=50),
        ),
    ]