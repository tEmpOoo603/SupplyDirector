# Generated by Django 5.1 on 2024-08-26 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_events_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='period',
            field=models.IntegerField(default=None, null=True),
        ),
    ]