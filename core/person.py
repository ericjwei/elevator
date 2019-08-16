from datetime import timedelta, datetime, time
from random import random, randint, randrange
from time import strftime, gmtime

class Person:
  def __init__(self, floor = None, begin = None, end = None):
    self.floor = floor
    self.begin = begin
    self.begin = end
  
  def set_begin(self):
    r = random()
    epoch = (datetime.combine(datetime.now().date(), time(0,0,0)) - datetime(1970,1,1)).total_seconds()
    if(r <= .05): #super early (6:15-6:30)
      self.begin = epoch + timedelta(hours=6, minutes=15).total_seconds() + randint(0, 900)
      # self.begin = datetime.time(6,randint(15,30),randint(0, 59))
    elif(r <= .95): #normal (6:30-7:00)
      self.begin = epoch + timedelta(hours=6, minutes=30).total_seconds() + randint(0, 1800)
      # self.begin = datetime.time(6,randint(30,59),randint(0, 59))
    else: #late (7:00-7:30)
      self.begin = epoch + timedelta(hours=7).total_seconds() + randint(0, 1800)
      # self.begin = datetime.time(7,randint(0,30),randint(0, 59))

  def set_end(self):
    r = random()
    epoch = (datetime.combine(datetime.now().date(), time(0,0,0)) - datetime(1970,1,1)).total_seconds()
    if(r <= .10): #early (15:30-16:00)
      self.end = epoch + timedelta(hours=15, minutes=30).total_seconds() + randint(0, 1800)
      # self.end = time(15,randint(30,59),randint(0, 59))
    elif(r <= .95): #normal (16:00-16:30)
      self.end = epoch + timedelta(hours=16).total_seconds() + randint(0, 1800)
      # self.end = datetime.time(16,randint(00,30),randint(0, 59))
    else: #late (16:30-16:45) 
      self.end = epoch + timedelta(hours=16, minutes=30).total_seconds() + randint(0, 900)
      # self.end = datetime.time(16,randint(30,45),randint(0, 59))
  
  def get_begin(self):
    return(self.begin)
  
  def get_end(self):
    return(self.end)

  def print_info(self):
    print(f"Floor: {self.floor:02d} Hours: {strftime('%Y-%m-%d %H:%M:%S', gmtime(self.begin))} - {strftime('%Y-%m-%d %H:%M:%S', gmtime(self.end))}")
