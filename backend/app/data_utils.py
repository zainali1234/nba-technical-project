from app.models import *

def get_player_data(player_id):
    try:
        player = Player.objects.get(pk=player_id)
        player_games = PlayerGameStats.objects.filter(player_id=player_id)

        player_data = {
            'name': player.player_name, 
            'games': [{
                'date': Game.objects.get(pk=player_game.game_id_id).date,
                'isStarter': player_game.is_starter,
                'minutes': player_game.minutes,
                'points': player_game.points,
                'assists': player_game.assists,
                'offensiveRebounds': player_game.offensive_rebounds,
                'defensiveRebounds': player_game.defensive_rebounds,
                'steals': player_game.steals,
                "blocks": player_game.blocks, 
                "turnovers": player_game.turnovers, 
                "defensiveFouls": player_game.defensive_fouls, 
                "offensiveFouls": player_game.offensive_fouls, 
                "freeThrowsMade": player_game.free_throws_made, 
                "freeThrowsAttempted": player_game.free_throws_attempted, 
                "twoPointersMade": player_game.two_pointers_made, 
                "twoPointersAttempted": player_game.two_pointers_attempted, 
                "threePointersMade": player_game.three_pointers_made, 
                "threePointersAttempted": player_game.three_pointers_attempted,
                "shots": [{
                    "isMake": shot.is_make,
                    "locationX": shot.location_x,
                    "locationY": shot.location_y
                } for shot in Shot.objects.filter(stat_id_id=player_game.stat_id)]}
                for player_game in player_games] 
        }
        return player_data
    except Player.DoesNotExist or PlayerGameStats.DoesNotExist:
        return None