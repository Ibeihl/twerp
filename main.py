from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time
import pymongo
from pymongo import MongoClient
from keys import ckey, csecret, atoken, asecret
from helpers import score_keeper, clear_score, start_message

#sets up mongodb with a db named tweep and collection named tweeps
client = MongoClient()
db = client.tweep
twitter_race = db.tweeps

# this is uses Twitter's StreamListener class ands some custom methods to it.

class listener(StreamListener):
    # here we enter our 2 contestants as strings
    # replace demo and the with your contestants!!
    contestant1 = "Trump"
    contestant2 = "Obama"

    def on_data(self, data):
        #get tweet data
        all_data = json.loads(data)

        #extract tweet text and add timestamp
        if "text" in all_data:
            tweet = str(time.ctime(int(time.time()))) + '::' + all_data["text"]
        else:
            tweet = str(time.ctime(int(time.time()))) + '::'

        #insert our formatted tweet into our mongodb 
        twitter_race.insert_one({'tweet': tweet})

        # run our contestants through our query function
        score_keeper(self.contestant1, self.contestant2)
        print(tweet + "\n\n")
        return True
    
    def on_error(self, status):
        print("something went wrong.... :(")
        print(status)

# here we tie everything together...
def run_twitter_race(ckey, csecret, atoken, asecret):
    #auth info set up
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    start_message()

    #set up the twitter stream
    twitterStream = Stream(auth, listener())

    #add geobox location
    twitterStream.filter(languages=["en"], locations=[-126,24,-67,49])

run_twitter_race(ckey, csecret, atoken, asecret)

# to restart the game, comment out the run_twitter_race, uncomment
# the clear_score function, and run this code!!

# clear_score()
