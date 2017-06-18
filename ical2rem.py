#!/usr/bin/env python
# -*- coding: utf-8 -*-
import icalendar as ical

with open("uni.ics", "rb") as icalFile:
    cal = ical.Calendar.from_ical(icalFile.read())

for evt in cal.walk():
    # if evt.name == "VEVENT":
        # print(evt.keys())
        # # print(str(evt["summary"]))
        # print(evt.get("summary"))
        # print(evt["dtstart"].dt)
        # print(evt["dtend"].dt)
        # print(evt["dtstamp"].dt)

    if evt.name == "ALARM":
        print(evt.keys())

