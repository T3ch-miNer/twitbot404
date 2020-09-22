# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:36:33 2020

@author: rahul
"""

#importing libraries

import tweepy
import time 

#keys generated from twitter developer site
consumer_key = 'KL8dn5e5WgwCxMLiaw1R4IWGC'
consumer_secret = 'sFEo5Y2hd3GqJo6riNQ8Z6oyPpWgJsO66lGFLcyosF8aWIVYnM'
key = '99275917-9BY2fRbBZ93DVzRynX29H2RAB0J7g2a3509cgAl4T'
secret = 'HR1H1GFQLLhVT03zMi3vSRsa5Wpd2kyMUEf99XrZ3Iibv'

'''consumer_key = 'ZGKPdPsl5XrWqZdLlZrmZUndf'
consumer_secret = 'iJLEa8OmGb0o1wLS0fui0DGk0189xMk80NIBu8VWH2fWo8d89c'
key = '99275917-eX4vgjQm39SLQHnwwpAEVP0KnTjj18fMcbuwZmvkx'
secret ='RvCRe7Xn1nJid3LgjZ1VRdWKlB3gcNOinlaqiFriO7ZsA'
'''
#get our working
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

#updating our status( basically it will tweet behalf of you)

api = tweepy.API(auth)
#api.update_status('Salam Namaste Twitter Vasiyoo #twitbot')

FILE_NAME ='previousguy.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id
#reading 
def store_last_seen(FILE_NAME, last_seen_id):
    file_write =open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return
#writing
tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
#print(tweets[0].text)

for tweet in reversed(tweets):
    if '#twibot' in tweet.full_text.lower():
        print(str(tweet.id)+' - ' + tweet.full_text)
        api.update_status("@" + tweet.user.screen_name + " twitbot worked :) ", tweet.id)
        store_last_seen(FILE_NAME,tweet.id)
        
        
        
        
        