# Generated by Django 2.1.2 on 2018-11-20 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0003_auto_20181118_2340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'get_latest_by': 'created_at'},
        ),
    ]