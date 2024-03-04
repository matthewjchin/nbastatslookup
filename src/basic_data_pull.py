from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats, playergamelog
import pandas as pd
import datetime
import csv


# Get a list of all NBA players
# nba_players = players.get_players()

# Get a list of all ACTIVE NBA players
nba_players = players.get_active_players()

# Get a list of all inactive NBA players
# nba_players = players.get_inactive_players()

# Initialize a list to store player seasons
player_seasons = []

# Count variable
count = 0

for player in nba_players:
    # player_id = player['id']
    # player_name = player['full_name']

    # Just a sample - Stephen Curry
    if player['full_name'] == 'Stephen Curry':
        career_stats = playercareerstats.PlayerCareerStats(player_id=player['id'])
        career_stats_df = career_stats.get_data_frames()[0] # career regular season stats by season

        # career_stats_df = career_stats.get_data_frames()[1] # total career regular season stats
        # career_stats_df = career_stats.get_data_frames()[2] # career playoffs stats by season
        # career_stats_df = career_stats.get_data_frames()[3] # total career playoffs stats
        # career_stats_df = career_stats.get_data_frames()[4] # career all-star season stats by season
        # career_stats_df = career_stats.get_data_frames()[5] # total career all-star stats
        # career_stats_df = career_stats.get_data_frames()[6] # college stats by season
        # career_stats_df = career_stats.get_data_frames()[7] # total college stats
        # career_stats_df = career_stats.get_data_frames()[8] # headers, and 9
        # career_stats_df = career_stats.get_data_frames()[10] # regular season rankings by season
        # career_stats_df = career_stats.get_data_frames()[11] # postseason rankings by season

        # print(career_stats.get_data_frames()[9])
        # print(type(career_stats_df)) # type: <class 'pandas.core.frame.DataFrame'>
        # print(career_stats_df['PTS'])   # points by season
        # print(career_stats_df['PTS'] / career_stats_df['GP'])   # points per game by season

        print("Career Stats for: ", player['id'], player['full_name'])
        print("Points per game: %3.2f" % (sum(career_stats_df['PTS']) / sum(career_stats_df['GP'])))  # career points per game
        print("Rebounds per game: %3.2f" % (sum(career_stats_df['REB']) / sum(career_stats_df['GP'])))  # career rebounds per game
        print("Assists per game: %3.2f" % (sum(career_stats_df['AST']) / sum(career_stats_df['GP'])))  # career assists per game
        print("Steals per game: %3.2f" % (sum(career_stats_df['STL']) / sum(career_stats_df['GP'])))  # career steals per game
        print("Blocks per game: %3.2f" % (sum(career_stats_df['BLK']) / sum(career_stats_df['GP'])))  # career blocks per game
        print("Turnovers per game: %3.2f" % (sum(career_stats_df['TOV']) / sum(career_stats_df['GP'])))  # career turnovers per game
        print()
        print("Field goal percentage: %3.2f" % (sum(career_stats_df['FGM']) / sum(career_stats_df['FGA'])))
        print("3-point field goal percentage: %3.2f" % (sum(career_stats_df['FG3M']) / sum(career_stats_df['FG3A'])))
        print("Free throw percentage: %3.2f" % (sum(career_stats_df['FTM']) / sum(career_stats_df['FTA'])))

    # career_stats_df = career_stats.get_data_frames()[0]
    # count += 1

# Returns the total number of NBA players listed with data in the API
# print(count)


'''
Total NBA Players with data pulled from API: 4900

Total Active NBA Players (as of 2023-24 season): 531
Total inactive NBA players: 4369
'''

