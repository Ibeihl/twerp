from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time
import pymongo
from pymongo import MongoClient
from keys import ckey, csecret, atoken, asecret, monkeyKey
from queries import score_keeper

#sets up mongo with collection of tweets
client = MongoClient()
db = client.tweep
twitter_race = db.tweeps

#this opens the live stream and stores the tweets in a mongodb
class listener(StreamListener):
    contestant1 = "demo"
    contestant2 = "the"
    def on_data(self, data):
        # self.contestant1 = contestant1
        # self.contestant2 = contestant2
        all_data = json.loads(data)
        tweet = str(time.ctime(int(time.time()))) + '::' + all_data["text"] 
        # insertMe = tweet.encode('ascii', 'ignore')

        twitter_race.insert_one({'tweet': tweet})
        print(tweet + "\n\n")
        print(self.contestant1)
        print(self.contestant2)
        score_keeper(self.contestant1, self.contestant2)
        return True
    
    def on_error(self, status):
        print(status)

# auth = OAuthHandler(ckey, csecret)
# auth.set_access_token(atoken, asecret)

# twitterStream = Stream(auth, listener())
# twitterStream.filter(locations=[-124.625,41.875,-116.375,46.375], languages=["en"]) 
# twitterStream.filter(follow=["25073877"], languages=["en"])
# twitterStream.filter(follow=["32010840"], locations=[-124.625,41.875,-116.375,46.375], languages=["en"])
# twitterStream.filter(follow=["32010840"])

def all_in_one(ckey, csecret, atoken, asecret):
    #set up mongodb
    client = MongoClient()
    db = client.tweep
    twitter_race = db.tweeps

    #auth info set up
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    #set up the twitter stream
    twitterStream = Stream(auth, listener())

    #add contestant attribute
    # twitterStream.contestant1 = contestant1
    # twitterStream.contestant2 = contestant2

    #add geobox location
    twitterStream.filter(follow=["25073877"])




all_in_one(ckey, csecret, atoken, asecret)