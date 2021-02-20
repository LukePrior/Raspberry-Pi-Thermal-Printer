#!/usr/bin/python

import requests
import textwrap
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--api", "-a", help="set open weather api key")
parser.add_argument("--headlines", "-h", help="number of headlines to return")
args = parser.parse_args()

if args.api:
    api = str(args.api)
else:
    print("No API")
    exit()

if args.headlines:
    headlines = int(args.headlines)
else:
    headlines = 3

apiKey = 'apiKey=' + api

url = ('http://newsapi.org/v2/top-headlines?' + 'country=au&' + str(apiKey))

response = requests.get(url)

printer = open("print.txt", "w")

printer.write("Australian News\n\n")

for article in response.json()['articles'][:headlines]:
    news = str(article['title'])
    news = textwrap.fill(news,20)
    printer.write(str(news) + "\n\n")


printer.close()

os.system('paps --left-margin=15 --font=\"Courier, Monospace Bold Italic 9\" print.txt | lp')