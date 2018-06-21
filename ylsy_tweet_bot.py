# coding=utf-8
'''
BilalCe tarafindan paylasildi...

'''

import tweepy, sys, time
import requests
import random
import time, datetime
import schedule


from time import sleep
from random import randint
from datetime import datetime
from threading import Timer



#### He hesap icin atilacak maximum tweet ve retweet sayisi.

max_twit = 6
numberofTweets = 10

#### Auto Tweet atmak icin twitlist teki daha onceden hazirlanmis twitleri okuyor. Oradan rastegele birini seciyor.

with open('twitlist.txt', 'r') as f:
    myNames = [line.strip() for line in f]

####

def tweetToTwitter():

	numm=random.randint(0, len(myNames)-1)

	for i in range (numm, numm + max_twit) :
		try:
			mystatustext = myNames[i]
			api.update_status(status=mystatustext)
			twit_sp = random.randint(10, 120)
			sleep(twit_sp)

		except tweepy.TweepError as e:
			print(e.reason)
			continue
		except StopIteration:
			break


def retweetToTwitter():
    search = ("1416ylsy")

    for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
            if not tweet.user.following:
            	tweet.user.follow()
            	print('Followed the user')
            	twit_sp1 = random.randint(10, 120)
            	sleep(twit_sp1)

        except tweepy.TweepError as e:
            print(e.reason)
            continue
        except StopIteration:
            break

#### Ben actigim 5 tane ayri hesaptan twit atiyorum. Asagida her hesabin consumer keyi, consumer secreti, access tokeni ve access token secreti var.

consumer_key = [
"cons_key1",
"cons_key2",
"cons_key3",
"cons_key4",
"cons_key5",
]


consumer_secret = [
"cons_secret1",
"cons_secret2",
"cons_secret3",
"cons_secret4",
"cons_secret5"
]

access_token = [
"access_token1",
"access_token2",
"access_token3",
"access_token4",
"access_token5",
]


access_token_secret = [
"access_token_secret1",
"access_token_secret2",
"access_token_secret3",
"access_token_secret4",
"access_token_secret5",
]

#### bu kisim, yukarida API bilgileri listelenmis her hesap icin listeden rastgele bir twit secip atiyor.
#### Sonra 10 saniye ile 120 saniye arasi bekliyor (rastege) bir twit data atiyor.
#### Bir hesaptan toplam 6 tane twit atip yukarida listelenmis ikinci hesaptan atmaya basliyor.

for x in range(0, len(consumer_key)):
	auth = tweepy.OAuthHandler(consumer_key[x], consumer_secret[x])
	auth.set_access_token(access_token[x], access_token_secret[x])
	api = tweepy.API(auth, wait_on_rate_limit=True)

	user = api.me()
	print(user.name)

	tweetToTwitter()

	twit_sp2 = random.randint(10, 120)
	sleep(twit_sp2)

#### bu kisim, yukarida API bilgileri listelenmis her hesap icin Retweet yapiyor.
#### Atilmis twitlerde #1416ylsy hastgini arayip, bulduklarini retwit yapiyor.
#### Sonra 10 saniye ile 120 saniye arasi bekliyor (rastege) bir retweet data atiyor.
#### Bir hesaptan toplam 10 tane twit atip yukarida listelenmis ikinci hesaptan atmaya basliyor.
#### Ayrica eger Retweet yaptigi hesabi takip etmiyorsa, o hesabi otmatik olarak takip etmeye basliyor.


for x in range(0, len(consumer_key)):
	auth = tweepy.OAuthHandler(consumer_key[x], consumer_secret[x])
	auth.set_access_token(access_token[x], access_token_secret[x])
	api = tweepy.API(auth, wait_on_rate_limit=True)

	user = api.me()
	print(user.name)

	retweetToTwitter()
