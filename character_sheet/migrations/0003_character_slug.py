# Generated by Django 4.2.15 on 2024-11-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character_sheet', '0002_character_character_race_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True),
        ),
    ]
