#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os    
import sys
import time
import pprint
import tweepy
import random
import argparse
import configparser


global debug
debug = True

# Use argparse library for user input
parser = argparse.ArgumentParser(description='Generate tweets and post these from different accounts.')

parser.add_argument('-c', '--credentials', default = 'credentials.ini', help = 'A formatted text file with credentials.')
parser.add_argument('-m', '--messages'   , default = 'messages.txt'   , help = 'A text file with a single message at each line.')
parser.add_argument('-p', '--people'     , default = 'people.txt'     , help = 'A text file with @people at each line.')
parser.add_argument('-t', '--tags'       , default = 'tags.txt'       , help = 'A text file with #hashtag at each line.')

# Command line arguments are stores in <args>
args = vars(parser.parse_args())


TimeSecRangeTop = 25 #Tweeting time density. The higher, the rarer it tweets.
men_d=10 #Density of mentions inserted into tweet texts. The higher, the more diluted. 10 means insert a random @ in evert 10 tweets.

#AccountCredentialsFile = sys.argv[1]
tweetPool = open(args['messages'], 'r').read().splitlines();
hashtagPool = open(args['tags'], 'r').read().splitlines();
mentionPool = open(args['people'], 'r').read().splitlines();

# select tweets, tags and mentions randomly

random.shuffle(tweetPool);
random.shuffle(hashtagPool);
random.shuffle(mentionPool);


# Use configparser library to parse the <ini> file. 
# See the sample <ini> file for syntax and mandatory fields
credentials = configparser.ConfigParser()
credentials.read(args['credentials'])

messages_db_file = open('messages_db.txt', 'a');
messages_db      = []
try:
    messages_db = messages_db_file.readlines();
except:
    pass

# ------------------------------------------------------------------------- #

# Console width used for pretty-printing, 
# e.g. for horizontal separators with '-'s
cWidth = int(os.popen('stty size', 'r').read().split()[1])

# This container holds all the user and their respective
# api's, credentials, statuses (banned, restricted, etc.)
users = [];

max_tweet_len = 240;

must_have_tags = ["#1416ylsy", "#1416ylsytazminat"]


def print_user(user, printDashes = False):

    if printDashes == True:
        print ('-'*cWidth)

    print("Username ---------- : %s" % user["name"])
    print("Is Active --------- : %s" % user["active"])
    print("Consumer Key ------ : %s" % user["ck"])
    print("Consumer Secret --- : %s" % user["cs"])
    print("Access Token ------ : %s" % user["at"])
    print("Access Token Secret : %s" % user["ats"])
    
    
def print_users():

    if len(users) == 0:
        print("No defined users !!!")
        return;

    print('')

    for user in users:
        print_user(user, True)
        
    print ('-'*cWidth)

  #######

def authenticate_users():

    # Clear the users list
    global users
    users = [];

    for sec in credentials.sections():
        # I am lazy, user abbreviations...
        user = {
            "name": credentials.get(sec, 'username'),
            "ck"  : credentials.get(sec, 'consumer_key'),
            "cs"  : credentials.get(sec, 'consumer_secret'),
            "at"  : credentials.get(sec, 'access_token'),
            "ats" : credentials.get(sec, 'access_token_secret')
        };

        user["num_tweets"] = 0;

        try:
            user["auth"] = tweepy.OAuthHandler(user["ck"], user["cs"])
            user["auth"].set_access_token(user["at"], user["ats"])

            #source : https://stackoverflow.com/a/48794903/6811631
            user["api"]  = tweepy.API(user["auth"], wait_on_rate_limit = True, wait_on_rate_limit_notify = True);
            user["user"] = user["api"].me()

            user["active"] = True;

            print (user["auth"])

        except tweepy.TweepError as e:

            print("\n- Error : %s" % e.reason)
            print("Skpping this user (application) < %s / %s >" % (sec, user["name"]));
            continue

        users.append(user);
        
        

def generate_unique_message(tweetNumber, add_people = True, verbose = False):

    num_people_to_mention = random.choice(range(1, 1 + min(4, len(mentionPool))));
    people = [] if add_people == False else random.sample(mentionPool, num_people_to_mention);

    num_tags_to_add = random.choice(range(len(hashtagPool)));
    
    tags = random.sample(hashtagPool, num_tags_to_add);

        
        
    message = " ".join(random.choice(tweetPool).strip().split());

    for must_have_tag in must_have_tags:
        if must_have_tag not in message: 
            if len(message) + len(must_have_tag) + 1 >= max_tweet_len:
                continue;
            message = message + " " + must_have_tag;

    for person in people:
        if person not in message:
            if tweetNumber % men_d ==0:
                if len(message) + len(person) + 1 >= max_tweet_len:
                    continue;
                message = message + " " + person; 
            
        

    for tag in tags:
        if tag not in message: 
            if len(message) + len(tag) + 1 >= max_tweet_len:
                continue;
            message = message + " " + tag;
           

    if message not in messages_db:
        if verbose == True :
            print("Adding message <%s> in the messages database." % message);
        messages_db.append(message);
        messages_db_file.write(message + "\n");
        return message;
    else:
        if verbose == True:
            print("The message <%s> is duplicate. Skipping." % message);
        return generate_unique_message(add_people, verbose);
    
    

# def tweetRandomizer():
#     """
#     Randomly concatinate hashtags # to tweet texts. Then, shuffle the lines in the output.
#     """
# #     mentionPool = []
# #     for line in mentionPoolFile:
# #         mentionPool.append(line.strip())
# #     hashtagPool = []
# #     for line in hashtagPoolFile:
# #         hashtagPool.append(line.strip())

#     out1 = open("tmp.txt","w")
#     tw_n = 0
#     for line in TweetPoolFile:
#         text = line.strip()
#         for hashtag in hashtagPool:
#             tw_n = tw_n+1
#             if tw_n%men_d == 0:
#                 tweetThisText="Sayin "+mentionPool[random.randint(1,len(mentionPool)-1)]+" "+text+" #1416ylsy #1416ylsyTAZMINAT "+hashtag
#             else:
#                 tweetThisText= text+" #1416ylsy #1416ylsyTAZMINAT "+hashtag
#             if len(tweetThisText) > 290:
#                 print "Character limit exceeded! Skipping the tweet...", tweetThisText
#             else:
#                 out1.write(tweetThisText+"\n")
#     out1.close()
#     #Randomize the tweet lines in the text file:
#     out2 = open("Randomized_TweetPool.txt","w")
#     with open("tmp.txt",'r') as outfile:
#         lines = outfile.readlines()
#     random.shuffle(lines)
#     for line in lines:
#         out2.write(line.strip()+"\n")

#     os.remove("tmp.txt")
#     return

def publishTweet():
    while True:

        # We will quit if there are no more active (not yet banned) users
        still_active_users = False;
        
        tweetCounter = 0;

        # Iterate through all users, post unique tweets from each account
        for user in users:

            # Check if the user is active (not banned)
            if user["active"] == False:
                print("Skipping inactive user [%s]" % user["name"]);
                continue;
            else:
                still_active_users = True;

            # 
            message = generate_unique_message(user["num_tweets"]);
 

            print ('-'*cWidth)
            print (' ')
            print("User [%s] is tweeting\n" % user["name"]);
            print("- %s" % message)

            #
            try:

                user["api"].update_status(message)
                user["num_tweets"] = user["num_tweets"] + 1;

                print("\n- Tweet tweeted! Tweet count is [%d]" % user["num_tweets"])

            except tweepy.TweepError as e:
                print("\n- Error : %s" % e.reason)

                if e.api_code == 261:
                    print('')
                    print("- You cannot tweet from this account/app. Possible reasons are :")
                    print("  1. Application cannot perform write actions.")
                    print("  2. Twitter account is suspended.")

                    user["active"] = False;                    
                    break

                if e.api_code == 185:
                    print('')
                    print("- This account reached its daily limit")
                    user["active"] = False;                    
                    break
                if e.api_code == 187:
                    print('')
                    print("- Status is a duplicate. You can try: ")
                    print("  1. Adding more variety of texts to tweet")
                    print("  2. Adding more hashtags to hashtagPoolFile.")
                  #  user["active"] = False;                    
                    break

        if still_active_users == False:
            print("There are no more active users. Exiting...")
            break;

        waitDuration = random.randint(10, 20);
        print("\n- Sleeping for [%d] seconds..." % waitDuration)
        time.sleep(waitDuration)


def main():
    authenticate_users()
    print_users()
    publishTweet()
    
main()
