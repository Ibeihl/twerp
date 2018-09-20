import pymongo
from pymongo import MongoClient
import time

def score_keeper(contestant1, contestant2):
    client = MongoClient()
    db = client.tweep
    twitter_race = db.tweeps

    score1 = twitter_race.find({"tweet": {"$regex": ".*%s.*" % contestant1 } }).count()
    score2 = twitter_race.find({"tweet": {"$regex": ".*%s.*" % contestant2 } }).count()
    print("---------->>> Twitter Battle: %s vs. %s <<<----------" % (contestant1, contestant2))
    
    if score1 > score2:
        print("~~~~~~~~~~ %s is winning! The score is %d to %d ~~~~~~~~~~\n" %(contestant1, score1, score2))
    elif score2 > score1:
        print("~~~~~~~~~~ %s is winning! The score is %d to %d ~~~~~~~~~~\n" %(contestant2, score2, score1))
    elif score1 == score2:
        print("~~~~~~~~~~ It's tied! the score is %d to %d ~~~~~~~~~~\n" %(score1, score2))
        
def clear_score():
    client = MongoClient()
    db = client.tweep
    twitter_race = db.tweeps
    twitter_race.drop()

def start_message():
    print("\n\nLET THE TWITTER BATTLE BEGIN...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1....")
    time.sleep(1)
    print("GO!!!\n\n")