#!/usr/bin/env python
# -*- coding: utf-8 -*-
import icalendar as ical
import datetime as dt
import argparse as ap

#parse command line arguments to script
parser = ap.ArgumentParser()
parser.add_argument("-in", action = "store", dest = "ics_file", help = "Input ics file")
parser.add_argument("-out", action = "store", dest =  "remind_file", help = "Output remind file")

results = parser.parse_args()

leadtime = 20

inFile = results.ics_file #"uni.ics"
outFile = results.remind_file # "test.remind"
#remind syntax
#REM weekday AT time +minutes DURATION hh:mm MSG title %
#REM month day +days (yyyy) MSG title %b %

#strftime format codes
# %a  Locale’s abbreviated weekday name.
# %A  Locale’s full weekday name.      
# %b  Locale’s abbreviated month name.     
# %B  Locale’s full month name.
# %c  Locale’s appropriate date and time representation.   
# %d  Day of the month as a decimal number [01,31].    
# %f  Microsecond as a decimal number [0,999999], zero-padded on the left
# %H  Hour (24-hour clock) as a decimal number [00,23].    
# %I  Hour (12-hour clock) as a decimal number [01,12].    
# %j  Day of the year as a decimal number [001,366].   
# %m  Month as a decimal number [01,12].   
# %M  Minute as a decimal number [00,59].      
# %p  Locale’s equivalent of either AM or PM.
# %S  Second as a decimal number [00,61].
# %U  Week number of the year (Sunday as the first day of the week)
# %w  Weekday as a decimal number [0(Sunday),6].   
# %W  Week number of the year (Monday as the first day of the week)
# %x  Locale’s appropriate date representation.    
# %X  Locale’s appropriate time representation.    
# %y  Year without century as a decimal number [00,99].    
# %Y  Year with century as a decimal number.   
# %z  UTC offset in the form +HHMM or -HHMM.
# %Z  Time zone name (empty string if the object is naive).    
# %%  A literal '%' character.

def rem(start, end, title, rrule = None):
    duration = str(end - start)
    if rrule is None:
        # whole single day events
        # print("REM {} +{} {} MSG {} %b %".format(start.strftime("%b %d"), leadtime, start.strftime("%Y"), title))
        return "REM {} +{} {} MSG {} %b %".format(start.strftime("%b %d"), leadtime, start.strftime("%Y"), title)

    else:
        # weekly recuring event at specific time with duration
        # print("REM {} AT {} +{} DURATION {} MSG {} %".format(start.strftime("%a"), start.strftime("%H:%M"), leadtime, duration, title))
        return "REM {} AT {} +{} DURATION {} MSG {} %".format(start.strftime("%a"), start.strftime("%H:%M"), leadtime, duration, title)


#read ical file
with open(inFile, "rb") as icalFile:
    cal = ical.Calendar.from_ical(icalFile.read())

with open(outFile, "w") as txtFile:
    for evt in cal.walk():
        if evt.name == "VEVENT":
            # print(evt.keys())
            # print(str(evt["summary"]))
            title = evt.get("summary")
            dtstart = evt["dtstart"].dt
            dtend = evt["dtend"].dt
            # print(evt["dtstamp"].dt)
            recur = evt.get("rrule")
            txtFile.write(rem(dtstart, dtend, title, recur) + "\n")

    # if evt.name == "ALARM":
        # print(evt.keys())

