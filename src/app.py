#!/usr/bin/env python3

from flask import Flask, request, jsonify
# # from flask_cors import CORS  # Comment out CORS on deployment
import os
import psycopg2
# import csv

from nba_api.stats.library import data
from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
from nba_api.stats.static import players
from nba_api.live.nba.endpoints import *

# CREATE_PLAYERS_TABLE = """CREATE TABLE IF NOT EXISTS players (player_id integer PRIMARY,
#                     player_name VARCHAR, first_name VARCHAR, last_name VARCHAR, date TIMESTAMP); """
#
# CREATE_STATS_TABLE = """CREATE TABLE IF NOT EXISTS playerstats (player_id integer PRIMARY,
#                         date TIMESTAMP, fgpct DECIMAL(10,2), 3pfgpct DECIMAL(10,2),
#                          ppg DECIMAL(10,2), rpg DECIMAL(10,2), apg DECIMAL(10,2),
#                          spg DECIMAL(10,2), bpg DECIMAL(10,2) ON DELETE CASCADE)"""
#


app = Flask(__name__)


url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url, sslmode='require')

#
# # This function is meant for testing purposes
# # Originally part of the first phase of project or in event that a deployment fails
# @app.post("/echo_greeting")
# def echo_input():
#     input_text = request.form.get("greeting", "")
#     return "Greeting: " + input_text


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


@app.post("/get_games")
def get_tonight_games():
    return scoreboard.ScoreBoard().get_json()


@app.post("/active_player_stats")
def get_active_player():
    user_input = request.form["active_player"]
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
    
    <br>
    
    All source code can be found at https://www.github.com/matthewjchin/nbastatslookup
    </p>
    
    
    Feeling like you just want to enter a random number? 
    Insert a number below and get an NBA player's info, former or current.   
    <form action="/get_player_info" method="POST">
     <input name="user_input">
     <input type="submit" value="Submit">
    </form>
    <br>
    
    Get today's scheduled games: 
    <form action="/get_games" method="POST">
    <input type="submit" value="Get today's NBA games">
    </form>
    <br>
    
      <br>
    '''

    # player_input = request.form['player']
    # player = players.find_players_by_full_name(player_input)
    # career_avgs += str(player)

    # common_player = commonplayerinfo.CommonPlayerInfo(player_id=player[0]['id']).get_normalized_json()
    front_page += "<p>Below are the top performing players from today's NBA games.</p><br>"

    # Get all live NBA game updates from the scoreboard library for that day
    # This is to come out as a dictionary, but be printed to webpage as string
    daily_scoreboard = scoreboard.ScoreBoard().get_dict()

    # New code to portray top players
    for x in daily_scoreboard.values():  # first dictionary
        for y, z in x.items():
            if y == 'games':
                for each_game in z:
                    front_page += (str(each_game['homeTeam']['teamCity']) + " " +
                                   str(each_game['homeTeam']['teamName']))
                    front_page += " (HOME) vs. "
                    front_page += (str(each_game['awayTeam']['teamCity']) + " " +
                                   str(each_game['awayTeam']['teamName']))
                    front_page += " (AWAY) <br>"
                    front_page += (str(each_game['homeTeam']['teamTricode']) + "    " +
                                   str(each_game['awayTeam']['teamTricode']))
                    front_page += "<br>"
                    front_page += (str(each_game['homeTeam']['score']) + "      " +
                                   str(each_game['awayTeam']['score']))
                    front_page += "<br>"
                    front_page += (str(each_game['gameLeaders']) + "<br><br>")


    # front_page += daily_scoreboard

    return front_page


if __name__ == "__main__":
    app.run(debug=True, port=5000)


# Unfortunately this code will crash on Heroku every time it is run
''' <p> Want to input a player's name and look up their overall career averages? 
    Enter the first AND last name and spell correctly. 
    (Temporary, but but currently the only thing that works for now.)
    <form action="/active_player_stats" method="POST">
     <input name="active_player">
     <input type="submit" value="Go">
    </form>  </p>'''

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
