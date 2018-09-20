import pymongo
from pymongo import MongoClient

def score_keeper(contestant1, contestant2):
    client = MongoClient()
    db = client.tweep
    twitter_race = db.tweeps

    score1 = twitter_race.find({"tweet": {"$regex": ".*%s.*" % contestant1 } }).count()
    score2 = twitter_race.find({"tweet": {"$regex": ".*%s.*" % contestant2 } }).count()
    if score1 > score2:
        print("%s is winning! The is %d to %d" %(contestant1, score1, score2))
    elif score2 > score1:
        print("%s is winning! The is %d to %d" %(contestant2, score2, score1))
    elif score1 == score2:
        print("It's tied! the score is %d to %d" %(score1, score2))
        

# build a few queries and see what people are talking about?
# add these to a graph or something to have the data tell a story?
# you could stream a bunch of tweets, then query the db for a couple names
# of politicians and see who is getting more tweets?
# ideas for key words to search for...
    # democrat, republican, congress, senate, house, election
