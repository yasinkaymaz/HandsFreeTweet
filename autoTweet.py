#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import sys
import time
import random

AccountCredentialsFile = sys.argv[1]
TweetPoolFile = sys.argv[2]
mentionPoolFile = open(sys.argv[3],"r")

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

def tweetRandomizer():
    """
    Randomly add mentions @ to tweet texts and add hashtags to end. Then, shuffle the lines in the output.
    """
    TwPoolFile = open(sys.argv[2],"r")
    out1 = open("tmp.txt","w")
    mentionPool = []
    for line in mentionPoolFile:
        target = line.strip()
        mentionPool.append(target)
    for line in TwPoolFile:
        text = line.strip()
        for mention in mentionPool:
            tweetThisText= "Sayin "+mention+" "+text+" #1416ylsy #1416ylsyTAZMINAT"
            out1.write(tweetThisText+"\n")
            out1.write(line.strip()+"\n")
    out1.close()
    #Randomize the tweet lines in the text file:
    out2 = open("Randomized_TweetPool.txt","w")
    with open("tmp.txt",'r') as outfile:
        lines = outfile.readlines()

    random.shuffle(lines)
    for line in lines:
        out2.write(line.strip()+"\n")

    return





def main():
    tweetRandomizer()
    SuccessfulTweetNumber = 0
    with open("Randomized_TweetPool.txt") as TwPool:
        for line in TwPool:
            tweetThisText = line.strip()
            print(tweetThisText)
            try:
###                api.update_status(tweetThisText)
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
#python autoTweet.py tokenKeyFile_lovenzyme.txt tweetpool_v4.txt tags.txt
