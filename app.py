from flask import Flask, request

from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
from nba_api.stats.static import players

app = Flask(__name__)


# @app.get("/")
# def main():
#     return "Hello World!"


@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "Greeting: " + input_text


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


