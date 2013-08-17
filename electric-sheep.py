#!/bin/env python
#Id,Tz,From,To,Sched,Hours,Rating,Comment,Framerate,Snore,Noise,Cycles,Event

import time

pattern = '%d.%m.%Y %H:%M'
header="matt.sleep"

f = open('sleep-export.csv', 'r')

while True:
    keys = f.readline()
    values = f.readline()
    values2 = f.readline()
    #Read untils you can't reads no mores
    if not values: break

    keys = keys.split(',')
    values = values.split(',')

    dictionary = dict(zip(keys, values))

    #Chop out stuff we don't need
    for item in ['Id','Tz','Sched','Hours','Rating','Comment','Framerate','Snore','Noise','Cycles']:
        dictionary.pop(item)

    #Clean off all event items
    for k in dictionary.keys():
        if k.startswith('\"Event'):
            dictionary.pop(k)

    #Hack out the dates it's for
    day1 = dictionary.pop('From').replace("\"","").replace(". ",".").split()[0]
    day2 = dictionary.pop('To').replace("\"","").replace(". ",".").split()[0]
   
    # DO STUFF!!!1!
    for k in dictionary.keys():
        if int(k.split(":")[0].replace("\"","")) > 12:
            print header, dictionary[k].replace("\"",""), int(time.mktime(time.strptime((day1 + " " + k.replace("\"","")),  pattern)))
        else:
            print header, dictionary[k].replace("\"",""), int(time.mktime(time.strptime((day2 + " " + k.replace("\"","")),  pattern)))

