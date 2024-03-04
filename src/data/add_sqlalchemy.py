# import the relevant sql library
from sqlalchemy import create_engine
import os
import psycopg2
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players


# Stephen Curry Total NBA Career Stats
nba_player_sc = players.find_player_by_id(201939)
# print(nba_player_sc)

career_stats = playercareerstats.PlayerCareerStats(player_id=nba_player_sc['id'])
# career_stats_df = career_stats.get_data_frames()[0]
career_stats_df = career_stats.get_data_frames()[1]

# # print(career_stats_df)
#
#
# # url = os.getenv("postgres://u12u7b6fo9s684:pa6b488169207651760673e9c9e9e2d187fa9b804e6d51789a8e53b572d2e6820@ec2-44-210-26-29.compute-1.amazonaws.com:5432/d1g41cl80lao5h")
# # connection = psycopg2.connect(url, sslmode='require')
#
# # link to your database
# # engine = create_engine("postgres://u12u7b6fo9s684:pa6b488169207651760673e9c9e9e2d187fa9b804e6d51789a8e53b572d2e6820@ec2-44-210-26-29.compute-1.amazonaws.com:5432/d1g41cl80lao5h", echo=False)
#
# # db_url = "postgres+psycopg2://u12u7b6fo9s684:pa6b488169207651760673e9c9e9e2d187fa9b804e6d51789a8e53b572d2e6820@ec2-44-210-26-29.compute-1.amazonaws.com:5432/d1g41cl80lao5h"
# # db_url = "postgres://suagpdtpwzoejo:7d51dd4b872c2d148d71b0439eb6c7e33a7ad4494753d71f4839e0a8ff8b54b3@ec2-52-54-200-216.compute-1.amazonaws.com:5432/dfam7jp194973u"
# # db_url = "postgres+psycopg2://suagpdtpwzoejo:7d51dd4b872c2d148d71b0439eb6c7e33a7ad4494753d71f4839e0a8ff8b54b3@ec2-52-54-200-216.compute-1.amazonaws.com:5432/dfam7jp194973u"
# db_url = "postgresql://DATABASE_URL"
#
# engine = create_engine(db_url, echo=False)
#
#
#
# # attach the data frame (df) to the database with a name of the
# # table; the name can be whatever you like
# career_stats_df.to_sql('test_table', con=engine, if_exists='append')
# # run a quick test
#
# print(engine.execute("SELECT * FROM test_table").fetchone())

'''HEROKU_POSTGRESQL_CYAN_URL'''

conn = psycopg2.connect(database="dfam7jp194973u",
                        user="suagpdtpwzoejo",
                        host='ec2-52-54-200-216.compute-1.amazonaws.com',
                        password="7d51dd4b872c2d148d71b0439eb6c7e33a7ad4494753d71f4839e0a8ff8b54b3",
                        port=5432)

# Open a cursor to perform database operations
cur = conn.cursor()
# Execute a command: create test_data table
# cur.execute("""CREATE TABLE test_data(
#             player_id SERIAL PRIMARY KEY,
#             player_name VARCHAR (50) UNIQUE NOT NULL,
#             total_points int NOT NULL,
#             total_rebs int NOT NULL,
#             total_asts int NOT NULL);
#             """)


cur.execute("""
            INSERT INTO test_data(player_id, player_name, total_points, total_rebs, total_asts) 
            VALUES(201939,'Stephen Curry', 23258, 4425, 6025)
            """)
# Make the changes to the database persistent
conn.commit()



# Close cursor and communication with the database
cur.close()
conn.close()



