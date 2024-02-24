from flask import Flask, request

from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
from nba_api.stats.static import players

app = Flask(__name__)


# @app.route("/echo_input", methods=["POST"])
# def echo_input():
#     input_text = request.form.get("user_input", "")
#     return "Greeting: " + input_text




@app.route("/echo_user_input", methods=["POST"])
def get_player_name_active():

    user_input = request.form["user_input"]

    nba_player = players.find_players_by_full_name(user_input)
    if nba_player is None:
        return "No player found"
    if user_input != nba_player[0]['full_name']:
        return "The player cannot be found. Please go back and try again."
    else:
        nba_player_career = playercareerstats.PlayerCareerStats(player_id=nba_player[0]['id'])
        return nba_player_career.get_normalized_json()


@app.route("/")
def main():
    return '''Soon this will be a website for NBA basketball players' metrics for stats gurus,
        fantasy players, or curiosity.

    You can check if the player you entered is active or not.
    Enter the first AND last name and spell correctly. <br>
    NOTE: We are working to get a drop down menu and/or features to search by last name.
        </p>

     <form action="/echo_user_input" method="POST">
         <input name="user_input">
         <input type="submit" value="Submit!">
     </form>
    '''


if __name__ == "__main__":
    app.run(debug=True)
    main()



'''
        <br>
        <form action="/echo_input" method="POST">
                 <input name="user_input">
                 <input type="submit" value="Submit!">
             </form>
    <br>'''
