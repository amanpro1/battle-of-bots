# Generated by Django 2.0.2 on 2020-01-19 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0020_auto_20200119_0723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='defence_list',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='weapon_list',
        ),
    ]
