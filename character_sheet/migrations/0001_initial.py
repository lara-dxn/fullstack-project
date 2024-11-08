# Generated by Django 4.2.15 on 2024-11-03 02:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isPlayer', models.BooleanField(default=False)),
                ('isGM', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hp', models.IntegerField()),
                ('character_class', models.CharField(max_length=100)),
                ('blinded', models.BooleanField(default=False)),
                ('charmed', models.BooleanField(default=False)),
                ('deafened', models.BooleanField(default=False)),
                ('frightened', models.BooleanField(default=False)),
                ('grappled', models.BooleanField(default=False)),
                ('incapacitated', models.BooleanField(default=False)),
                ('invisible', models.BooleanField(default=False)),
                ('paralyzed', models.BooleanField(default=False)),
                ('petrified', models.BooleanField(default=False)),
                ('poisoned', models.BooleanField(default=False)),
                ('prone', models.BooleanField(default=False)),
                ('restrained', models.BooleanField(default=False)),
                ('stunned', models.BooleanField(default=False)),
                ('unconscious', models.BooleanField(default=False)),
                ('exhaustion', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character_sheet.userprofile')),
            ],
        ),
    ]
