#!/usr/bin/env python3

from flask import Flask, request, jsonify
# from flask_cors import CORS  # Comment out CORS on deployment
import os
import psycopg2
# import get_player_data

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


# @app.post("/echo_user_input")
# def echo_input():
#     input_text = request.form.get("user_input", "")
#     return "Greeting: " + input_text


def get_player_name(number):
    active_players = players.get_active_players()
    return active_players[number]


@app.route("/echo_user_input", methods=['POST'])
def get_active_player():
    user_input = request.form["user_input"]
    nba_player = players.find_players_by_full_name(user_input)
    if nba_player[0] is None:
        return "No player found"
    if user_input != nba_player[0]['full_name']:
        return "The player cannot be found. Press the back button and try again."
    else:
        nba_player_career = playercareerstats.PlayerCareerStats(player_id=nba_player[0]['id'])
        return nba_player_career.get_normalized_json()


@app.route("/")
def main():
    front_page = '''Soon this will be a website for NBA basketball players' metrics for stats gurus,
        fantasy players, or curiosity. <br>
        
    <p> You can check if the player you entered is active or not.
    Enter the first AND last name and spell correctly. <br>

    All source code can be found at https://www.github.com/matthewjchin/nbastatslookup
    </p>
    <form action="/echo_user_input" method="POST">
     <input name="user_input">
     <input type="submit" value="Submit!">
    </form>
    '''

    return front_page
    # return ''


if __name__ == "__main__":
    app.run(debug=True)

