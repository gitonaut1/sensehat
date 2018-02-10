#!/usr/bin/env python

from sense_hat import SenseHat
import time, datetime
import datetime
from random import randint
from time import sleep

hat = SenseHat()
sense = SenseHat()

print ("Day of the week:", datetime.date.today().strftime("%j"))
print ("Month of year: ", datetime.date.today().strftime("%B"))
print ("Current date and time: " , datetime.datetime.now())

year_color = (192, 192, 192)    #(0, 255, 0)
month_color = (128, 128, 128)
day_color = (255, 0, 0)
hour_color = (0, 255, 0)
minute_color = (255, 0, 255)      #(0, 0, 255)
second_color = (255, 255, 0)
hundrefths_color = (127, 127, 127)

off = (0, 0, 0)

hat.clear()

def display_binary(value, row, color):
	binary_str = "{0:8b}".format(value)
	for x in range(0, 8):
		if binary_str[x] == '1':
			hat.set_pixel(x, row, color)
		else:
			hat.set_pixel(x, row, off)

while True:
        
        #day = datetime.date.today().strftime("%j")
        #sense.set_rotation(180)
        #red = (255, 0, 0)
        #sense.show_message(day, text_colour=red)

        #today = datetime.date.today().strftime("%B")
        #sense.set_rotation(180)
        #red = (255, 0, 0)
        #sense.show_message(today, text_colour=red)

        #date = datetime.datetime.now().strftime("%d.%B %Y-%H:%M")
        date = datetime.datetime.now().strftime("%H:%M")
        #sense.set_rotation(180)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        col = (r, g, b)
        sense.show_message(date, text_colour=col)
        sleep(0.5)

        n = 1000
        while 1 < n:
                n = n-1
                t = datetime.datetime.now()
                display_binary(t.year % 100, 0, year_color)
                display_binary(t.month, 1, month_color)
                display_binary(t.day, 2, day_color)
                display_binary(t.hour, 3, hour_color)
                display_binary(t.minute, 4, minute_color)
                display_binary(t.second, 5, second_color)
                #display_binary(t.microsecond / 10000, 6, hundrefths_color)
                #display_binary(t.microsecond, 6, hundrefths_color)
                time.sleep(0.0001)
