# Generated by Django 3.2.15 on 2022-09-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_events_start_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='start_project',
            field=models.BooleanField(auto_created=True, default=False, verbose_name='Начало голосования'),
        ),
    ]