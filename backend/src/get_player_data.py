
from flask import Flask

from nba_api.stats.endpoints import commonplayerinfo, playercareerstats
from nba_api.stats.static import players
import random


app = Flask(__name__)


# Picks a number between 0 and 530 (current number of active NBA players) to return their id, first name, and last name
def get_player_name(number):
    active_players = players.get_active_players()
    return active_players[number]


def get_player_common_info(number):
    player_common_info = commonplayerinfo.CommonPlayerInfo(player_id=number)
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


def get_player_stats(number):
    player_career = playercareerstats.PlayerCareerStats(player_id=number)
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


if __name__ == '__main__':
    # db.create_all()
    # Enter number between 0 and 530
    num = random.randint(0, len(players.get_active_players()))
    player_info = get_player_name(num)
    print(player_info)

    # player_common_info = get_player_common_info(num)
    print(get_player_stats(player_info['id']))
    print(get_points_per_game(player_info['id']))
