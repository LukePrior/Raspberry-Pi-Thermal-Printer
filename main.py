#!/usr/bin/python

from pyowm import OWM
import time
import os

owm = OWM('739fdafe1bfd3ba2fc75b8a614b4e2d1')
mgr = owm.weather_manager()
one_call = mgr.one_call(lat=-32.9278, lon=151.7108)

days = 3

t = time.time()
daily = 60*60*24

printer = open("print.txt", "w")

printer.write("Weather Report\n\n")

for i in range(days):
    printer.write(time.strftime('%a %d %B', time.localtime(t + (i*daily))) + "\n")
    printer.write("Temperature " + str(round(one_call.forecast_daily[i+1].temperature('celsius').get('day', None), 1)) + u'\N{DEGREE SIGN}' + "C\n")
    printer.write("Humidity " + str(one_call.forecast_daily[i+1].humidity) + "%\n")
    printer.write(str(one_call.forecast_daily[i+1].detailed_status).title() + "\n\n")

printer.close()

os.system("lp print.txt")