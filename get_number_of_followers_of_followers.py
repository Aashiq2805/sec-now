import oauth, tweepy, sys, locale, threading 
from time import localtime, strftime, sleep

def init(): 
    global api
    consumer_key = "..."
    consumer_secret = "..."
    access_key="..."
    access_secret="..."
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api=tweepy.API(auth)
    for follower in tweepy.Cursor(api.followers).items():
        user = tweepy.api.get_user(follower)
        print user.screen_name
        print user.followers_count
