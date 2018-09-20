import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.tweep
tweeps = db.tweeps

# querying the db looking for any tweets that include the word korea
# maybe should build a bunch or different queries...?
results = db.tweeps.find({"tweet": {"$regex": ".*Korea.*" } }).count()
print(results)

# build a few queries and see what people are talking about?
# add these to a graph or something to have the data tell a story?
# you could stream a bunch of tweets, then query the db for a couple names
# of politicians and see who is getting more tweets?
# ideas for key words to search for...
    # democrat, republican, congress, senate, house, election