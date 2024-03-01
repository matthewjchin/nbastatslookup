#!/usr/bin/env python3

from flask import Flask, request, jsonify
# from flask_cors import CORS  # Comment out CORS on deployment
import os
import psycopg2
import get_player_data

from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
from nba_api.stats.static import players

# CREATE_PLAYERS_TABLE = """CREATE TABLE IF NOT EXISTS players (player_id integer PRIMARY,
#                     player_name VARCHAR, first_name VARCHAR, last_name VARCHAR, date TIMESTAMP); """
#
# CREATE_STATS_TABLE = """CREATE TABLE IF NOT EXISTS playerstats (player_id integer PRIMARY,
#                         date TIMESTAMP, fgpct DECIMAL(10,2), 3pfgpct DECIMAL(10,2).
#                          ppg DECIMAL(10,2), rpg DECIMAL(10,2), apg DECIMAL(10,2).
#                          spg DECIMAL(10.2), bpg DECIMAL(10.2) ON DELETE CASCADE)"""
#
# INSERT_PLAYER_RETURN_ID = """INSERT INTO players"""

app = Flask(__name__)


# url = os.getenv(db_link)
# connection = psycopg2.connect(url)


# This function is meant for testing purposes
# Originally part of the first phase of project or in event that a deployment fails
@app.post("/echo_greeting")
def echo_input():
    input_text = request.form.get("greeting", "")
    return "Greeting: " + input_text


from nba_api.stats.library import data


@app.post("/get_player_info")
def get_any_player_name():
    player_str = ''
    user_input = request.form['user_input']

    number = int(user_input)
    players_list = players.get_players()
    player_info = players_list[number]

    player_str += str(player_info)

    # nba_player_career = playercareerstats.PlayerCareerStats(player_id=player_info[0])
    # player_str += str(nba_player_career.get_normalized_json())
    return player_str


@app.post("/active_stats")
def get_active_player_avgs():
    user_input = request.form['player']
    career_avgs = ''''''

    # Get player info
    player = players.find_players_by_full_name(user_input)
    career_avgs += "Player ID:\t" + str(player[0]['id'])
    career_avgs += "\nFirst Name: \t" + str(player[0]['first_name'])
    career_avgs += "\nLast Name: \t" + str(player[0]['last_name'])

    # Get player points, rebounds, assists, steals, blocks, percentages per game
    player_ppg = get_player_data.get_points_per_game(player[0]['id'])
    player_rpg = get_player_data.get_rebounds_per_game(player[0]['id'])
    player_apg = get_player_data.get_assists_per_game(player[0]['id'])
    player_spg = get_player_data.get_steals_per_game(player[0]['id'])
    player_bpg = get_player_data.get_blocks_per_game(player[0]['id'])
    player_fg = get_player_data.get_fg_pct_per_game_career(player[0]['id'])
    player_3pg = get_player_data.get_3pfg_pct_per_game_career(player[0]['id'])
    player_ft = get_player_data.get_ft_pct_per_game_career(player[0]['id'])

    career_avgs += "\nPoints per game:\t" + str(player_ppg)
    career_avgs += "\nRebounds per game: \t" + str(player_rpg)
    career_avgs += "\nAssists per game: \t" + str(player_apg)
    career_avgs += "\nSteals per game: \t" + str(player_spg)
    career_avgs += "\nBlocks per game: \t" + str(player_bpg)
    career_avgs += "\nCareer FG Percentage: \t" + str(player_fg)
    career_avgs += "\nCareer 3PFG Percentage: \t" + str(player_3pg)
    career_avgs += "\nCareer FT Percentage: \t" + str(player_ft)

    return career_avgs


# @app.post("/get_active_player_stats")
def get_active_player():
    user_input = request.form["user_input"]
    nba_player = players.find_players_by_full_name(user_input)
    if nba_player[0] is None:
        return "No player found"
    if user_input != nba_player[0]['full_name']:
        return "The player cannot be found. Press the back button and try again."
    else:
        nba_player_career = playercareerstats.PlayerCareerStats(player_id=nba_player[0]['id'])
        return '''NBA player output: <br>''' + nba_player_career.get_normalized_json()


@app.route("/")
def main():
    front_page = '''
    
    <h1>NBA Player Stats Lookup</h1>
    <p>
    Soon this will be a website for NBA basketball players' metrics for stats gurus,
    fantasy players, or curiosity. You can check if the player you entered is active or not.
   
    </p>
    
    
    Feeling like you just want to enter a random number? 
    Insert a number below and get an NBA player's info, former or current.   
    <form action="/get_player_info" method="POST">
     <input name="user_input">
     <input type="submit" value="Submit">
    </form>
    
    <br>
        
    Want to input a player's name and look up their overall career averages? 
    Enter the first AND last name and spell correctly. 
    (Temporary, but but currently the only thing that works for now.)
    <form action="/active_stats" method="POST">
     <input name="player">
     <input type="submit" value="Submit">
    </form>
    
    '''

    front_page += "All source code can be found at https://www.github.com/matthewjchin/nbastatslookup"

    return front_page
    # return ''


if __name__ == "__main__":
    app.run(debug=True, port=5000)


# Don't use these forms
# Change "echo_user_input" whenever deemed possible
'''<form action="/echo_user_input" method="POST">
     <input name="user_input">
     <input type="submit" value="Submit!">
    </form>'''

'''<form action="/echo_greeting" method="POST">
     <input name="greeting">
     <input type="submit" value="Submit!">
    </form>'''