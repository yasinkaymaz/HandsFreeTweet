# HandsFreeTweet
This repository provides a collection of codes for tweeting while working.

### How to install:
install tweepy: https://github.com/tweepy/tweepy

git clone https://github.com/yasinkaymaz/HandsFreeTweet.git

### How to use:

#### Prepare a file for your twitter account credentials :
A tab separated tab file which contains in the exact order: username, consumer_key, consumer_secret, access_token, access_token_secret

Example:
TwitterUsername	3RD4iElfk5Qyu22PRCQq6to4j	1rZvVMnRKkBqYKNyx9G84rv3CdcHa0p4XdHl23JQua0ijf	1003735820948571226309-snSxi0ILFOWflsj201H0kwlXf5MJmox6	6XLOiy5IbKZPUeKfl39fSLiIDHJ2heTQrlywPuqbetUlYB

#### Second file you need is a text file in which you store your tweets: one tweet text per line.
Randomized_TweetPool.txt

#### Run autoTweet

cd HandsFreeTweet
python autoTweet.py tokenKeyFile.txt Randomized_TweetPool.txt

##### Limit: 25 tweets per 15mins.
