import sys
import os
import json
import django

# Add the parent directory to path to access modules from external script
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set env variable to specify Django settings from script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from app.models import *

def load_teams():
    with open('backend/raw_data/teams.json', 'r') as jsonfile:
        teams_data = json.load(jsonfile)
        
        for team_data in teams_data:
            if not Team.objects.filter(pk=team_data['id']).exists():
                Team.objects.create(
                    team_id=team_data['id'],
                    team_name=team_data['name']
                )
            else:
                print(f"Team with ID {team_data['id']} already exists.")


def load_players():
    with open('backend/raw_data/players.json', 'r') as jsonfile:
        players_data = json.load(jsonfile)
        
        for player_data in players_data:
            if not Player.objects.filter(pk=player_data['id']).exists():
                Player.objects.create(
                    player_id=player_data['id'], 
                    player_name=player_data['name']
                )
            else:
                print(f"Player with ID {player_data['id']} already exists.")

def load_games():
    with open('backend/raw_data/games.json', 'r') as jsonfile:
        games_data = json.load(jsonfile)
        
        for game_data in games_data:
            if not Game.objects.filter(pk=game_data['id']).exists():
                Game.objects.create(
                    game_id=game_data['id'], 
                    date=game_data['date'],
                    home_team_id=Team.objects.get(pk=game_data['homeTeam']['id']),
                    away_team_id=Team.objects.get(pk=game_data['awayTeam']['id'])
                )
            else:
                print(f"Game with ID {game_data['id']} already exists.")

            
def load_game_stats():
    with open('backend/raw_data/games.json', 'r') as jsonfile:
        games_data = json.load(jsonfile)
        
        stat_id_counter = 1

        for game_data in games_data:
            players = game_data['homeTeam']['players'] + game_data['awayTeam']['players']
            
            for player in players:
                if not PlayerGameStats.objects.filter(pk=stat_id_counter).exists():
                    PlayerGameStats.objects.create(
                        stat_id=stat_id_counter,
                        game_id=Game.objects.get(pk=game_data['id']),
                        player_id=Player.objects.get(pk=player['id']),
                        team_id=Team.objects.get(pk=game_data['homeTeam']['id']),
                        is_starter=player['isStarter'],
                        minutes=player['minutes'],
                        points=player['points'],
                        assists=player['assists'],
                        offensive_rebounds=player['offensiveRebounds'],
                        defensive_rebounds=player['defensiveRebounds'],
                        steals=player['steals'],
                        blocks=player['blocks'],
                        turnovers=player['turnovers'],
                        defensive_fouls=player['defensiveFouls'],
                        offensive_fouls=player['offensiveFouls'],
                        free_throws_made=player['freeThrowsMade'],
                        free_throws_attempted=player['freeThrowsAttempted'],
                        two_pointers_made=player['twoPointersMade'],
                        two_pointers_attempted=player['twoPointersAttempted'],
                        three_pointers_made=player['threePointersMade'],
                        three_pointers_attempted=player['threePointersAttempted']
                    )
                else:
                    print(f"Game Stat with ID {stat_id_counter} already exists.")
                stat_id_counter += 1

def load_game_shots():
    with open('backend/raw_data/games.json', 'r') as jsonfile:  
        games_data = json.load(jsonfile)

        stat_id_counter, shot_id_counter = 1, 1

        for game_data in games_data:
            for player in game_data['homeTeam']['players'] + game_data['awayTeam']['players']:
                for shot in player['shots']:
                    if not Shot.objects.filter(pk=shot_id_counter).exists():
                        Shot.objects.create(
                            shot_id=shot_id_counter,
                            stat_id=PlayerGameStats.objects.get(pk=stat_id_counter),
                            is_make=shot['isMake'],
                            location_x=shot['locationX'],
                            location_y=shot['locationY'],
                        )
                    else:
                        print(f"Shot Stat with ID {shot_id_counter} already exists.")
                    shot_id_counter += 1
                stat_id_counter += 1

if __name__ == '__main__':
    load_game_shots()