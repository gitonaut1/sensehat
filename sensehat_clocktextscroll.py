#!/usr/bin/python
from sense_hat import SenseHat
import time, datetime
import datetime
from random import randint
from time import sleep

#http://www.pythonforbeginners.com/basics/python-datetime-time-examples

sense = SenseHat()

print ("Day of the week:", datetime.date.today().strftime("%j"))
print ("Month of year: ", datetime.date.today().strftime("%B"))
print ("Current date and time: " , datetime.datetime.now())

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
        x = randint(0, 7)
        y = randint(0, 7)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        sense.set_pixel(x, y, r, g, b)
        sleep(0.01)

