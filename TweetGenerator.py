import sys
import random

#First argument to script is a file of tweet pool per line.
#Second one is mention/tag/@ pool file. @ per line.

mentionPoolFile = open(sys.argv[2],"r")
TwPoolFile = open(sys.argv[1],"r")
out1 = open("tmp.txt","w")
mentionPool = []
for line in mentionPoolFile:
    target = line.strip()
    mentionPool.append(target)
print mentionPool

for line in TwPoolFile:
    text = line.strip()
    for mention in mentionPool:
        tweetThisText= "Sayin "+mention+" "+text+" #1416ylsy #1416ylsyTAZMINAT"
        #print(tweetThisText)
        out1.write(tweetThisText+"\n")
        out1.write(line.strip()+"\n")

out1.close()

out2 = open("Randomized_TweetPool.txt","w")

with open("tmp.txt",'r') as outfile:
    lines = outfile.readlines()

random.shuffle(lines)
for line in lines:
    print line.strip()
    out2.write(line.strip()+"\n")

#how to run this script:
#python TweetGenerator.py tweetpool_v4.txt tags.txt
