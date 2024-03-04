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
def get_player_name_active(nba_player):
    nba_player_career = playercareerstats.PlayerCareerStats(player_id=nba_player['id'])
    return nba_player_career.get_data_frames()[0]


def get_player_common_info(player):
    player_common_info = commonplayerinfo.CommonPlayerInfo(player_id=player['id'])
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
    print(common_info.get_normalized_json())

    # print(get_player_stats(player_info['id']))
    print(get_player_name_active(player_info))

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






# # Get player points, rebounds, assists, steals, blocks, percentages per game
# player_ppg = get_points_per_game(player[0]['id'])
# player_rpg = get_rebounds_per_game(player[0]['id'])
# player_apg = get_assists_per_game(player[0]['id'])
# player_spg = get_steals_per_game(player[0]['id'])
# player_bpg = get_blocks_per_game(player[0]['id'])
# player_fg = get_fg_pct_per_game_career(player[0]['id'])
# player_3pg = get_3pfg_pct_per_game_career(player[0]['id'])
# player_ft = get_ft_pct_per_game_career(player[0]['id'])

# career_avgs += "\nPoints per game:\t" + str(player_ppg)
# career_avgs += "\nRebounds per game: \t" + str(player_rpg)
# career_avgs += "\nAssists per game: \t" + str(player_apg)
# career_avgs += "\nSteals per game: \t" + str(player_spg)
# career_avgs += "\nBlocks per game: \t" + str(player_bpg)
# career_avgs += "\nCareer FG Percentage: \t" + str(player_fg)
# career_avgs += "\nCareer 3PFG Percentage: \t" + str(player_3pg)
# career_avgs += "\nCareer FT Percentage: \t" + str(player_ft)
#
# return career_avgs




