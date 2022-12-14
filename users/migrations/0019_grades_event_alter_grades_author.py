# Generated by Django 4.1 on 2022-09-23 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20220918_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='grades',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.events', verbose_name='Мероприятие, в котором оценённый проект'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grades',
            name='author',
            field=models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Оценивший жюри'),
        ),
    ]
