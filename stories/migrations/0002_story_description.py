# Generated by Django 4.2.6 on 2024-01-25 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
