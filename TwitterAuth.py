import numpy as np
import tweepy

def CrumblBot():

    client = tweepy.Client(consumer_key="XXXXXXXXXXXXXXXXXXXXXXXXX",
                        consumer_secret="XXXXXXXXXXXXXXXXXXXXXXXXX",
                        access_token="XXXXXXXXXXXXXXXXXXXXXXXXX",
                        access_token_secret="XXXXXXXXXXXXXXXXXXXXXXXXX")

    f = open("crumbl-cookie-flavors.txt", "r")
    response = client.create_tweet(text=f.read())
