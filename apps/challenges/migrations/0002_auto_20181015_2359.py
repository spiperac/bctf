# Generated by Django 2.1.2 on 2018-10-15 23:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='solved',
            field=models.ManyToManyField(null=True, related_name='accounts', to=settings.AUTH_USER_MODEL),
        ),
    ]