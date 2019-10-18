from datetime import timedelta
from random import random, randint
from time import strftime, gmtime

from constants import SHIFT_START, SHIFT_END, MAX_FLOOR

class Person:
  def __init__(self, floor = randint(2, MAX_FLOOR), shift_start = SHIFT_START, shift_end = SHIFT_END):
    self.floor = floor #which floor they work
    # self.begin = begin #set begin time
    # self.end = end #set end time
  
    r = random()
    if(r <= .05): #super early 45min - 30min early
      #self.begin = timedelta(hours=6, minutes=15).total_seconds() + randint(0, 1800)
      # self.begin = timedelta(hours=0, minutes=15).total_seconds() + randint(0, 1800)
      self.begin = (shift_start - timedelta(minutes=45)).total_seconds() + randint(0, 900)
    elif(r <= .95): #normal 30min - 0min early
      #self.begin = timedelta(hours=6, minutes=30).total_seconds() + randint(0, 1800)
      # self.begin = timedelta(hours=0, minutes=30).total_seconds() + randint(0, 1800)
      self.begin = (shift_start - timedelta(minutes=30)).total_seconds() + randint(0, 1800)
    else: #late < 30min late
      #self.begin = timedelta(hours=7).total_seconds() + randint(0, 1800)
      # self.begin = timedelta(hours=1).total_seconds() + randint(0, 1800)
      self.begin = shift_start.total_seconds() + randint(0, 1800)

    r = random()
    if(r <= .10): #early 30min early
      # self.end = timedelta(hours=15, minutes=30).total_seconds() + randint(0, 1800)
      self.end = (shift_end - timedelta(minutes=30)).total_seconds() + randint(0, 1800)
    elif(r <= .95): #normal on time to 30min after shift
      # self.end = timedelta(hours=16).total_seconds() + randint(0, 1800)
      self.end = shift_end.total_seconds() + randint(0, 1800)
    else: #late 30min to 45min after shift
      # self.end = timedelta(hours=16, minutes=30).total_seconds() + randint(0, 900)
      self.end = (shift_end + timedelta(minutes=30)).total_seconds() + randint(0, 900)

  def print_info(self):
    print(f"Floor: {self.floor:02d} Hours: {strftime('%H:%M:%S', gmtime(self.begin))} - {strftime('%H:%M:%S', gmtime(self.end))}")
