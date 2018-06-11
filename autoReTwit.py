import tweepy

consumer_key = '58aoH7zjwxnEg8LmnBTjt737C'
consumer_secret = 'DDV3KoKdse1lDzZDaaZtlSpcGnH5bftxj6c42bGQufFqi3uXNW'
access_token = '91248892-0JhKXnretakwtRPiDMJtg1hj8QN6Sq0rHHUao7KG1'
access_token_secret = 'PKre7kzG9qGGI2mjOkjRqyCQjV3gbvwOHIKgzPjgoEomN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

def main():
    search = ("1416ylsy")

    numberofTweets = 10
    for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
main()
