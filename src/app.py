# import datetime
from django.conf.global_settings import DATABASES
from flask import Flask, request  # , jsonify
# # from flask_cors import CORS  # Comment out CORS on deployment
import os
import psycopg2
import dj_database_url
from dotenv import load_dotenv
# import csv

# from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
from nba_api.stats.static import players
from nba_api.live.nba.endpoints import *

CREATE_PLAYERS_IDS = """CREATE TABLE IF NOT EXISTS 
                        pids(id SERIAL PRIMARY KEY, pid INTEGER);"""

CREATE_ACTIVE_PLAYERS_LOOKUP = """CREATE TABLE IF NOT EXISTS 
                    players_test(player_id INTEGER, player_name VARCHAR, active BOOLEAN);"""

INSERT_INTO_ACTIVE_PLAYERS_LOOKUP = """INSERT INTO players_test(player_id, player_name, active) 
                                        VALUES (%s, %s, %s);"""

# CREATE_STATS_TABLE = """CREATE TABLE IF NOT EXISTS playerstats (player_id integer PRIMARY,
#                         date TIMESTAMP, fgpct DECIMAL(10,2), 3pfgpct DECIMAL(10,2),
#                          ppg DECIMAL(10,2), rpg DECIMAL(10,2), apg DECIMAL(10,2),
#                          spg DECIMAL(10,2), bpg DECIMAL(10,2) ON DELETE CASCADE)"""
#
load_dotenv()
app = Flask(__name__)
# db_url = 'HEROKU_POSTGRESQL_CYAN_URL'
# app.config[db_url] = ""

url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url, sslmode='require')
# psycopg2.connect()
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


# # This function is meant for testing purposes
# # Originally part of the first phase of project or in event that a deployment fails
# @app.post("/echo_greeting")
# def echo_input():
#     input_text = request.form.get("greeting", "")
#     return "Greeting: " + input_text


# Get player basic information, which in this case is if they are an active or inactive NBA player
@app.post("/get_player_info")
def get_any_player_name():
    player_str = ''
    user_input = request.form['user_input']

    try:
        number = int(user_input)
        players_list = players.get_players()
        player_info = players_list[number]

        player_str += str(player_info)
        player_str += "<br>You entered: "
        player_str += str(player_info['full_name'])
        player_str += "<br>Player id: "
        player_str += str(player_info['id'])
        player_str += ("<br>Is this player active? " + str(player_info["is_active"]))

        id = player_info['id']
        name = player_info['full_name']
        active = player_info['is_active']

        cursor = connection.cursor()
        cursor.execute(CREATE_ACTIVE_PLAYERS_LOOKUP)
        cursor.execute(INSERT_INTO_ACTIVE_PLAYERS_LOOKUP, (id, name, active))
        # player_id = cursor.fetchone()[0]
        connection.commit()

        # connection.cursor().close()
        # connection.close()
        return player_str

    except ValueError:
        player_str += "You entered: "
        player_str += user_input
        player_str += "<br> Invalid input. Please go back and enter a number between 0 and 4899. "
        return player_str


# Get a list of all the NBA games playing that night
# Only one large JSON string returned to webpage after pressing "today's games" button
@app.post("/get_games")
def get_tonight_games():
    return scoreboard.ScoreBoard().get_json()


# Get top performers from all live NBA game updates from the scoreboard library for that day
# This is to come out as a dictionary, but be printed to webpage as string
def get_top_performers():
    front_page = ''''''
    daily_scoreboard = scoreboard.ScoreBoard().get_dict()

    # New code to portray top performing players from each game that day
    for x in daily_scoreboard.values():  # first dictionary
        for y, z in x.items():  # second dictionary
            if y == 'games':
                for each_game in z:  # third dictionary
                    # Convert all dictionary keys and/or values to string to add to overall main() string
                    front_page += (str(each_game['homeTeam']['teamCity']) + " " +
                                   str(each_game['homeTeam']['teamName']))
                    front_page += (" (HOME): " + str(each_game['homeTeam']['score']) + "  vs. ")
                    front_page += (str(each_game['awayTeam']['teamCity']) + " " +
                                   str(each_game['awayTeam']['teamName']))
                    front_page += (" (AWAY): " + str(each_game['awayTeam']['score']) + "<br>")
                    front_page += (str(each_game['gameLeaders']) + "<br><br>")

    return front_page


@app.route("/")
def main():
    front_page = '''
    
    <h1>NBA Player Stats Lookup</h1>
    <p>
    Soon this will be a website for NBA basketball players' metrics for stats gurus,
    fantasy players, or curiosity. 
    <br>
    You can check if the player you entered is active or not.
    <br>
    All source code can be found at https://www.github.com/matthewjchin/nbastatslookup
    </p>
    
    <h3>Check for an Active NBA Player</h3>
    Feeling like you just want to enter a random number? 
    Insert a number below and get an NBA player's info, former or current.   
    <form action="/get_player_info" method="POST">
        <input name="user_input">
        <input type="submit" value="Submit">
    </form>
    <br>
    
    <h3>Today's NBA Games</h3>
    Get today's scheduled games by pressing the button below.  
    <form action="/get_games" method="POST">
    <input type="submit" value="Get today's NBA games">
    </form>
    <br>
    
    <h3>Top Performers</h3>
    '''

    front_page += ("<p>Below are the top performing players from today's NBA games.<br>"
                   "Some of the players listed below may be helpful in your stats endeavors "
                   "or as guidance for fantasy basketball. </p>")
    top_players = get_top_performers()
    front_page += top_players

    return front_page


if __name__ == "__main__":
    app.run(debug=True, port=5000)

# Unfortunately this form submission code will crash on Heroku every time it is run
# Code times out after 30 seconds on Heroku, but does work locally
''' <p> Want to input a player's name and look up their overall career averages? 
    Enter the first AND last name and spell correctly. 
    (Temporary, but but currently the only thing that works for now.)
    <form action="/active_player_stats" method="POST">
     <input name="active_player">
     <input type="submit" value="Go">
    </form>  </p>'''

# Don't use these forms
# Change "echo_user_input" whenever deemed possible
'''<form action="/echo_greeting" method="POST">
     <input name="greeting">
     <input type="submit" value="Submit!">
    </form>'''

# This function will be modified to avoid the use of the playercareerstats package of nba_api library
# This work can only be done manually, to gather, analyze, clean, and present statistics to webpage
# This information that is gathered from the playercareerstats package from the webpage will be updated to
# the database that is connected to the webpage, and will be updated once per day in the morning, Pacific Time.
# This was the only way this solution will work as accessing playercareerstats on the webpage times out after
# 30 seconds when deployed via Heroku.
# @app.post("/active_player_stats")
# def get_active_player():
#     user_input = request.form["active_player"]
#     nba_player = players.find_players_by_full_name(user_input)
#
#     if nba_player[0] is None:
#         return "No player found"
#     if user_input != nba_player[0]['full_name']:
#         return "The player cannot be found. Press the back button and try again."
#     else:
#         nba_player_career = playercareerstats.PlayerCareerStats(player_id=nba_player[0]['id'])
#         return '''NBA player output: <br>''' + nba_player_career.get_normalized_json()
