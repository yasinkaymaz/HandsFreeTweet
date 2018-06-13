#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import sys
import time
import random

TimeSecRangeTop = 25 #Tweeting time density. The higher, the rarer it tweets.
men_d=10 #Density of mentions inserted into tweet texts. The higher, the more diluted. 10 means insert a random @ in evert 10 tweets.

AccountCredentialsFile = sys.argv[1]
TweetPoolFile = open(sys.argv[2],"r")
hashtagPoolFile = open(sys.argv[3],"r")
mentionPoolFile = open(sys.argv[4],"r")

with open(AccountCredentialsFile) as AccFile:
    for item in AccFile:
        username = item.strip().split("\t")[0]
        consumer_key = item.strip().split("\t")[1]
        consumer_secret = item.strip().split("\t")[2]
        access_token = item.strip().split("\t")[3]
        access_token_secret = item.strip().split("\t")[4]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

user = api.me()
print(user.name)

def tweetRandomizer():
    """
    Randomly concatinate hashtags # to tweet texts. Then, shuffle the lines in the output.
    """
    mentionPool = []
    for line in mentionPoolFile:
        mentionPool.append(line.strip())
    hashtagPool = []
    for line in hashtagPoolFile:
        hashtagPool.append(line.strip())

    out1 = open("tmp.txt","w")
    tw_n = 0
    for line in TweetPoolFile:
        text = line.strip()
        for hashtag in hashtagPool:
            tw_n = tw_n+1
            if tw_n%men_d == 0:
                tweetThisText="Sayin "+mentionPool[random.randint(1,len(mentionPool)-1)]+" "+text+" #1416ylsy #1416ylsyTAZMINAT "+hashtag
            else:
                tweetThisText= text+" #1416ylsy #1416ylsyTAZMINAT "+hashtag
            if len(tweetThisText) > 290:
                print "Character limit exceeded! Skipping the tweet...", tweetThisText
            else:
                out1.write(tweetThisText+"\n")
    out1.close()
    #Randomize the tweet lines in the text file:
    out2 = open("Randomized_TweetPool.txt","w")
    with open("tmp.txt",'r') as outfile:
        lines = outfile.readlines()
    random.shuffle(lines)
    for line in lines:
        out2.write(line.strip()+"\n")

    os.remove("tmp.txt")
    return





def main():
    tweetRandomizer()
    SuccessfulTweetNumber = 0
    with open("Randomized_TweetPool.txt") as TwPool:
        for line in TwPool:
            tweetThisText = line.strip()
            print(tweetThisText)
            try:
                api.update_status(tweetThisText)
                SuccessfulTweetNumber = SuccessfulTweetNumber+1
                print "Tweet tweeted! Tweet number is ", SuccessfulTweetNumber
                time.sleep(random.randint(1,TimeSecRangeTop))
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

    print "Total Number of texts tweeted successfully is ", SuccessfulTweetNumber
main()

#How to run this script:
#python autoTweet.py tokenKeyFile.txt tweetpool_v4.txt hashtags.txt mentiontags.txt
