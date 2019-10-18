from time import time, sleep
import threading

from elevatorCar import ElevatorCar 
from constants import RATIO, MAX_FLOOR

def elevator_thread(demand_queue, car, num):
  for() 

  while(True):
    car.board(demand_queue) 
    print(f"Car {num} leaving")

    while(car.passengers):
      car.travel(car.passengers[-1].floor)
      car.deboard()

    car.travel(1) #return to lobby
    print(f"Car {num} returned to lobby")


def control_system(demand_queue):
  car1 = ElevatorCar(1, list(range(1, MAX_FLOOR + 1)))
  car2 = ElevatorCar(1, list(range(1, MAX_FLOOR + 1)))

  elevator_list = [car1, car2]

  elevator1 = threading.Thread(target=elevator_thread, args=(demand_queue, car1, 1))
  elevator2 = threading.Thread(target=elevator_thread, args=(demand_queue, car2, 2))
  elevator1.start()
  elevator2.start()
  # elevator2 = threading.Thread(target=elevator2_thread, args=(demand_queue,))
  # elevator2.start()