#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import sys
import time
import random

AccountCredentialsFile = sys.argv[1]
TweetPoolFile = sys.argv[2]

with open(AccountCredentialsFile) as AccFile:
    for item in AccFile:
        username = item.strip().split("\t")[0]
        consumer_key = item.strip().split("\t")[1]
        consumer_secret = item.strip().split("\t")[2]
        access_token = item.strip().split("\t")[3]
        access_token_secret = item.strip().split("\t")[4]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

def main():
    SuccessfulTweetNumber = 0
    with open(TweetPoolFile) as TwPool:
        for line in TwPool:
            tweetThisText = line.strip()
            print(tweetThisText)
            try:
                api.update_status(tweetThisText)
                SuccessfulTweetNumber = SuccessfulTweetNumber+1
                print("Tweet tweeted! Tweet number is ", SuccessfulTweetNumber)
                time.sleep(random.randint(1,100))
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

    print("Total Number of texts tweeted successfully is ", SuccessfulTweetNumber)
main()

#How to run this script:
#python autoTweet.py tokenKeyFile_PrinterDr.txt Randomized_TweetPool.txt
