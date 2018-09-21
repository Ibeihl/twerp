# Twitter Races

## An easy way to set two people, keywords, or hashtags against each other!

### Set Up Instructions
After cloning this repo, you must create an account with Twitter if you do not already have one, and create a new app to get the necessary access tokens and keys to access the streaming api. Don't worry it is easy to do and free!

Here's a link to the developer login!

https://developer.twitter.com/en/apply-for-access.html

After that make sure you have Mongodb installed on your computer and running before you try to start the game, here's a link to help install and run!

https://docs.mongodb.com/manual/installation/

This program uses Python3, so make sure you have that installed! You can check to see what version of python you have on your computer with: $ python3 --version in the command line.

### How to Play
Once the game is set up properly, all you have to do is choose your contestants!  Enter your two chosen contestants as strings as defined in the listener class.  The game is currently set up to filter out any non-english tweets that are not from the US, but of those can be modifed by changing the language setting and the locations setting.  For more information on how to do that, checkout Twitter's streaming documentation.

https://developer.twitter.com/en/docs/tweets/rules-and-filtering/overview/standard-operators.html

After entering the contestants in the listener class, all you have to do is open a terminal window, cd into the correct directory where you have cloned this repo, and run python3 main.py

To end the game and stop the live stream, simply enter ^c

To restart the game, run the clear_score function in the script by uncommenting it, and commenting the run_twitter_race function to reset.  Then, comment out the clear_score function and uncomment the run_twitter_race function and run the code again!

### Screen Shot
![screen shot 2018-09-21 at 11 22 27 am](https://user-images.githubusercontent.com/38081935/45899189-036a3600-bd91-11e8-8a26-33d295e9ca5c.png)


### Target Audience
Anyone interested in using live twitter data and comparing popular or trending topics.  

### Future
I would like to make it easier for users to play the game by allowing them to simply enter their two contestants and run the program.  After that, I plan on creating a simple gui where users can enter their contestants, run the game, see the live results and score, and reset the game.
