# -*- coding: utf-8 -*-
"""Contains models related to stats"""
from django.db import models

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=255)

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=255)

class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    date = models.DateField()
    home_team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_games')
    away_team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_games')

class PlayerGameStats(models.Model):
    stat_id = models.AutoField(primary_key=True)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    is_starter = models.BooleanField()
    minutes = models.IntegerField()
    points = models.IntegerField()
    assists = models.IntegerField()
    offensive_rebounds = models.IntegerField()
    defensive_rebounds = models.IntegerField()
    steals = models.IntegerField()
    blocks = models.IntegerField()
    turnovers = models.IntegerField()
    defensive_fouls = models.IntegerField()
    offensive_fouls = models.IntegerField()
    free_throws_made = models.IntegerField()
    free_throws_attempted = models.IntegerField()
    two_pointers_made = models.IntegerField()
    two_pointers_attempted = models.IntegerField()
    three_pointers_made = models.IntegerField()
    three_pointers_attempted = models.IntegerField()

class Shot(models.Model):
    shot_id = models.AutoField(primary_key=True)
    stat_id = models.ForeignKey(PlayerGameStats, on_delete=models.CASCADE)
    is_make = models.BooleanField()
    location_x = models.FloatField()
    location_y = models.FloatField()