# Generated by Django 4.2.4 on 2023-08-18 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.AutoField(primary_key=True, serialize=False)),
                ('player_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerGameStats',
            fields=[
                ('stat_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_starter', models.BooleanField()),
                ('minutes', models.IntegerField()),
                ('points', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('offensive_rebounds', models.IntegerField()),
                ('defensive_rebounds', models.IntegerField()),
                ('steals', models.IntegerField()),
                ('blocks', models.IntegerField()),
                ('turnovers', models.IntegerField()),
                ('defensive_fouls', models.IntegerField()),
                ('offensive_fouls', models.IntegerField()),
                ('free_throws_made', models.IntegerField()),
                ('free_throws_attempted', models.IntegerField()),
                ('two_pointers_made', models.IntegerField()),
                ('two_pointers_attempted', models.IntegerField()),
                ('three_pointers_made', models.IntegerField()),
                ('three_pointers_attempted', models.IntegerField()),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.game')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.player')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Shot',
            fields=[
                ('shot_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_make', models.BooleanField()),
                ('location_x', models.FloatField()),
                ('location_y', models.FloatField()),
                ('stat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.playergamestats')),
            ],
        ),
        migrations.AddField(
            model_name='playergamestats',
            name='team_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.team'),
        ),
        migrations.AddField(
            model_name='game',
            name='away_team_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_games', to='app.team'),
        ),
        migrations.AddField(
            model_name='game',
            name='home_team_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_games', to='app.team'),
        ),
    ]