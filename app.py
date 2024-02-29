from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import psycopg2

from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
from nba_api.stats.static import players

db_link = "DATABASE_URL=postgres://u12u7b6fo9s684:pa6b488169207651760673e9c9e9e2d187fa9b804e6d51789a8e53b572d2e6820@ec2-44-210-26-29.compute-1.amazonaws.com:5432/d1g41cl80lao5h"

CREATE_PLAYERS_TABLE = """CREATE TABLE IF NOT EXISTS players (player_id integer PRIMARY, 
                    player_name VARCHAR, first_name VARCHAR, last_name VARCHAR, date TIMESTAMP); """

CREATE_STATS_TABLE = """CREATE TABLE IF NOT EXISTS playerstats (player_id integer PRIMARY, 
                        date TIMESTAMP, fgpct DECIMAL(10,2), 3pfgpct DECIMAL(10,2).
                         ppg DECIMAL(10,2), rpg DECIMAL(10,2), apg DECIMAL(10,2).
                         spg DECIMAL(10.2), bpg DECIMAL(10.2) ON DELETE CASCADE)"""

INSERT_PLAYER_RETURN_ID = """INSERT INTO players"""

app = Flask(__name__)
url = os.getenv(db_link)
connection = psycopg2.connect(url)


# @app.post("/echo_user_input")
# def echo_input():
#     input_text = request.form.get("user_input", "")
#     return "Greeting: " + input_text


@app.post("/echo_user_input")
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


if __name__ == "__main__":
    app.run(debug=True)


