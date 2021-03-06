#/*
# * ------------------------------------------------------------
# * "THE BEERWARE LICENSE" (Revision 42):
# * cfultz (Caleb Fultz) wrote this code. As long as you retain this 
# * notice, you can do whatever you want with this stuff. If we
# * meet someday, and you think this stuff is worth it, you can
# * buy me a beer in return.
# * ------------------------------------------------------------
#*/
# bot.py

import tweepy, time, sys
from secrets import *

argfile = str(sys.argv[1]) # This allows for you to pass the text file of your choosing through to tweet each line

##
## From Tweepy OAuth documentation
##
#create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

 #Construct the API instance
api = tweepy.API(auth) # create an API object

# Allows the file to be parsed

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

# For every line in the file, process it as a status update.

for line in f:
    api.update_status(status=line)
    time.sleep(3600) # Tweet every 1 hour for rate limiting.
### Note that the time can be shortened significantly lower, however
### you need to follow the Twitter guidelines
### or you'll have your bot and account banned.

