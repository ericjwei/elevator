from time import sleep
from constants import RATIO

class ElevatorCar:
  def __init__(self, id, floors, max_capacity = 10, passengers = []):
    self.id = id
    self.floors = floors
    self.max_capacity = max_capacity
    self.passengers = passengers

  def board(self, queue):
    buffer = 5
    while(len(self.passengers) < self.max_capacity and buffer > 0):
      sleep(.5 / RATIO)
      if(queue.empty() and len(self.passengers) == 0):
        continue
      elif(queue.empty()):
        buffer -= 1
      else:
        p = queue.get()
        p.print_info()
        self.passengers.append(p)
    sleep(2 / RATIO)
    self.passengers = sorted(self.passengers, key=lambda person: person.floor)
    print("leaving")

  def TEMPDEBOARD(self, queue):
    self.passengers = []

  def deboard(self, floor_num, floor):
    sleep(2 / RATIO)
    while(self.passengers[0].floor == floor_num):
      floor.append(self.passengers.pop(0))
      sleep(.5 / RATIO)

  def print_passengers(self):
    for p in range(self.passengers):
      p.print_info()

  def print_info(self):
    print(f"Elevator {self.id} Capacity: {len(self.passengers)}")