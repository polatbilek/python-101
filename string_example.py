#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 12:25:21 2019

@author: polatbilek
"""
def calculate_hour(curr_time, extra_hour, seconds):
    hour = curr_time[0] + extra_hour + (seconds//3600)
    
    if hour % 24 > 23:
        hour = hour % 24
        
    return hour

def calculate_min(curr_time, extra_min, seconds):
    extra_hour = 0

    if (curr_time[1] + extra_min + ((seconds//60)%60)) > 59:
        extra_hour = 1
        final_min = (curr_time[1] + extra_min + ((seconds//60)%60)) % 60
    else:
        final_min = curr_time[1] + extra_min + ((seconds//60)%60)
        
    return final_min, extra_hour

def calculate_sec(curr_time, seconds):
    extra_min = 0
    
    if (curr_time[2] + (seconds%60)) > 59:
        extra_min = 1
        final_sec = (curr_time[2] + (seconds%60)) % 60
    else:
        final_sec = curr_time[2] + (seconds%60)
        
    return final_sec, extra_min


s = input("Enter the current hour")
seconds_to_add = int(input("Enter the seconds to add"))

splitted = s.split(":")
final_sec, extra_min = calculate_sec([int(splitted[0]),
              int(splitted[1]),
              int(splitted[2])],
                seconds_to_add)

final_min, extra_hour = calculate_min([int(splitted[0]),
                                     int(splitted[1]),
                                     int(splitted[2])],
                                    extra_min,
                                    seconds_to_add)

final_hour = calculate_hour([int(splitted[0]),
                                     int(splitted[1]),
                                     int(splitted[2])],
                                    extra_hour,
                                    seconds_to_add)

print(str(final_hour) + ":" + str(final_min) + ":" + str(final_sec))



