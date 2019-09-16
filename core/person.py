from datetime import timedelta
from random import random, randint
from time import strftime, gmtime

class Person:
  def __init__(self, floor = None, begin = None, end = None):
    self.floor = floor
    self.begin = begin
    self.end = end
  
  def set_begin(self):
    r = random()
    if(r <= .05): #super early (6:15-6:30)
      #self.begin = timedelta(hours=6, minutes=15).total_seconds() + randint(0, 1800)
      self.begin = timedelta(hours=0, minutes=15).total_seconds() + randint(0, 1800)
    elif(r <= .95): #normal (6:30-7:00)
      #self.begin = timedelta(hours=6, minutes=30).total_seconds() + randint(0, 1800)
      self.begin = timedelta(hours=0, minutes=30).total_seconds() + randint(0, 1800)
    else: #late (7:00-7:30)
      #self.begin = timedelta(hours=7).total_seconds() + randint(0, 1800)
      self.begin = timedelta(hours=1).total_seconds() + randint(0, 1800)

  def set_end(self):
    r = random()
    if(r <= .10): #early (15:30-16:00)
      self.end = timedelta(hours=15, minutes=30).total_seconds() + randint(0, 1800)
    elif(r <= .95): #normal (16:00-16:30)
      self.end = timedelta(hours=16).total_seconds() + randint(0, 1800)
    else: #late (16:30-16:45) 
      self.end = timedelta(hours=16, minutes=30).total_seconds() + randint(0, 900)
  
  def get_begin(self):
    return(self.begin)
  
  def get_end(self):
    return(self.end)

  def print_info(self):
    print(f"Floor: {self.floor:02d} Hours: {strftime('%H:%M:%S', gmtime(self.begin))} - {strftime('%H:%M:%S', gmtime(self.end))}")
