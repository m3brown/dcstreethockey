# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('ref1', models.CharField(max_length=50)),
                ('ref2', models.CharField(max_length=50)),
                ('notes', models.CharField(max_length=500)),
                ('is_regularseasion', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.PositiveSmallIntegerField()),
                ('win', models.PositiveSmallIntegerField()),
                ('loss', models.PositiveSmallIntegerField()),
                ('tie', models.PositiveSmallIntegerField()),
                ('goals_for', models.PositiveSmallIntegerField()),
                ('goals_against', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('user_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Refs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('plaer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position1', models.CharField(max_length=30)),
                ('position2', models.CharField(max_length=30)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_champion', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assists', models.PositiveSmallIntegerField()),
                ('goals_against', models.PositiveSmallIntegerField()),
                ('en', models.PositiveSmallIntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.Games')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.Player')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.Season')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=30)),
                ('team_color', models.CharField(max_length=30)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='season',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.Team'),
        ),
        migrations.AddField(
            model_name='roster',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.Team'),
        ),
        migrations.AddField(
            model_name='league',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.Season'),
        ),
        migrations.AddField(
            model_name='league',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.Team'),
        ),
        migrations.AddField(
            model_name='games',
            name='awayteam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='leagues.Team'),
        ),
        migrations.AddField(
            model_name='games',
            name='hometeam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='leagues.Team'),
        ),
        migrations.AddField(
            model_name='games',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.Season'),
        ),
    ]
