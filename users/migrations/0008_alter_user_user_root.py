# Generated by Django 3.2.15 on 2022-09-14 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_user_root'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_root',
            field=models.BooleanField(auto_created=True, verbose_name='Админ ли?'),
        ),
    ]