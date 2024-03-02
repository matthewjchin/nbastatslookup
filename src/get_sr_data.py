# more testing

from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
from nba_api.stats.static import players
from nba_api.live.nba.endpoints import *

daily_scoreboard = scoreboard.ScoreBoard().get_dict()
# print(type(daily_scoreboard))
# print(daily_scoreboard)
# print(daily_scoreboard.keys())

# print(type(daily_scoreboard.values()))
# print(daily_scoreboard.values())

for x in daily_scoreboard.values():     # first dictionary
    # print(type(x))
    for y, z in x.items():  # get key, value of item x, the key of the first dictionary
        # print(y)
        # print(z)
        # print(y, z)
        # print(type(y), type(z))

        # Present game leaders' statistics for that day, whenever made applicable

        if y == 'games':     # check key for "games" and get the values
            # print(gameid )
            for game in z:   # value consists of a list of dictionaries
                print(game['homeTeam']['teamCity'], game['homeTeam']['teamName'],
                      " vs. ", game['awayTeam']['teamCity'], game['awayTeam']['teamName'])
                print(game['gameLeaders'])
                # if game['gameLeaders'] is not None:
                #     print(game['gameLeaders'])
                #     # print(game['gameLeaders'].values())
                # print(game.keys())
                # print(game.values())




