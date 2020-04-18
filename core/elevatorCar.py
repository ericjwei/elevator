from time import sleep, time, perf_counter
from constants import RATIO, FLOOR_HEIGHT
from math import sqrt

from bisect import insort

ACCELERATION = 1 #1 m/s^2 standard elevator acceleration in the US
MAX_VELOCITY = 10
MAX_DISTANCE = (MAX_VELOCITY ** 2) / (2 * ACCELERATION)  #max distance of constant acceleration for max velocity of 10 m/s
ACCELERATION_TIME = sqrt(FLOOR_HEIGHT / ACCELERATION) #time of acceleration
class ElevatorCar:
  def __init__(self, id, floors, max_capacity = 10, passengers = [], 
      selected_floors = [], current_floor = 1, current_location = 0, current_velocity = 0):
    self.id = id
    self.floors = floors #servicable floors
    self.max_capacity = max_capacity
    self.passengers = passengers
    self.selected_floors = selected_floors #might not need this
    self.current_floor = current_floor

    self.current_location
    self.current_velocity #might not need this
    self.direction #boolean true is up false is down

  def add_stop(self, floor):
    insort(self.selected_floors, floor)

  def track_location(self, depart_time)
    
    direction = 1 if self.direction else -1
      
    while(perf_counter - depart_time < ACCELERATION_TIME):
      sleep(0.5)
    self.current_floor = self.current_floor + direction * 0.5
    depart_time = depart_time + ACCELERATION_TIME

    while()


    #every half floor the elevator will update location
    #floor 0 is lobby, 0.5 is half between lobby and 1st floor



  # Travel to next floor with travel time taken to reach the designated floor
  def travel(self):
    if(not self.selected_floors):
      #return to the lobby
    
    while(True):



    distance = abs(self.current_floor - end) * FLOOR_HEIGHT
    start_time = perf_counter()
    while(True):
      self.current_location = (perf_counter - start_time) ** 2 * ACCELERATION / 2
      self.current_floor = self.current_location / 4.5 + 1

    if(distance <= MAX_DISTANCE * 2):
      while(True):
        sleep(0.5 / RATIO)
        self.current_location = 
        self.current_velocity = ACCELERATION * (time - start_time) 


      sleep(2 * sqrt(distance / ACCELERATION) / RATIO)
    else: #max velocity reached
      sleep(2 * sqrt(distance / ACCELERATION) + (distance - (MAX_DISTANCE * 2)) / MAX_VELOCITY / RATIO)
    self.current_floor = end

  def board(self, queue):
    sleep(2 / RATIO)
    buffer = 5
    while(len(self.passengers) < self.max_capacity and buffer >= 0):
      sleep(.5 / RATIO)
      if(queue.empty() and not self.passengers):
        continue
      elif(queue.empty()):
        buffer -= 1
      else:
        p = queue.get()
        p.print_info()
        self.passengers.append(p)

    sleep(2 / RATIO)
    self.passengers = sorted(self.passengers, key=lambda person: person.floor, reverse=True)

  def TEMPDEBOARD(self, queue):
    self.passengers = []

  def deboard(self):
    #sleep(5 / RATIO)
    while(self.passengers and self.passengers[-1].floor == self.current_floor):
      self.passengers.pop().print_info()
      #floor.append(self.passengers.pop(0))
      sleep(.5 / RATIO)

  def print_passengers(self):
    for p in range(self.passengers):
      p.print_info()

  def print_info(self):
    print(f"Elevator {self.id} Capacity: {len(self.passengers)}")