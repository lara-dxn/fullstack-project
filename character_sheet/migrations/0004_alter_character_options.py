# Generated by Django 4.2.15 on 2024-11-04 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('character_sheet', '0003_character_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='character',
            options={'ordering': ['name']},
        ),
    ]
