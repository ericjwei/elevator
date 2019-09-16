from time import time, sleep
import threading

from elevatorCar import ElevatorCar 
from constants import RATIO, MAX_FLOOR
    
def elevator1_thread(demand_queue):
  car1 = ElevatorCar(1, list(range(1, MAX_FLOOR + 1)))
  while(True):
  # print(list(demand_queue.queue))
    car1.board(demand_queue) 
    sleep(60 / RATIO)
    car1.TEMPDEBOARD(demand_queue)  

def elevator2_thread(demand_queue):
  None

def control_system(demand_queue):
  elevator1 = threading.Thread(target=elevator1_thread, args=(demand_queue,))
  elevator1.start()
  elevator2 = threading.Thread(target=elevator2_thread, args=(demand_queue,))
  elevator2.start()