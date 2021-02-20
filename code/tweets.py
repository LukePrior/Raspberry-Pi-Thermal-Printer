#!/usr/bin/python

import os
import tweepy
import textwrap
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--key", "-k", help="set twitter consumer key")
parser.add_argument("--secret", "-s", help="set twitter consumer secret")
parser.add_argument("--query", "-q", help="set search term")
parser.add_argument("--tweets", "-t", help="set number of tweets to return")
args = parser.parse_args()

if args.key:
    consumer_key = str(args.key)
else:
    print("No consumer key")
    exit()

if args.secret:
    consumer_secret = str(args.secret)
else:
    print("No consumer secret")
    exit()

if args.query:
    search = str(args.query)
else:
    search = '@diyodemag'

if args.tweets:
    tweets = int(args.tweets)
else:
    tweets = 3

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)

printer = open("print.txt", "w")

headline = search + " tweets"
headline = textwrap.fill(headline, 20)
printer.write(headline + "\n\n")

for tweet in tweepy.Cursor(api.search, q=search, result_type='popular', tweet_mode='extended').items(tweets):
    name = str(tweet.user.name)
    name = re.sub(r'[^\x00-\x7F]+','', name)
    name = textwrap.fill(name, 20)
    printer.write(name + "\n\n")
    content = tweet.full_text
    content = re.sub(r'[^\x00-\x7F]+', '', content)
    content = re.sub(r'https?:\/\/.*[\r\n]*', '', content, flags=re.MULTILINE)
    content = textwrap.fill(content, 20)
    printer.write(content + "\n\n")

printer.close()

os.system('paps --left-margin=15 --font=\"Courier, Monospace Bold Italic 9\" print.txt | lp')