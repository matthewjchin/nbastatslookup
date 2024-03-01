from flask import Flask

from nba_api.stats.endpoints import commonplayerinfo, playercareerstats
from nba_api.stats.static import players
import random


app = Flask(__name__)


# Picks a number between 0 and 530 (current number of active NBA players) to return their id, first name, and last name
def get_player_name(number):
    active_players = players.get_active_players()
    return active_players[number]


# This should be the key function in requesting info from users.
# Originally this was in the app.py file
def get_player_name_active(request):
    user_input = request.form["user_input"]
    nba_player = players.find_players_by_full_name(user_input)
    if nba_player is None:
        return "No player found"
    if user_input != nba_player[0]['full_name']:
        return "The player cannot be found. Please go back and try again."
    else:
        nba_player_career = playercareerstats.PlayerCareerStats(player_id=nba_player[0]['id'])
        return nba_player_career.get_normalized_json()


def get_player_common_info(player):
    player_common_info = commonplayerinfo.CommonPlayerInfo(player_id=player['id'])
    # custom_headers = {
    #     'Host': 'stats.nba.com',
    #     'Connection': 'keep-alive',
    #     'Cache-Control': 'max-age=0',
    #     'Upgrade-Insecure-Requests': '1',
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3)
    #     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,
    #     image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'en-US,en;q=0.9',
    # }
    # player_common_info = commonplayerinfo.CommonPlayerInfo(player_id=number, proxy='127.0.0.1:80',
    #                                                        headers=custom_headers, timeout=600)
    return player_common_info.get_response()


def get_player_last_name(name):
    players_last_name = players.find_players_by_last_name(name)
    return players_last_name


def get_player_stats(pid):
    player_career = playercareerstats.PlayerCareerStats(player_id=pid)
    return player_career.get_data_frames()[0]


def get_points_per_game(pid):
    player_career = playercareerstats.PlayerCareerStats(player_id=pid)
    return sum(player_career.get_data_frames()[0]['PTS']) / sum(player_career.get_data_frames()[0]['GP'])


def get_rebounds_per_game(pid):
    player_career = playercareerstats.PlayerCareerStats(player_id=pid)
    return sum(player_career.get_data_frames()[0]['REB']) / sum(player_career.get_data_frames()[0]['GP'])


def get_assists_per_game(pid):
    player_career = playercareerstats.PlayerCareerStats(player_id=pid)
    return sum(player_career.get_data_frames()[0]['AST']) / sum(player_career.get_data_frames()[0]['GP'])


def get_steals_per_game(pid):
    player_career = playercareerstats.PlayerCareerStats(player_id=pid)
    return sum(player_career.get_data_frames()[0]['STL']) / sum(player_career.get_data_frames()[0]['GP'])


def get_blocks_per_game(pid):
    player_career = playercareerstats.PlayerCareerStats(player_id=pid)
    return sum(player_career.get_data_frames()[0]['BLK']) / sum(player_career.get_data_frames()[0]['GP'])


def get_fta_per_game(pid):
    player_career = playercareerstats.PlayerCareerStats(player_id=pid)
    return sum(player_career.get_data_frames()[0]['FTA']) / sum(player_career.get_data_frames()[0]['GP'])


def get_fg_pct_per_game(pid):
    player_career = playercareerstats.PlayerCareerStats(player_id=pid)
    return player_career.get_data_frames()[0]['FG_PCT']


def get_fg_pct_per_game_career(pid):
    player_career = playercareerstats.PlayerCareerStats(player_id=pid)
    return sum(player_career.get_data_frames()[0]['FGM']) / sum(player_career.get_data_frames()[0]['FGA'])


def get_3pfg_pct_per_game(pid):
    player_career = playercareerstats.PlayerCareerStats(player_id=pid)
    return player_career.get_data_frames()[0]['FG3_PCT']


def get_3pfg_pct_per_game_career(pid):
    player_career = playercareerstats.PlayerCareerStats(player_id=pid)
    return sum(player_career.get_data_frames()[0]['FG3M']) / sum(player_career.get_data_frames()[0]['FG3A'])


def get_ft_pct_per_game(pid):
    player_career = playercareerstats.PlayerCareerStats(player_id=pid)
    return player_career.get_data_frames()[0]['FT_PCT']


def get_ft_pct_per_game_career(pid):
    player_career = playercareerstats.PlayerCareerStats(player_id=pid)
    return sum(player_career.get_data_frames()[0]['FTM']) / sum(player_career.get_data_frames()[0]['FTA'])


# Primarily a function for testing purposes; generate a random number
if __name__ == '__main__':

    # Enter number between 0 and 530
    num = random.randint(0, len(players.get_active_players()))
    player_info = get_player_name(num)
    # print(player_info)
    #
    # player_common_info = get_player_common_info(player_info)
    # print(player_common_info)
    # print(type(player_common_info))

    common_info = commonplayerinfo.CommonPlayerInfo(player_info['id'])
    print(common_info.player_stats)

    # print(get_player_stats(player_info['id']))
    #
    # print(get_points_per_game(player_info['id']))
    # print(get_rebounds_per_game(player_info['id']))
    # print(get_assists_per_game(player_info['id']))
    # print(get_steals_per_game(player_info['id']))
    # print(get_blocks_per_game(player_info['id']))
    # print(get_fg_pct_per_game(player_info['id']))
    # print(get_3pfg_pct_per_game(player_info['id']))
    #
    # print(playercareerstats.PlayerCareerStats(player_id=player_info['id']).get_data_frames())

    # lbj_player = players.find_players_by_full_name("LeBron James")
    # print(lbj_player)
    # print(type(lbj_player))
    # print(lbj_player)

