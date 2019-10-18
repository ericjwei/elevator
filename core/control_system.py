from time import time, sleep
import threading
import multiprocessing

from elevatorCar import ElevatorCar 
from constants import RATIO, MAX_FLOOR

def elevator_thread(demand_queue, selected_floors, num):



car = ElevatorCar(num, list(range(1, MAX_FLOOR + 1)))

  while(True):
    car.board(demand_queue) 
    car.print
    _info()

    while(car.passengers):
      car.travel(selected_floors[-1])
      #car.travel(car.passengers[-1].floor)
      car.deboard()

    if(car.selected_floors):
      car.travel(car.selected_floors[-1])
      continue
      #new demand
    
    car.travel(1) #return to lobby
      print(f"Car {num} returned to lobby")


def select_car(elevator_list, floor):
  

def control_system(demand_list):
  elevator_list = [car1, car2]
  car1 = ElevatorCar(1, list(range(1, MAX_FLOOR + 1)))
  car2 = ElevatorCar(2, list(range(1, MAX_FLOOR + 1)))

  
  # Constantly check for demand, if it exists, add the demand to the an elevator following rules
  while(True):
    for floor, queue in enumerate(demand_list):
      if not queue.empty():
        elevator = select_car(elevator_list, floor)
        elevator.add_stop(queue)


  selected_floors = 

  elevator1 = threading.Thread(target=elevator_thread, args=(demand_queue, selected_floors, 1))
  #elevator2 = threading.Thread(target=elevator_thread, args=(demand_queue, elevator_list, car2, 2))
  elevator1.start()
  elevator2.start()
  # elevator2 = threading.Thread(target=elevator2_thread, args=(demand_queue,))
  # elevator2.start()