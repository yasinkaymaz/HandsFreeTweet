#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import sys
import time
import random

#lovenzyme
# consumer_key = '58aoH7zjwxnEg8LmnBTjt737C'
# consumer_secret = 'DDV3KoKdse1lDzZDaaZtlSpcGnH5bftxj6c42bGQufFqi3uXNW'
# access_token = '91248892-0JhKXnretakwtRPiDMJtg1hj8QN6Sq0rHHUao7KG1'
# access_token_secret = 'PKre7kzG9qGGI2mjOkjRqyCQjV3gbvwOHIKgzPjgoEomN'

#PrinterDr
consumer_key = 'pNgWj5WuhUam7gH7FI4fFc9RH'
consumer_secret = 'jTVkJI0jNxKu4NXrXCE8zk8KO3bLbBl4KKDtPSeioSHQUKcVL5'
access_token = '1003735858288226309-D2IoiixarItUY62PJirZycm35G6Qik'
access_token_secret = '22zjLuwKAYBBuZJHAEspMjO2Cbp2srGZdUL97XFIGcsW1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

mentionPoolFile = open(sys.argv[2],"r")

def main():
    SuccessfulTweetNumber = 0
    #api.update_status('Sayin @oktay_saral @RT_Erdogan #1416ylsy MEB Burslulari tazminatta zaten dolar olan borca bir de devletin uyguladigi yuksek faizler nedeniyle eziliyor! #1416ylsyTAZMINAT')
    with open(sys.argv[1]) as TwPool:
        for tagline in mentionPoolFile:
            target = tagline.strip()
            for line in TwPool:
                text = line.strip()
                tweetThisText= "Sayin "+target+" "+text
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
