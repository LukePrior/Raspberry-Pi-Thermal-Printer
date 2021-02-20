#!/usr/bin/python

from pyowm import OWM
import time
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--api", "-a", help="set open weather api key")
parser.add_argument("--days", "-d", help="set amount of days to return weather forecast for")
args = parser.parse_args()

if args.api:
    api = str(args.api)
else:
    print("No API")
    exit()

if args.days:
    days = int(args.days)
else:
    days = 3

owm = OWM(api)
mgr = owm.weather_manager()
one_call = mgr.one_call(lat=-32.9278, lon=151.7108)

t = time.time()
daily = 60*60*24

printer = open("print.txt", "w")

printer.write("Weather Report\n\n")

for i in range(days):
    printer.write(time.strftime('%a %d %B', time.localtime(t + (i*daily))) + "\n")
    printer.write("Temperature " + str(round(one_call.forecast_daily[i+1].temperature('celsius').get('day', None), 1)) + "°C\n")
    printer.write("Humidity " + str(one_call.forecast_daily[i+1].humidity) + "%\n")
    printer.write(str(one_call.forecast_daily[i+1].detailed_status).title() + "\n\n")

printer.close()

os.system('paps --left-margin=15 --font=\"Courier, Monospace Bold Italic 9\" print.txt | lp')