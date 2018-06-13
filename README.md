# HandsFreeTweet
This repository provides a collection of codes for tweeting while working...


### How to install:
Assuming that you already have python install in your computer.

**First**, you need to install tweepy module:

```
sudo pip install tweepy
```
or
```
git clone https://github.com/tweepy/tweepy.git
cd tweepy
sudo python setup.py install
```
You can also follow the instructions here: https://github.com/tweepy/tweepy

**Then**, download this code to your computer by typing the following:
```
git clone https://github.com/yasinkaymaz/HandsFreeTweet.git

cd HandsFreeTweet
```

Now it is ready to use.

---

### How to use:

#### Prepare a file for your twitter account credentials :

First, create an application from https://apps.twitter.com/

A tab separated tab file which contains in the exact order: username, consumer_key, consumer_secret, access_token, access_token_secret

Example tokenKeyFile.txt file (tab separated):

$ cat tokenKeyFile.txt

TwitterUsername	3RD4iElfk5Qyu22PRCQq6to4j	1rZvVMnRKkBqYKNyx9G84rv3CdcHa0p4XdHl23JQua0ijf	1003735820948571226309-snSxi0ILFOWflsj201H0kwlXf5MJmox6	6XLOiy5IbKZPUeKfl39fSLiIDHJ2heTQrlywPuqbetUlYB

#### Second file you need is a text file in which you store your tweets: one tweet text per line.
Randomized_TweetPool.txt

#### Third file you need is a text file which contains tags per line:
$ cat tags.txt

@RT_Erdogan

@BA_Yildirim

@TC_Basbakan

@tcbestepe

...

---

#### Run autoTweet

cd HandsFreeTweet

python autoTweet.py tokenKeyFile_lovenzyme.txt tweetpool_v4.txt tags.txt

##### Limit: 25 tweets per 15mins.
