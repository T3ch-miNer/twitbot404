# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:24:50 2020

@author: rahul
"""
import tweepy
import time 

#keys generated from twitter developer site
consumer_key = 'KL8dn5e5WgwCxMLiaw1R4IWGC'
consumer_secret = 'sFEo5Y2hd3GqJo6riNQ8Z6oyPpWgJsO66lGFLcyosF8aWIVYnM'
key = '99275917-9BY2fRbBZ93DVzRynX29H2RAB0J7g2a3509cgAl4T'
secret = 'HR1H1GFQLLhVT03zMi3vSRsa5Wpd2kyMUEf99XrZ3Iibv'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag = "#PlaystationIndia"
tweetNumber=5

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)
searchBot()