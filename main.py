from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import datetime
import pymongo
from pymongo import MongoClient
from monkeylearn import MonkeyLearn
from keys import ckey, csecret, atoken, asecret, monkeyKey

client = MongoClient()
db = client.tweep
tweeps = db.tweeps

def sentimentalizer(text):
    ml = MonkeyLearn(monkeyKey)
    data = [text]
    model_id = 'cl_qkjxv9Ly'
    result = ml.classifiers.classify(model_id, data)
    _sentiment = result.body[0][u'classifications'][0][u'tag_name']
    confidenceScore = result.body[0][u'classifications'][0][u'confidence'] * 100
    sentiment = {
        "confidence": confidenceScore,
        "rating": _sentiment
        }
    #return "%s with %s percent confidence"%(sentiment["rating"], sentiment["confidence"])
    return sentiment

#this opens the live stream and stores the tweets in a mongodb
class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        # print(type(tweet.encode('ascii', 'ignore')))
        insertMe = tweet.encode('ascii', 'ignore')

        print(tweet)
        sentiment = sentimentalizer(tweet)
        tweeps.insert_one({'tweet': insertMe, 'sentiment': sentiment})
        print(sentiment['rating'])
        return True
    
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
#twitterStream.filter(track=["chicago"])
#twitterStream.filter(locations=[-124.625,41.875,-116.375,46.375]) 
twitterStream.filter(follow=["25073877"])
