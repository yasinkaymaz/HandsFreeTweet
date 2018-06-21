import tweepy
import sys

AccountCredentialsFile = sys.argv[1]
hashtag_query='#1416ylsy OR #YLSY #1416ylsy OR #1416ylsyTAZMINAT'

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
#print(user.name)

MAX_TWEETS = 5000000000000000000000
#MAX_TWEETS = 50
tc=0

twittedout = open("tweeted.out.txt","w")
for tweet in tweepy.Cursor(api.search, q=hashtag_query, rpp=100).items(MAX_TWEETS):
    # Do something
    tc=tc+1
    print tc
    try:
        #tweet.retweet()
        print tweet.created_at, tweet.text
        twittedout.write(str(tweet.created_at)+"\t"+tweet.text.encode('utf-8')+"\n")
        #print("Tweet Retweeted")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
