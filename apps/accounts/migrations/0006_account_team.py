# Generated by Django 2.1.2 on 2018-11-19 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
        ('accounts', '0005_account_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='teams.Team'),
        ),
    ]