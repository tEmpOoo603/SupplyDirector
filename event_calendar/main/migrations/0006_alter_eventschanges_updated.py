# Generated by Django 5.1 on 2024-08-26 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_eventschanges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventschanges',
            name='updated',
            field=models.DateTimeField(),
        ),
    ]
